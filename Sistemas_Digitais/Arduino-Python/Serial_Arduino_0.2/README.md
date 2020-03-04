Criação: Rejane Nobre Bezerra

Aplicação:
  Programa capaz de controlar um led e registrar se ele está acesso ou apagado.

Nota de uso:
 - O primeiro arquivo a ser executado é o do Arduino (ou seja: deve haver um programa no Arduino capaz de interagir com o programa Python. Extra: a IDE do Arduino PODE estar aberta, não TEM que estar.)
- Certifique-se de que não haja outro programa já se comunicando com o Arduino, como a janela da IDE do Arduino. (Perceba que se houver um programa se comunicando com a porta que o Arduino está conectado, não se extabelecerá uma coneção)
 - Execute o programa em Python.

Como funciona?
  - Entrada:
    O programa utiliza o caracter "1" como interrupitor.
    O programa utiliza o caracter "0" para encerra a coneção com a placa.
  - Saída:
    O LED pode assumir os estados 1 (on) ou 0 (off).
