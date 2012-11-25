# -*- encoding: utf-8 -*-
import threading
import time
import serial
from tradutor import Tradutor

class ReaderThread(threading.Thread):
	def __init__(self, texto, config):
		threading.Thread.__init__(self)
		self.config = config
		self.texto = texto
		self.lista = texto.split()
		self.tr = Tradutor(texto)
		self.com = serial.Serial('/dev/ttyUSB1', 19200, timeout=1)
		#com.read(10)
	
	def EnviarLetra(self, letra):
		tempo = (1 << 7) + self.config.tempo_celula
		self.com.write(bytes([tempo, int(letra, 2)]))
	
	def MontarBraille(self, palavras):
		self.braille = ''
		for palavra in palavras:
			for letra in palavra['letras']:
				self.braille += letra[1]
			self.braille += ' '
	
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
		novo = '<html><head/><body>'#<span style=" font-size:16pt; color:#000000;">⠁ ⠉⠑⠓⠑</span></p></body></html>
		novo += self.braille[:indice]
		novo += '<span style="font-size:16pt; color:#0000c0;">' 
		novo += self.braille[indice] + '</span>'
		novo += self.braille[indice + 1:]
		self.config.lbBraille.setText(novo)		
		
	def stop(self):
		self.ativo = False
		
	def run(self):
		self.ativo = True
		self.MontarBraille(self.tr.data['palavras'])
		indice_total = 0
		for ip, palavra in enumerate( self.tr.data['palavras'] ):
			#self.AtualizarTexto(ip)
			lp = len(palavra['letras'])
			for i, letra in enumerate(palavra['letras']):
				self.EnviarLetra(letra[2])
				print(letra)
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
