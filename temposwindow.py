# -*- encoding: utf-8 -*-
from PyQt4.QtGui import QApplication, QDialog
from PyQt4.QtCore import SIGNAL
from ui_temposwindow import Ui_TemposWindow

class TemposWindow(QDialog, Ui_TemposWindow):
	def __init__(self, tempo_celula, tempo_palavras, tempo_sentencas, parent=None):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		
		x = (QApplication.desktop().width() - self.width()) * .5
		y = (QApplication.desktop().height() - self.height()) * .5
		self.move(x, y)
		
		self.connect(self.hsCelulaAtiva, SIGNAL('valueChanged(int)'), self.hsCelulaAtivaChange)
		self.connect(self.hsPalavra, SIGNAL('valueChanged(int)'), self.hsPalavraChange)
		self.connect(self.hsSentencas, SIGNAL('valueChanged(int)'), self.hsSentencasChange)

		# Quando chamado setValue, se o QSlider já está na posição
		# desejada, não é gerado um evento valueChanged(int).
		self.tempo_celula = tempo_celula
		self.tempo_palavras = tempo_palavras
		self.tempo_sentencas = tempo_sentencas
		self.hsCelulaAtiva.setValue(tempo_celula)
		self.hsPalavra.setValue(tempo_palavras)
		self.hsSentencas.setValue(tempo_sentencas)

	def hsCelulaAtivaChange(self, value):
		self.labelCelulaAtiva.setText('%.1f segundos' % (value / 50))
		self.tempo_celula = value

	def hsPalavraChange(self, value):
		self.labelPalavra.setText('%.1f segundos' % (value / 50))
		self.tempo_palavras = value

	def hsSentencasChange(self, value):
		self.labelSentenca.setText('%.1f segundos' % (value / 50))
		self.tempo_sentencas = value
