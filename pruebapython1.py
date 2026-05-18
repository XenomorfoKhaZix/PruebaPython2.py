
#DATOS A CONSIDERAR:

Medicamentos = 60000
Despacho_a_Domicilio = 8000

Edad = int ( input ( " Ingrese su edad "))
Tramo = input ( " Ingrese su tramo segun corresponda ( A, B, C, D ): " )

#DESCUENTOS DE LOS MEDICAMENTOS:

El_descuento_de_los_medicamentos_es = 0 

if Edad <= 30:
    
    if Tramo == "A" or Tramo == "B":
        El_descuento_de_los_medicamentos_es = 0.18
        
    elif Tramo == "C" or Tramo == "D":
        El_descuento_de_los_medicamentos_es = 0.12
        

elif Edad >= 31 and Edad <= 60:
    
    if Tramo == "A" or Tramo == "B":
       El_descuento_de_los_medicamentos_es = 0.12
       
    elif Tramo == "C" or Tramo == "D":
       El_descuento_de_los_medicamentos_es = 0.08
       

else: 
    El_descuento_de_los_medicamentos_es = 0 
    
    
#ANALISIS: DESCUENTOS DE MEDICAMENTOS*****

Valor_descuento_medicamentos = Medicamentos * El_descuento_de_los_medicamentos_es
   
Valor_final_medicamentos = Medicamentos - Valor_descuento_medicamentos


#ANALISIS: DESCUENTO DESPACHO*****

Descuento_de_despacho = 0


if Tramo == "A" or Tramo == "B":
    Descuento_de_despacho += 0.10
    
if Edad >= 55:
    Descuento_de_despacho += 0.05
    

#VALOR CALCULO DESPACHO:

Valor_descuento_despacho = Despacho_a_Domicilio * Descuento_de_despacho

Valor_final_de_despacho = Despacho_a_Domicilio - Valor_descuento_despacho


print ( " El valor de los MEDICAMENTOS es: ", int(Valor_final_medicamentos))

print ( " El valor del DESPACHO  es: ", int( Valor_final_de_despacho ))