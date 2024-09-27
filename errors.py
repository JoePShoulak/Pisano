class InvalidHeightError(Exception):
  def __init__(self, height, period):
    self.height = height
    self.period = period

  def __str__(self):
    return f"Height {self.height} is invalid, not a factor of the period {self.period}"
  
class InvalidModulusError(Exception):
  def __init__(self, modulus):
      self.modulus = modulus

  def __str__(self):
      return f"Modulus {self.modulus} is invalid; it must be greater than or equal to 3."
      