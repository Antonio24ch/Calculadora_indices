# -*- coding: utf-8 -*-

import calculadora_indices as cal

peso = float(input('Ingrese el peso de la persona (en kg): '))
altura = float(input('Ingrese la altura de la persona (en cm): '))
edad = float(input('Ingrese la edad de la persona (en años) '))
valor_genero = float(input('Ingrese el valor 5 en caso de ser masculino y en caso de ser femenino -161: '))

TMB = round(cal.calcular_calorias_en_reposo(peso, altura,edad,valor_genero),2)

print('Para adelgazar es recomendado que consumas entre:',round(TMB*0.80,2), 'y', round(TMB*0.85,2), 'cal')

