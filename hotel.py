from plan import (
  p1h1, p2h1, p3h1, p4h1, p5h1,
  p1h2, p2h2, p3h2,
  p1h3, p2h3, p3h3, p4h3, p5h3,
  p1h4, p2h4, p3h4, p4h4,
  p1h5, p2h5, p3h5
)
from habitacion import (
  h1h1, h2h1, h3h1, h4h1, h5h1,
  h1h2, h2h2, h3h2,
  h1h3, h2h3, h3h3, h4h3, h5h3,
  h1h4, h2h4, h3h4, h4h4,
  h1h5, h2h5, h3h5
)

class Hotel:
  def __init__(self, nombrehotel, estrellas, capacidad, minibar):
    self.nombrehotel = nombrehotel
    self.estrellas = estrellas
    self.capacidad = capacidad
    self.minibar = minibar
    self.planes = []
    self.habitaciones = []
  def agregar_plan(self, plan):
    self.planes.append(plan)

  def agregar_habitacion(self, habitacion):
    self.habitaciones.append(habitacion)


h1 = Hotel("El Paraiso", 4, 25, 50000)
h2 = Hotel("Descansar", 3, 15, 30000)
h3 = Hotel("Caribbean Resort", 5, 150, 100000)
h4 = Hotel("Hotel del Mar", 4, 50, 40000)
h5 = Hotel("Hotel Palmas", 3, 30, 20000)


for p in [p1h1, p2h1, p3h1, p4h1, p5h1]:
  h1.agregar_plan(p)
for h in [h1h1, h2h1, h3h1, h4h1, h5h1]:
  h1.agregar_habitacion(h)

for p in [p1h2, p2h2, p3h2]:
  h2.agregar_plan(p)
for h in [h1h2, h2h2, h3h2]:
  h2.agregar_habitacion(h)

for p in [p1h3, p2h3, p3h3, p4h3, p5h3]:
  h3.agregar_plan(p)
for h in [h1h3, h2h3, h3h3, h4h3, h5h3]:
  h3.agregar_habitacion(h)

for p in [p1h4, p2h4, p3h4, p4h4]:
  h4.agregar_plan(p)
for h in [h1h4, h2h4, h3h4, h4h4]:
  h4.agregar_habitacion(h)

for p in [p1h5, p2h5, p3h5]:
  h5.agregar_plan(p)
for h in [h1h5, h2h5, h3h5]:
  h5.agregar_habitacion(h)
