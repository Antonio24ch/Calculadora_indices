# -*- coding: utf-8 -*-

import calculadora_indices as cal

peso = float(input('Ingrese el peso de la persona (en kg): '))
altura = float(input('Ingrese la altura de la persona (en m): '))
edad = float(input('Ingrese la edad de la persona (en años) '))
valor_genero = float(input('Ingrese el valor 10.8 en caso de ser masculino y 0 en caso de ser femenino: '))

GC = round(cal.calcular_porcentaje_grasa(peso,altura,edad,valor_genero),2)

print('El %GC de la persona es de:',GC,'%')