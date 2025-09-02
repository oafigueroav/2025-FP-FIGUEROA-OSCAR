import random

# Datos base
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 2

# Crear matriz 3D: ciudades x semanas x días
# Cada temperatura será un número aleatorio entre 15 y 35 grados
temperaturas = [
    [  # Para cada ciudad
        [random.uniform(15, 35) for _ in dias_semana]  # Para cada día de la semana
        for _ in range(num_semanas)  # Para cada semana
    ]
    for _ in ciudades
]

# Mostrar resultados
print("📊 Promedio de temperaturas por ciudad y semana:\n")

for i, ciudad in enumerate(ciudades):
    print(f"🌆 Ciudad: {ciudad}")
    for semana in range(num_semanas):
        suma = sum(temperaturas[i][semana])
        promedio = suma / len(dias_semana)
        print(f"  📅 Semana {semana + 1}: {promedio:.2f}°C")
    print()
