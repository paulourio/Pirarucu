# -*- encoding: utf-8 -*-
from PyQt4.QtGui import QApplication, QMainWindow, QDialog
from PyQt4.QtCore import SIGNAL
from ui_mainwindow import Ui_MainWindow
from temposwindow import TemposWindow
from reader_thread import ReaderThread

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, app, parent=None):
		QMainWindow.__init__(self, parent)
		self.setupUi(self)
		
		self.app = app
		
		#x = (QApplication.desktop().width() - self.width()) * .5
		#y = (QApplication.desktop().height() - self.height()) * .5
		#self.move(x, y)
		
		self.connect(self.hsTempo, SIGNAL('valueChanged(int)'), self.update_tempo_celula)
		self.connect(self.btAjusteTempo, SIGNAL('clicked()'), self.btAjusteTempoClicked)
		
		self.hsTempo.setValue(60)
		self.tempo_palavras = 60
		self.tempo_sentencas = 70
		
		self.texto.setText('Louis Braille nasceu em Coupvray (em França) em 1809. Ele perdeu a visão aos três anos. Quatro anos depois, ele ingressou no Instituto de Cegos de Paris. Em 1827, então com dezoito anos, tornou-se professor desse instituto. Ao ouvir falar de um sistema de pontos e buracos inventado por um oficial para ler mensagens durante a noite em lugares onde seria perigoso acender a luz, ele fez algumas adaptações no sistema de pontos em alto relevo.')
		
		self.connect(self.btIniciar, SIGNAL('clicked()'), self.btIniciarClicked)
		self.connect(self.btParar, SIGNAL('clicked()'), self.btPararClicked)
		self.connect(self.lbLetraAtual, SIGNAL('update(QString)'), self.lbLetraAtualUpdate)
		self.connect(self.lbLetraProxima, SIGNAL('update(QString)'), self.lbLetraProximaUpdate)
		self.connect(self.texto, SIGNAL('update(QString)'), self.TextoUpdate)
		self.connect(self.lbBraille, SIGNAL('update(QString)'), self.lbBrailleUpdate)
		self.connect(self.statusBar, SIGNAL('update(QString)'), self.statusBarUpdate)
		
		self.connect(self.led1, SIGNAL('update(QString)'), self.LedAtualUpdate)
		self.connect(self.pled1, SIGNAL('update(QString)'), self.LedProximoUpdate)

	def update_tempo_celula(self, value):
		self.lblTempo.setText('%.1f segundos' % (value / 50))
		self.tempo_celula = value
		
	def btAjusteTempoClicked(self):
		tempos = TemposWindow(self.tempo_celula, self.tempo_palavras, self.tempo_sentencas, self)
		if tempos.exec_() == 1:
			self.hsTempo.setValue(tempos.tempo_celula)
			self.tempo_palavras = tempos.tempo_palavras
			self.tempo_sentencas = tempos.tempo_sentencas
			
	def btIniciarClicked(self):
		conteudo = self.texto.toPlainText()
		if conteudo != '':
			self.IniciarLeitura(conteudo)
			
	def btPararClicked(self):
		if hasattr(self, 'reader'):
			self.reader.stop()

	def IniciarLeitura(self, conteudo):
		self.reader = ReaderThread(conteudo, self)
		self.reader.start()
		
	def statusBarUpdate(self, texto):
		self.statusBar.message(texto)		
	
	def AtualizarLeds(self, atual, proxima):
		if atual[0] is not None:
			self.lbLetraAtual.emit(SIGNAL('update(QString)'), atual[0].upper())
		else:
			self.lbLetraAtual.emit(SIGNAL('update(QString)'), '')
		self.AtualizarLedsAtual(atual[2])			
		self.statusBar.emit(SIGNAL('update(QString)'), 'Atual: ' + atual[3])
		if proxima[0] is not None:
			self.lbLetraProxima.emit(SIGNAL('update(QString)'), '<html><head/><body><p><span style=" color:#808080;">' + proxima[0].upper() + '</span></p></body></html>')
		else:
			self.lbLetraProxima.emit(SIGNAL('update(QString)'), '')
		self.AtualizarLedsProximo(proxima[2])
		self.app.processEvents()
		
	def AtualizarLedsAtual(self, bits):
		if not bits:
			bits = '000000'
		self.led1.emit(SIGNAL('update(QString)'), bits)
			
	def LedAtualUpdate(self, bits):
		self.led1.setState(bits[0] == '1')
		self.led2.setState(bits[1] == '1')
		self.led3.setState(bits[2] == '1')
		self.led4.setState(bits[3] == '1')
		self.led5.setState(bits[4] == '1')
		self.led6.setState(bits[5] == '1')
		
	def AtualizarLedsProximo(self, bits):
		if not bits:
			bits = '000000'
		self.pled1.emit(SIGNAL('update(QString)'), bits)
	
	def LedProximoUpdate(self, bits):
		self.pled1.setState(bits[0] == '1')
		self.pled2.setState(bits[1] == '1')
		self.pled3.setState(bits[2] == '1')
		self.pled4.setState(bits[3] == '1')
		self.pled5.setState(bits[4] == '1')
		self.pled6.setState(bits[5] == '1')	
		
	def lbLetraAtualUpdate(self, texto):
		self.lbLetraAtual.setText(texto)
			
	def lbLetraProximaUpdate(self, texto):
		self.lbLetraProxima.setText(texto)

	def TextoUpdate(self, texto):
		self.texto.setHtml(texto)
		print('== Destaque atualizado')
	
	def lbBrailleUpdate(self, texto):
		self.lbBraille.setText(texto)
		
	def AtualizarTextoBraille(self, texto):
		self.lbBraille.emit(SIGNAL('update(QString)'), texto)
		self.app.processEvents()
		
	def AtualizarDestaqueTexto(self, novo):
		self.texto.emit(SIGNAL('update(QString)'), novo)
		self.app.processEvents()
