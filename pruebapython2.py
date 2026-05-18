from random import randint

print ( " (X_X) ***** BIENVENIDO AL JUEGO DE ADIVINANZAS ***** (O_O) " )

# INGRESOS DE DATOS 

X = int ( input ( " Ingrese límite inferior: " ))
Y = int ( input ( " Ingrese límite superior: " ))

# VALIDACIÓN DE RANGOS 

while X >= Y:
    print ( " ***ERROR***: El límite inferior debe ser menor. " )
    
    X = int ( input ( " Ingrese límite inferior: " ))
    Y = int ( input ( " Ingrese límite superior: " ))
    
# GENERAR N° PAR ALEATORIOS

numero = randint ( X, Y )    

if numero % 2 != 0:
    
    if numero + 1 <= Y:
        numero += 1
    
    else:
        numero -= 1
        

# +_+ JUEGO +_+

intentos = 3
ganador = False

for intento in range ( 1, intentos + 1 ):
    
    usuario = int ( input (f"/n Intento {intento}: " ))
    
    
    if usuario == numero:
        
        print ( f"/nFelicitaciones W_W  " )
        print ( f"Adivinastes el número en el intento {intento} " )
        
        
        ganador = True
        break
    
    
    else:
        
        if usuario < numero:
            print ( " El número es ( MAYOR ) " )
        else:
            print ( " El número es ( MENOR ) " )
             
        
        if intento == 2:
            
            print ( " /nPISTA EXTRA: " )
            
            distancia1 = abs (numero - usuario)
            
            print ( " Te faltó una distancia de: " , distancia1 )
            
            
# SI PIERDES T_T 


if ganador == False:
    
    print ( " /nPerdistes U_U " )
    print ( " El número correcto era: " , numero )
    
    
    print ( " /n ********** FIN DEL JUEGO ********** " )                   