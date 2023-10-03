class Action:
  def __init__(self,action_name,action) -> None:
    self.name = action_name
    self.action = action
  def run(self,*args):
    self.action(*args)

def test_a():
  print('test_a')

def test_b():
  print('test_b')

action1 = Action('go',test_a)
action2 = Action('no go',test_b)

action1.run()
action2.run()
