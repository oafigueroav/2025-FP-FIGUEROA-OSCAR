import random

# Datos base
ciudad = "Guayaquil"
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 3

# Crear matriz 3D: semanas x días x temperatura
# Cada temperatura será un número aleatorio entre 25 y 35 grados (clima cálido típico de Guayaquil)
temperaturas_guayaquil = [
    [ [random.uniform(25, 35)] for _ in dias_semana ]  # Temperatura por día
    for _ in range(num_semanas)  # Por semana
]

# Mostrar resultados
print(f"🌆 Temperaturas diarias en {ciudad}:\n")

for semana in range(num_semanas):
    print(f"📅 Semana {semana + 1}:")
    for dia in range(len(dias_semana)):
        temp = temperaturas_guayaquil[semana][dia][0]
        print(f"  {dias_semana[dia]}: {temp:.2f}°C")
    print()

# Calcular promedio por semana
print(f"📊 Promedio semanal de temperaturas en {ciudad}:\n")
for semana in range(num_semanas):
    suma = sum([temperaturas_guayaquil[semana][dia][0] for dia in range(len(dias_semana))])
    promedio = suma / len(dias_semana)
    print(f"  Semana {semana + 1}: {promedio:.2f}°C")
