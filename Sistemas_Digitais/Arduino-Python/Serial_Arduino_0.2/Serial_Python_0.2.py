#Criação: Rejane Nobre Bezerra

#Aplicação:
#Programa capaz de controlar um led e registrar se ele está acesso ou apagado.

#Nota de uso:
# - O primeiro arquivo a ser executado é o do Arduino
#(ou seja: deve haver um programa no Arduino capaz
# de interagir com o programa Python
# Extra: a IDE do Arduino PODE estar aberta, não TEM que estar.)
#
# - Certifique-se de que não haja outro programa já
# se comunicando com o Arduino, como a janela da IDE do Arduino.
#(Perceba que se houver um programa se comunicando com a porta
# que o Arduino está conectado, não se extabelecerá uma coneção)
#
# - Execute o programa em Python.

#Como funciona?
#Entrada:
#O programa utiliza o caracter "1" como interrupitor.
#O programa utiliza o caracter "0" para encerra a coneção com a placa.
#Saída:
#O LED pode assumir os estados 1 (on) ou 0 (off).

import serial

ser = serial.Serial('COM3', baudrate = 9600, timeout = 1)

button = "1"

while (button != "0"):
        button = input("Digite 1 (um) para mudar o estado do LED e 0 (zero) para encerrar a coneção: ")
        if(button == "1"):
                ser.write(b'1')
                data = ser.readline().decode('ascii')
                print("LED: ",data)
           
ser.close()
print("Coneção encerrada.")
