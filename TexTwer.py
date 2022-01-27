import os

file = open("C:/Users/CENTIC/Escritorio/BrokerJSW/hola.txt", "w")
file.write("Hola" + os.linesep)
file.write("Estoy enviando un mensaje")
file.close()