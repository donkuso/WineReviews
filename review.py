
class Review:
  """
  Represents a single wine review
  Attributes: 
    ID (int)
    country (str)
    description (str)
    designation (str)
    points (int)
    price (float)
    province (str)
    region_1 (str)
    region_2 (str)
    variety (str)
    winery (str)
  """
  def __init__(self, ID=0, country="", description="", designation="", points=0, price=0.0, province="", region_1="", region_2="", variety="", winery=""):
    self.ID = int(ID)
    self.country = country
    self.description = description
    self.designation = designation
    self.points = int(points)
    self.price = float(price)
    self.province = province
    self.region_1 = region_1
    self.region_2 = region_2
    self.variety = variety
    self.winery = winery
  def __str__(self):
    """
    Returns a formatted string:
    <country> [<province>: <region_1> / <region_2>] -- <points> pts, $<price>
    """
    Return f"{self.country} [{self.province}: {self.region_1} / {self.region_2}] -- {self.points} pts, ${self.price}"
