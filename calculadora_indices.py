# -*- coding: utf-8 -*-
def calcular_IMC(peso,altura):
    
    retorno= peso / altura**2
    
    '''Calcula el índice de masa corporal de una persona 
  a partir de la ecuación definida anteriormente'''

    
    return retorno

  

def calcular_porcentaje_grasa(peso,altura,edad,valor_genero):
           
    IMC = peso / altura**2
    retorno= 1.2 * IMC + 0.23 * edad - 5.4  - valor_genero
        
               
    '''Calcula el porcentaje de grasa de una persona a partir de
    la ecuación definida anteriormente'''
        
    return retorno
    


def calcular_calorias_en_reposo(peso,altura,edad,valor_genero):

  retorno= (10*peso) + (6.25 * altura) - (5*edad) + valor_genero

  '''Calcula la cantidad de calorías que una persona quema estando en reposo
  (esto es, su tasa metabólica basal), a partir de la ecuación definida anteriormente'''

  return retorno



def calcular_calorias_en_actividad(peso,altura,edad,valor_genero, valor_actividad):

        TMB = (10*peso) + (6.25 * altura) - (5*edad) + valor_genero 

        retorno = TMB * valor_actividad
  
        '''Calcula la cantidad de calorías que una persona quema al realizar algún tipo 
        de actividad física(esto es, su tasa metabólica basal según su actividad física),
        a partir de la ecuación anterior definida anteriormente'''

        return retorno


def calculo_calorias_en_reposo(peso,altura,edad,valor_genero):

  '''Calcula la cantidad de calorías que una persona quema estando en reposo
  (esto es, su tasa metabólica basal), a partir de la ecuación definida anteriormente'''

  retorno = (10*peso) + (6.25 * altura) - (5*edad) + valor_genero

  return retorno

