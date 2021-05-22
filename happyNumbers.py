# Los números felices se definen como todos aquellos números, positivos, cuya suma de los cuadrados de sus dígitos (se repite el proceso cuantas veces sea necesario) de como resultado 1.

# Por ejemplo, 82 es un número feliz ya que:

# 8^2+2^2=68

# 6^2+8^2=100

# 1^2+0^2+0^2=1

# El procesos es algo laborioso, 😴es por ello que en esta ocasión será necesario construyas un script el cual nos permita conocer si un número es feliz o no. Los requerimientos son los siguientes.

# Define una función llamada happy_number.
# La función debe poseer un parámetro llamado number.
# La función debe recibir como argumento (De forma obligatoria) un número entero.
# La función debe retornar verdadero o falso si el parámetro es, o no, un número feliz.

# Ejemplo.

# >>> happy_number(7)
# True

# >>> happy_number(19)
# True

# >>> happy_number(5)
# False
# Ayuda:

# Número Feliz Wikipedia.
# Aquí un vídeo que me gusto mucho.
# Puedes apoyarte de las listas para facilitar tu labor.
# Una forma muy sencilla de solucionar el problema es apoyarnos de la programación funcional.
# Es importante no caer en un ciclo infinito.
# Pista: Recuerda, los números, al igual que las personas, pueden ser felices o infelices.

def happy_number(num) :
    num = str(num)
    confirm = []
    counter = 0
    happyNums = 0
    while True :
      for counter in range(len(num)) :
       aux = int(num[counter])
       happyNums += aux**2
       print( counter, happyNums, num )
      counter = 0       
      if happyNums in confirm :
          print('bucle')
          print('No es un numero happy')
          return False
      elif happyNums == 1 :
          print('Es un numero happy')
          return True
      confirm.append(happyNums)
      num = str(happyNums)  
      happyNums = 0
      print('happynums : ',happyNums)
      
if __name__ == "__main__":
    num = input('Es esto un happyNumber : ')

    if num.isdigit() :
        happy_number(num)
    else : 
        print('no es un numero entero')

    