class Library:
  def __init__(self) -> None:
    self.lib = {}
  def add(self,key,value):
    self.lib[key] = value
  def remove(self,key):
    val = self.lib.pop(key,None)
    return val
  def call(self,key):
    if key in self.lib:
      return self.lib[key]
    else:
      return None


def test_library():
  test = Library()
  test.add(1,'kuku')
  test.add(2,'foo')
  test.add(3,'bar')
  var = test.call(2)
  print(var)

  var = test.remove(1)
  print(var)
  var = test.call(1)
  print(var)

if __name__ == "__main__":
  test_library()