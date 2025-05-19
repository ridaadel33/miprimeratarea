def tabla_de_multiplicar(numero):
  """Muestra la tabla de multiplicar del número dado."""
  print(f"Tabla de multiplicar del {numero}:")
  for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Ejemplo de uso
numero_tabla = int(input("Introduce un número para ver su tabla de multiplicar: "))
tabla_de_multiplicar(numero_tabla)