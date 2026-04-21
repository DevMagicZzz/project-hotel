class Reserva:
  def __init__(self, cliente, ciudad, hotel, plan, costototal, habitacion, noches=None, tiene_minibar=False):
    self.cliente = cliente
    self.ciudad = ciudad
    self.hotel = hotel
    self.plan = plan
    self.costototal = costototal
    self.habitacion = habitacion
    self.noches = noches
    self.tiene_minibar = tiene_minibar

  def mostrar(self):
    print(f"Ciudad: {self.ciudad.nombreciudad}")
    print(f"Hotel: {self.hotel.nombrehotel} ({self.hotel.estrellas} estrellas)")
    if self.plan:
      print(f"Plan: {self.plan.nombreplan}")
      print(f"Habitacion: {self.plan.habitacion.calidad} | Capacidad: {self.plan.habitacion.capacidad} personas")
      print(f"  Noches : {self.plan.noches}")
    else:
      print(f"Habitacion: {self.habitacion.calidad} | Capacidad: {self.habitacion.capacidad} personas")
      print(f"Noches : {self.noches}")
    print(f"Minibar: {'Sí' if self.tiene_minibar else 'No'}")
    print(f"Total: {self.costototal:,}$")
