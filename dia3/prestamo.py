ingreso_mensual = 4800000
historial_positivo = True
deuda_actual = 1200000

if historial_positivo and deuda_actual < ingreso_mensual * 0.3:
    print("Prestamo aprobado")
elif historial_positivo:
    print("Aprobado con monto reducido")
else:
    print("Prestamo rechazado")