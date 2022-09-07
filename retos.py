sis = int(input())
dia = int(input())

if sis < 70 and dia < 50:
    print('Hipotension Alerta Amarilla')
elif 70 <= sis < 110 and 50 <= dia < 70:
    print('Optima Alerta Verde')
elif 110 <= sis < 120 and 70 <= dia < 75:
    print('Normal Alerta Verde')
elif 120 <= sis < 130 and 75 <= dia < 80:
    print('Prehipertension Alerta Amarilla')
elif 130 <= sis < 150 and 80 <= dia < 90:
    print('Hipertension Grado 1 Alerta Naranja')
elif 150 <= sis < 170 and 90 <= dia < 100:
    print('Hipertension Grado 2 Alerta Roja')
elif sis >= 170 and dia >= 100:
    print('Hipertension Grado 3 Alerta Roja')
elif sis >= 130 and dia < 80:
    print('Hipertension Solo Sistolica Alerta Naranja')
else:
    print('No se puede determinar la categoria Alerta Gris')

med1 = int(input())
med2 = int(input())
tot_pac, pac_med1, pac_med2 = 0, 0, 0

while med1 > 0 and med2 > 0:
    sis = int(input())
    dia = int(input())

    if sis < 70 and dia < 50:
        pac_med2 += 1
        med2 -= 5
    elif 120 <= sis < 130 and 75 <= dia < 80:
        pac_med1 += 1
        med1 -= 10
    elif 130 <= sis < 150 and 80 <= dia < 90:
        pac_med1 += 1
        med1 -= 15
    elif 150 <= sis < 170 and 90 <= dia < 100:
        pac_med1 += 1
        med1 -= 25
    elif sis >= 170 and dia >= 100:
        pac_med1 += 1
        med1 -= 45
    elif sis >= 130 and dia < 80:
        pac_med1 += 1
        med1 -= 25
    tot_pac += 1
        
print(tot_pac)
if tot_pac > 0:
    print('{:} {:.2f}%'.format(pac_med1, pac_med1 / tot_pac * 100))
    print('{:} {:.2f}%'.format(pac_med2, pac_med2 / tot_pac * 100))
else:
    print('0 0.00%')
    print('0 0.00%')