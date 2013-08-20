class Arm:
  def __init__(self):
    self.value = 0
    self.num_played = 0
  def __repr__(self):
    return "'%s : %d'" % (str(self.value), self.num_played)
  def __cmp__(self, other):
    return cmp(self.value, other.value)
  def __eq__(self, other):
    return self.value == other.value
