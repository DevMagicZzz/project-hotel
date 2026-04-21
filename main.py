from datetime import datetime
from clientes import Cliente, clientes
from ciudad import ciudades
from reserva import Reserva

#funciones auxiliares

def preguntar_si_no(mensaje):
  while True:
    respuesta = input(mensaje).strip().lower()
    if respuesta == "s":
      return True
    elif respuesta == "n":
      return False
    else:
      print("Respuesta inválida. Ingrese 's' para sí o 'n' para no.")

#login y registro

def registrar_cliente():
  print("\n=== BIENVENIDO AL SISTEMA DE RESERVAS ===")

  while True:
    nombrecliente = input("Ingrese su nombre: ").strip()
    if not nombrecliente:
      print("El nombre no puede estar vacío.")
    elif not nombrecliente.replace(" ", "").isalpha():
      print("El nombre NO puede contener números.")
    else:
      break

  while True:
    dni = input("Ingrese su DNI: ").strip()
    if not dni:
      print("El DNI no puede estar vacío.")
    elif not dni.isdigit():
      print("El DNI NO puede contener letras.")
    elif len(dni) < 6:
      print("El DNI es muy corto.")
    elif len(dni) > 10:
      print("El DNI es inválido.")
    else:
      break

  for c in clientes:
    if c.dni == dni:
      if c.nombrecliente.lower() == nombrecliente.lower():
        print(f"\nCliente reconocido. ¡Bienvenido de nuevo, {c.nombrecliente}!")
        return c, True
      else:
        print("Ya existe un cliente con ese DNI pero diferente nombre.")
        return registrar_cliente()

  for c in clientes:
    if c.nombrecliente.lower() == nombrecliente.lower():
      print("Ya existe un cliente con ese nombre y otro DNI. Verifique sus datos.")
      return registrar_cliente()

  nuevo = Cliente(nombrecliente, dni)
  clientes.append(nuevo)
  print(f"\n¡Registro exitoso! Bienvenido, {nuevo.nombrecliente}.")
  return nuevo, False

#menu cliente existente

def menu_cliente(cliente):
  while True:
    print(f"Menú de opciones del cliente — {cliente.nombrecliente.upper()}")
    print("1. Ver mis reservas")
    print("2. Realizar una nueva reserva")
    print("3. Cerrar sesión")
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
      if not cliente.reservas:
        print("No tiene reservas registradas aún.")
      else:
        print(f" Historial de reservas de {cliente.nombrecliente} ---")
        for i, r in enumerate(cliente.reservas, start=1):
          print(f"Reserva #{i}")
          r.mostrar()

    elif opcion == "2":
      return True

    elif opcion == "3":
      print(f"Hasta luego, {cliente.nombrecliente}.")
      return False

    else:
      print("Opción inválida.")

#funciones de seleccion 

def seleccionar_ciudad():
  while True:
    print("\n--- CIUDADES DISPONIBLES ---")
    for i, ciudad in enumerate(ciudades, start=1):
      print(f"  {i}. {ciudad.nombreciudad}")
    opcion = input("Elige una ciudad: ").strip()
    if opcion.isdigit():
      opcion = int(opcion)
      if 1 <= opcion <= len(ciudades):
        return ciudades[opcion - 1]
      else:
        print("Número fuera de rango.")
    else:
      print("Opción inválida.")

def seleccionar_hotel(ciudad):
  while True:
    print(f"\n--- HOTELES EN {ciudad.nombreciudad} ---")
    for i, hotel in enumerate(ciudad.hoteles, start=1):
      print(f"  {i}. {hotel.nombrehotel} — {hotel.estrellas} estrellas | Capacidad: {hotel.capacidad} huéspedes")
    opcion = input("Elige un hotel: ").strip()
    if opcion.isdigit():
      opcion = int(opcion)
      if 1 <= opcion <= len(ciudad.hoteles):
        return ciudad.hoteles[opcion - 1]
      else:
        print("Número fuera de rango.")
    else:
      print("Opción inválida.")

def seleccionar_tipo_reserva():
  while True:
    print("--- TIPO DE RESERVA ---")
    print("1. Con plan (noches fijas + precio especial)")
    print("2. Reserva directa (elige habitación y noches)")
    opcion = input("Elige una opción: ").strip()
    if opcion == "1":
      return "plan"
    elif opcion == "2":
      return "directa"
    else:
      print("Opción inválida.")

def seleccionar_plan(hotel):
  if not hotel.planes:
    print("Este hotel no tiene planes disponibles.")
    return None
  while True:
    print(f"\n--- PLANES DISPONIBLES — {hotel.nombrehotel} ---")
    for i, plan in enumerate(hotel.planes, start=1):
      print(f"  {i}. [{plan.nombreplan}] {plan.habitacion.calidad} | Cap: {plan.habitacion.capacidad} personas | {plan.noches} noches | Total: ${plan.costo:,}")
    opcion = input("Elige un plan: ").strip()
    if opcion.isdigit():
      opcion = int(opcion)
      if 1 <= opcion <= len(hotel.planes):
        return hotel.planes[opcion - 1]
      else:
        print("Número fuera de rango.")
    else:
      print("Opción inválida.")

