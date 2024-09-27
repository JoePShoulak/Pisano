class InvalidHeightError(Exception):
  def __init__(self, height, period):
    self.height = height
    self.period = period

  def __str__(self):
    return f"Height {self.height} is invalid, not a factor of the period {self.period}"
  