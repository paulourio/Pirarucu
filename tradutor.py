# -*- encoding: utf-8 -*-
from braille import Braille
import re

class Tradutor(object):
	def __init__(self, texto):
		self.processar(texto)
	
	def processar(self, texto):
		data = dict()
		words = list()
		
		data[Braille.ALLCAPS] = texto.upper() == texto # FIXME: ALLCAPS se for só números
	
		palavras = texto.split()
		for p in palavras:
			words.append(self.converter_palavra(p, data[Braille.ALLCAPS]))
	
		data['palavras'] = words
		self.data = data
	
	def converter_palavra(self, palavra, ignorar_caps):
		p = dict()
		p[Braille.NUMERO] = self.is_integer(palavra)
		p[Braille.CAPS] = palavra.upper() == palavra and not ignorar_caps and not p[Braille.NUMERO]
		letras = list()
		if p[Braille.CAPS]:
			letras.append([None] + Braille.MEC2002[Braille.CAPS])
		if p[Braille.NUMERO]:
			letras.append([None] + Braille.MEC2002[Braille.NUMERO])
		for l in palavra:
			if l.upper() == l and re.match("[A-Za-z]", l) and not p[Braille.CAPS] and not ignorar_caps:
				letras.append([None] + Braille.MEC2002[Braille.MAIUSCULA])
			try:
				ll = Braille.MEC2002[l.lower()]
				letras.append([l.lower()] + ll)
			except:
				pass
		p['letras'] = letras
		p['última'] = p['letras'][-1][0] == '.'
		return p
		
	def is_integer(self, valor):
		return re.match("^[\d]+[.,]?$", valor) is not None

if __name__ == '__main__':
	tr = Tradutor('Paulo Roberto Urio, nascido em 1991.')
	for t in tr.data['palavras']:
		print (t)
