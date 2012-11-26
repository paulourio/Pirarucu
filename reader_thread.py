# -*- encoding: utf-8 -*-
import threading
import time
import serial
from PyQt4 import QtCore
from tradutor import Tradutor

class ReaderThread(QtCore.QThread):
	def __init__(self, texto, config):
		QtCore.QThread.__init__(self)
		#threading.Thread.__init__(self)
		self.config = config
		self.texto = texto
		self.lista = texto.split()
		self.tr = Tradutor(texto)
		self.porta = '/dev/ttyUSB1'
		try:
			self.com = serial.Serial(self.porta, 19200, timeout=1)
		except serial.SerialException:
			self.config.statusBar.emit(QtCore.SIGNAL('update(QString)'), 'Não foi possível abrir a porta ' + self.porta)
		#com.read(10)
	
	def EnviarLetra(self, letra):
		tempo = (1 << 7) + self.config.tempo_celula
		self.com.write(bytes([tempo, int(letra, 2)]))
	
	def MontarBraille(self, palavras):
		self.braille = ''
		for palavra in palavras:
			for letra in palavra['letras']:
				self.braille += letra[1]
			self.braille += '⠀'
	
	def AtualizarTexto(self, indice):
		novo = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
				<html><head><meta name="qrichtext" content="1" /><style type="text/css">
				p, li { white-space: pre-wrap; }
			</style></head><body><p>"""
		novo += ' '.join( self.lista[:indice] )
		novo += '<span style=" font-weight:600; color:#0000c0;"> ' 
		novo += self.lista[indice] + '</span> ' 
		novo += ' '.join( self.lista[indice + 1:] ) + "</p></body></html>"
		self.config.AtualizarDestaqueTexto(novo)
		
	def AtualizarBraille(self, indice):
		antes = self.braille[:indice]
		depois = self.braille[indice + 1:]
		if len(self.braille) > 38:
			ia = indice - 18
			if ia < 0:
				ia = 0
			antes = self.braille[ia:indice]
			id = indice + 18
			if indice < 18:
				id += abs(indice - 18)
			depois = self.braille[indice + 1:id]
		novo = '<html><head/><body>'#<span style=" font-size:16pt; color:#000000;">⠁ ⠉⠑⠓⠑</span></p></body></html>
		novo += antes
		novo += '<span style="font-size:16pt; color:#0000c0;">' 
		novo += self.braille[indice] + '</span>'
		novo += depois
		self.config.AtualizarTextoBraille(novo)		
		
	def stop(self):
		self.ativo = False
		
	def run(self):
		if not hasattr(self, 'com'):
			print('Leitura abortada: não foi possível abrir a porta ' + self.porta)
			return		
		self.ativo = True
		self.MontarBraille(self.tr.data['palavras'])
		indice_total = 0
		for ip, palavra in enumerate( self.tr.data['palavras'] ):
			self.AtualizarTexto(ip)
			lp = len(palavra['letras'])
			for i, letra in enumerate(palavra['letras']):
				print(letra)
				if type(letra[2]) is list:
					for l in letra[2]:
						self.EnviarLetra(l)
						self.AtualizarBraille(indice_total)
						indice_total += 1
						if i + 1 < lp:
							proxima = palavra['letras'][i+1]
						else:
							proxima = [None, None, None, '']
						time.sleep(self.config.tempo_celula / 50)						
				else:
					self.EnviarLetra(letra[2])
					self.AtualizarBraille(indice_total)
					indice_total += 1
					if i + 1 < lp:
						proxima = palavra['letras'][i+1]
					else:
						proxima = [None, None, None, '']
					self.config.AtualizarLeds(letra, proxima)
					time.sleep(self.config.tempo_celula / 50)
				if not self.ativo:
					self.com.close()
					return
			self.AtualizarBraille(indice_total)
			indice_total += 1
			if palavra['última']:
				letra = [None, None, None, '']
				self.config.AtualizarLeds(letra, letra)
				time.sleep(self.config.tempo_sentencas / 50)
			else:
				time.sleep(self.config.tempo_palavras  / 50	)
		self.com.close()
