# Oscar David López Mora
# Matriz, recursos y horas trabajadas de lunes a viernes
recursos = [
    ["Ana", 8, 9, 8, 8, 9],
    ["Carlos", 10, 9, 10, 9, 8],
    ["María", 7, 8, 7, 8, 7],
    ["Luis", 9, 9, 9, 9, 9]
]

# Función, calcular total y clasificación
def calcular_horas(recurso):
    nombre = recurso[0]
    horas = recurso[1:]
    total_horas = sum(horas)
    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"
    return nombre, total_horas, clasificacion
# Recorrer la matriz, imprimir resultados
for recurso in recursos:
    nombre, total, clasificacion = calcular_horas(recurso)
    print("Recurso:", nombre)
    print("Total de horas:", total)
    print("Clasificación:", clasificacion)
    print("-" * 30)
    
