# -*- coding: utf-8 -*-

import calculadora_indices as cal

peso = float(input('Ingrese el peso de la persona (en kg): '))
altura = float(input('Ingrese la altura de la persona (en cm): '))
edad = float(input('Ingrese la edad de la persona (en años) '))
valor_genero = float(input('Ingrese el valor 5 en caso de ser masculino y en caso de ser femenino -161: '))
valor_actividad = float(input('Ingrese el valor de la actividad física que realiza en la semana: 1.2(poco o ningún ejercicio), 1.375(1-3 días semana), 1.55(3-5 días a la semana), 1.725(6-7 días a la semana), 1.9 (entrenamiento mañana y tarde): '))

TMB_act_fis = round(cal.calcular_calorias_en_actividad(peso,altura,edad,valor_genero, valor_actividad),2)

print('La TMB_act_fis de la persona es de:',TMB_act_fis,'cal')