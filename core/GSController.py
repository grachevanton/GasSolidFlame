import GSView
import GSModel

class GSController():
  def __init__(self):
    self.view = GSView.GSMainWindow()
    self.model = GSModel.GSCalc()

    self.view.show()