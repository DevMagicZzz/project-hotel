from hotel import h1, h2, h3, h4, h5

class Ciudad:
  def __init__(self, nombreciudad):
    self.nombreciudad = nombreciudad
    self.hoteles = []

  def agregar_hotel(self, hotel):
    self.hoteles.append(hotel)

ciudades = []

c1 = Ciudad("Barranquilla")
c2 = Ciudad("Bogotá")
c3 = Ciudad("Medellin")
c4 = Ciudad("Cartagena")
c5 = Ciudad("Cali")

ciudades.append(c1)
ciudades.append(c2)
ciudades.append(c3)
ciudades.append(c4)
ciudades.append(c5)

c1.agregar_hotel(h1)
c1.agregar_hotel(h2)
c1.agregar_hotel(h3)

c2.agregar_hotel(h1)
c2.agregar_hotel(h4)
c2.agregar_hotel(h5)

c3.agregar_hotel(h2)
c3.agregar_hotel(h3)
c3.agregar_hotel(h5)

c4.agregar_hotel(h1)
c4.agregar_hotel(h3)
c4.agregar_hotel(h4)

c5.agregar_hotel(h2)
c5.agregar_hotel(h4)
c5.agregar_hotel(h5)
