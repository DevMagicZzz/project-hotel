from habitacion import (
  h1h1, h2h1, h3h1, h4h1, h5h1,
  h1h2, h2h2, h3h2,
  h1h3, h2h3, h3h3, h4h3, h5h3,
  h1h4, h2h4, h3h4, h4h4,
  h1h5, h2h5, h3h5
)

class Plan:
  def __init__(self, nombreplan, habitacion, noches, costo):
    self.nombreplan = nombreplan
    self.habitacion = habitacion
    self.noches = noches
    self.costo = costo


p1h1 = Plan("Basic",     h1h1, 3,  85000)
p2h1 = Plan("Mid",       h2h1, 3, 120000)
p3h1 = Plan("High",      h3h1, 3, 180000)
p4h1 = Plan("Deluxe",    h4h1, 3, 250000)
p5h1 = Plan("Exclusive", h5h1, 5, 200000)


p1h2 = Plan("Económico", h1h2, 2,  45000)
p2h2 = Plan("Estándar",  h2h2, 3,  90000)
p3h2 = Plan("Confort",   h3h2, 4, 200000)


p1h3 = Plan("Resort Basic",     h1h3, 3, 130000)
p2h3 = Plan("Resort Mid",       h2h3, 3, 220000)
p3h3 = Plan("Resort Premium",   h3h3, 5, 550000)
p4h3 = Plan("Resort Deluxe",    h4h3, 5, 800000)
p5h3 = Plan("Resort Exclusive", h5h3, 7, 500000)


p1h4 = Plan("Mar Basic",   h1h4, 2,  60000)
p2h4 = Plan("Mar Mid",     h2h4, 3, 140000)
p3h4 = Plan("Mar Premium", h3h4, 4, 280000)
p4h4 = Plan("Mar Deluxe",  h4h4, 5, 520000)


p1h5 = Plan("Palmas Basic",  h1h5, 2,  38000)
p2h5 = Plan("Palmas Mid",    h2h5, 3,  80000)
p3h5 = Plan("Palmas Confort",h3h5, 4, 190000)