def seleccionar_habitacion(hotel):
  while True:
    print(f"--- HABITACIONES DISPONIBLES — {hotel.nombrehotel} ---")
    for i, hab in enumerate(hotel.habitaciones, start=1):
      print(f"  {i}. {hab.calidad} | Cap: {hab.capacidad} personas | ${hab.costonoche:,}/noche")
    opcion = input("Elige una habitación: ").strip()
    if opcion.isdigit():
      opcion = int(opcion)
      if 1 <= opcion <= len(hotel.habitaciones):
        return hotel.habitaciones[opcion - 1]
      else:
        print("Número fuera de rango.")
    else:
      print("Opción inválida.")

def seleccionar_fechas(cliente, hotel):
  while True:
    print("\n--- SELECCIÓN DE FECHAS ---")
    while True:
      fecha_entrada_str = input("Ingrese fecha de check-in (DD/MM/AAAA): ").strip()
      try:
        fecha_entrada = datetime.strptime(fecha_entrada_str, "%d/%m/%Y")
        if fecha_entrada < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
          print("La fecha de check-in no puede ser en el pasado.")
        else:
          break
      except ValueError:
        print("Formato inválido. Use DD/MM/AAAA.")
    while True:
      fecha_salida_str = input("Ingrese fecha de check-out (DD/MM/AAAA): ").strip()
      try:
        fecha_salida = datetime.strptime(fecha_salida_str, "%d/%m/%Y")
        if fecha_salida <= fecha_entrada:
          print("La fecha de check-out debe ser posterior al check-in.")
        else:
          break
      except ValueError:
        print("Formato inválido. Use DD/MM/AAAA.")
    noches = (fecha_salida - fecha_entrada).days
    conflicto = False
    for r in cliente.reservas:
      if r.hotel is hotel and r.fechas_se_interceptan(fecha_entrada, fecha_salida):
        print(f"Ya tiene una reserva en este hotel del "
              f"{r.fecha_entrada.strftime('%d/%m/%Y')} al {r.fecha_salida.strftime('%d/%m/%Y')}.")
        print("Las fechas se interceptan. Elija otras fechas.")
        conflicto = True
        break
    if not conflicto:
      return fecha_entrada, fecha_salida, noches

def preguntar_minibar(hotel):
  print(f"Minibar")
  print(f"Costo adicional: {hotel.minibar:,}$")
  while True:
    respuesta = preguntar_si_no("¿Desea agregar minibar a su reserva? (s/n): ")
    if respuesta:
      return True, hotel.minibar
    else:
      return False, 0

#reservas

def confirmar_reserva_plan(cliente, ciudad, hotel, plan, tiene_minibar, costo_mini, fecha_entrada, fecha_salida):
  costo_total = plan.costo + costo_mini
  reserva = Reserva(
    cliente, ciudad, hotel, plan,
    costototal=costo_total,
    habitacion=None,
    noches=plan.noches,
    tiene_minibar=tiene_minibar,
    fecha_entrada=fecha_entrada,
    fecha_salida=fecha_salida
  )
  print("Reserva confirmada:")
  print(f"  Cliente  : {cliente.nombrecliente} (DNI: {cliente.dni})")
  reserva.mostrar()
  cliente.reservas.append(reserva)
  return reserva

def confirmar_reserva_directa(cliente, ciudad, hotel, habitacion, noches, tiene_minibar, costo_mini, fecha_entrada, fecha_salida):
  costo_total = (habitacion.costonoche * noches) + costo_mini
  reserva = Reserva(
    cliente, ciudad, hotel,
    plan=None,
    costototal=costo_total,
    habitacion=habitacion,
    noches=noches,
    tiene_minibar=tiene_minibar,
    fecha_entrada=fecha_entrada,
    fecha_salida=fecha_salida
  )
  print("\n=== RESERVA CONFIRMADA ===")
  print(f"  Cliente  : {cliente.nombrecliente} (DNI: {cliente.dni})")
  reserva.mostrar()
  cliente.reservas.append(reserva)
  return reserva

#flujo reserva

def flujo_reserva(cliente):
  ciudad = seleccionar_ciudad()
  hotel = seleccionar_hotel(ciudad)
  tipo = seleccionar_tipo_reserva()

  if tipo == "plan":
    plan = seleccionar_plan(hotel)
    if plan is None:
      return
    fecha_entrada, fecha_salida, _ = seleccionar_fechas(cliente, hotel)
    tiene_minibar, costo_mini = preguntar_minibar(hotel)
    confirmar_reserva_plan(cliente, ciudad, hotel, plan, tiene_minibar, costo_mini, fecha_entrada, fecha_salida)

  elif tipo == "directa":
    habitacion = seleccionar_habitacion(hotel)
    fecha_entrada, fecha_salida, noches = seleccionar_fechas(cliente, hotel)
    tiene_minibar, costo_mini = preguntar_minibar(hotel)
    confirmar_reserva_directa(cliente, ciudad, hotel, habitacion, noches, tiene_minibar, costo_mini, fecha_entrada, fecha_salida)


def main():
  while True:
    cliente, ya_existia = registrar_cliente()

    while True:
      if ya_existia:
        hacer_reserva = menu_cliente(cliente)
        if not hacer_reserva:
          break

      ya_existia = True
      flujo_reserva(cliente)

      if not preguntar_si_no("\n¿Desea hacer otra reserva? (s/n): "):
        print(f"\n¡Hasta luego, {cliente.nombrecliente}! Gracias por usar el sistema.")
        break
    if not preguntar_si_no("\n¿Desea registrar o ingresar otro cliente? (s/n): "):
      print("\nCerrando el sistema. ¡Hasta pronto!")
      break
main()
