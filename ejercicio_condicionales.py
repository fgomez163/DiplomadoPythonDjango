lista_ingredientes_brownies = {
    'chocolate negro': 5000,
    'mantequilla': 800,
    'huevos': 1000,
    'azucar': 1200,
    'harina': 1000,
}

ingredientes_listos = ['chocolate negro', 'harina']

costo_total = 0
ahorro = 0

for key, value in lista_ingredientes_brownies.items():
    if key in ingredientes_listos:
        ahorro = ahorro + value
    else:
        costo_total = costo_total + value

print('Costo total ' , costo_total)
print('Ahorro total ' , ahorro)