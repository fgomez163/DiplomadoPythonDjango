criterio_1 = False
criterio_2 = True
criterio_3 = False
criterio_4 = True
criterio_5 = True

if (criterio_1 or (criterio_2 and criterio_3)):
    print('Se cumple la política')
elif criterio_2:
    if criterio_4 and criterio_5:
        print('Se cumple la política por criterio 2')
else: 
    print('Se incumple la política')