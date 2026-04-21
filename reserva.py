class Reserva:
  def __init__(self, cliente, ciudad, hotel, plan, costototal, habitacion, noches=None, tiene_minibar=False, fecha_entrada=None, fecha_salida=None):
    self.cliente = cliente
    self.ciudad = ciudad
    self.hotel = hotel
    self.plan = plan
    self.costototal = costototal
    self.habitacion = habitacion
    self.noches = noches
    self.tiene_minibar = tiene_minibar
    self.fecha_entrada = fecha_entrada
    self.fecha_salida = fecha_salida

  def fechas_se_interceptan(self, fecha_entrada, fecha_salida):
    return not (fecha_salida <= self.fecha_entrada or fecha_entrada >= self.fecha_salida)

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
    if self.fecha_entrada and self.fecha_salida:
      print(f"Check-in : {self.fecha_entrada.strftime('%d/%m/%Y')}")
      print(f"Check-out: {self.fecha_salida.strftime('%d/%m/%Y')}")
    print(f"Minibar: {'Sí' if self.tiene_minibar else 'No'}")
    print(f"Total: {self.costototal:,}$")
