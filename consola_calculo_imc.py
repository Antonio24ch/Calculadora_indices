# -*- coding: utf-8 -*-

import calculadora_indices as cal

peso = float(input('Ingrese el peso de la persona (en kg): '))
altura = float(input('Ingrese la altura de la persona (en m): '))


IMC = round(cal.calcular_IMC(peso,altura),2)
print('El IMC de la persona es de:',IMC)

if IMC <16:
  print('La persona tiene delgadez severa')
elif IMC>= 16 and IMC<=16.99:
  print('La persona tiene delgadez moderada')
elif IMC >=17 and IMC<=18.49:
  print('La persona tiene delgadez aceptable')
elif IMC >=18.5 and IMC<=24.99:
  print('La persona tiene peso normal')
elif IMC >=25 and  IMC<=29.99:
  print('La persona tiene sobrepeso')
elif IMC >=30 and IMC<=34.99:
  print('La persona tiene obesidad tipo I')
elif IMC >=35 and IMC<=39.99:
  print('La persona tiene obesidad tipo II')
elif IMC >=40 and IMC<=49.99:
  print('La persona tiene obesidad tipo III o mórbida')
else:
  print('La persona tiene obesidad tipo IV o extrema')