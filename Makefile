

default: icones_rc.py ui_mainwindow.py ui_temposwindow.py

ui_mainwindow.py: main.ui
	pyuic4 main.ui > ui_mainwindow.py

ui_temposwindow.py: tempos.ui
	pyuic4 tempos.ui > ui_temposwindow.py

icones_rc.py: icones.qrc
	pyrcc4 -py3 icones.qrc > icones_rc.py

clean:
	$(RM) ui_mainwindow.py ui_temposwindow.py icones_rc.py

