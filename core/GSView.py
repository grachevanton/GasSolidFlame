from PySide import QtCore, QtGui

from res import GasSolidFlame_rc

#Main window form

class GSMainWindow(QtGui.QMainWindow):
  def __init__(self):
    super(GSMainWindow, self).__init__()

    self.setWindowTitle("GasSolidFlame")

    self.createActions()
    self.createMenus()
    self.createToolBars()

    self.parametersForm = GSParametersForm()

  def new(self):
    pass

  def open(self):
    pass

  def save(self):
    pass

  def saveAs(self):
    pass

  def close(self):
    pass

  def editPars(self):
    self.parametersForm.show()

  def run(self):
    pass

  def pause(self):
    pass

  def stop(self):
    pass

  def about(self):
    pass

  def createActions(self):
    self.newAct = QtGui.QAction(QtGui.QIcon(':/images/new.png'),
                                "&New", self,
                                shortcut=QtGui.QKeySequence.New,
                                statusTip="Create a new experiment",
                                triggered=self.new
                                )

    self.openAct = QtGui.QAction(QtGui.QIcon(':/images/open.png'),
                                "&Open", self,
                                shortcut=QtGui.QKeySequence.Open,
                                statusTip="Open an existing experiment",
                                triggered=self.open
                                )

    self.saveAct = QtGui.QAction(QtGui.QIcon(':/images/save.png'),
                                "&Save", self,
                                shortcut=QtGui.QKeySequence.Save,
                                statusTip="Save experiment to disk",
                                triggered=self.save
                                )

    self.saveAsAct = QtGui.QAction("Save &As ...", self,
                                shortcut=QtGui.QKeySequence.SaveAs,
                                statusTip="Save experiment under a new name",
                                triggered=self.saveAs
                                )

    self.exitAct = QtGui.QAction("E&xit", self,
                                shortcut="Ctrl+Q",
                                statusTip="Exit the application",
                                triggered=self.close
                                )

    self.parametersAct = QtGui.QAction(QtGui.QIcon(':/images/parameters.png'),
                                "Parameters", self,
                                shortcut="Ctrl+O",
                                statusTip="Edit parameters of experiment",
                                triggered=self.editPars
                                )

    self.runAct = QtGui.QAction(QtGui.QIcon(':/images/run.png'),
                                "&Run", self,
                                shortcut="Ctrl+R",
                                statusTip="Run experiment",
                                triggered=self.run
                                )

    self.pauseAct = QtGui.QAction(QtGui.QIcon(':/images/pause.png'),
                                "&Pause", self,
                                shortcut="Ctrl+P",
                                statusTip="Pause experiment",
                                triggered=self.pause
                                )

    self.stopAct = QtGui.QAction(QtGui.QIcon(':/images/stop.png'),
                                "S&top", self,
                                shortcut="Ctrl+T",
                                statusTip="Stop experiment",
                                triggered=self.stop
                                )

    self.aboutAct = QtGui.QAction(QtGui.QIcon(':/images/about.png'),
                                "&About", self,
                                shortcut="Ctrl+A",
                                statusTip="About programm",
                                triggered=self.about
                                )


  def createMenus(self):
    self.fileMenu = self.menuBar().addMenu("&File")
    self.fileMenu.addAction(self.newAct)
    self.fileMenu.addAction(self.openAct)
    self.fileMenu.addAction(self.saveAct)
    self.fileMenu.addAction(self.saveAsAct)
    self.fileMenu.addSeparator()
    self.fileMenu.addAction(self.exitAct) # ? Not working on my Mac

    self.editMenu = self.menuBar().addMenu("&Edit")
    self.editMenu.addAction(self.parametersAct)

    self.menuBar().addSeparator()

    self.runMenu = self.menuBar().addMenu("Run")
    self.runMenu.addAction(self.runAct)
    self.runMenu.addAction(self.pauseAct)
    self.runMenu.addAction(self.stopAct)

    self.aboutMenu = self.menuBar().addMenu("About")
    self.aboutMenu.addAction(self.aboutAct)

  def createToolBars(self):
    self.fileToolBar = self.addToolBar("File")
    self.fileToolBar.addAction(self.newAct)
    self.fileToolBar.addAction(self.openAct)
    self.fileToolBar.addAction(self.saveAct)

    self.editToolBar = self.addToolBar("Edit")
    self.editToolBar.addAction(self.parametersAct)

    self.runToolBar = self.addToolBar("Run")
    self.runToolBar.addAction(self.runAct)
    self.runToolBar.addAction(self.pauseAct)
    self.runToolBar.addAction(self.stopAct)

    self.aboutToolBar = self.addToolBar("About")
    self.aboutToolBar.addAction(self.aboutAct)

# Parameters widget
class GSParametersForm(QtGui.QWidget):
  def __init__(self, parent=None):
    super(GSParametersForm, self).__init__(parent)

    self.setWindowTitle("Parameters of experiment")
    self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
