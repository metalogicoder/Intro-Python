# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon

  def get_info(self):
    return ['{}: {}'.format(k, v) for k, v in self.__dict__.items()]
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.

class Waypoint(LatLon):
  def __init__(self, lat, lon, name):
    LatLon.__init__(self, lat, lon)
    self.name = name

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
  def __init__(self, lat, lon, name, difficulty, size):
    Waypoint.__init__(self, lat, lon, name)
    self.difficulty = difficulty
    self.size = size

# Make a new waypoint "Catacombs", 41.70505, -121.51521

catacombs_wp = Waypoint(41.70505, -121.51521, 'Catacombs')
w = catacombs_wp.get_info()

# Print it
#
# Without changing the following line, how can you make it print into something
# more human-readable?
print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

newberry_gc = Geocache(44.052137, -121.41556, 'Newberry Views', 1.5, 2)
g = newberry_gc.get_info()

# Print it--also make this print more nicely
print(g)
