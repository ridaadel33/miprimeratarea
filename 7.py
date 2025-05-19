def media(n1, n2):
  """Calcula la media de dos números."""
  return (n1 + n2) / 2

# Ejemplo de uso
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
promedio = media(num1, num2)
print(f"La media de {num1} y {num2} es: {promedio}")