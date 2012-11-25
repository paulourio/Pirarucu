# -*- encoding: utf-8 -*-
import threading
import time
from tradutor import Tradutor

class ReaderThread(threading.Thread):
	def __init__(self, texto, config):
		threading.Thread.__init__(self)
		self.config = config
		self.texto = texto
		self.tr = Tradutor(texto)
	
	def MontarBraille(self, palavras):
		self.braille = ''
		for palavra in palavras:
			for letra in palavra['letras']:
				self.braille += letra[1]
			self.braille += ' '
	
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
		for palavra in self.tr.data['palavras']:
			lp = len(palavra['letras'])
			for i, letra in enumerate(palavra['letras']):
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
					return
			self.AtualizarBraille(indice_total)
			indice_total += 1
			if palavra['última']:
				letra = [None, None, None, '']
				self.config.AtualizarLeds(letra, letra)
				time.sleep(self.config.tempo_sentencas / 50)
			else:
				time.sleep(self.config.tempo_palavras  / 50	)
