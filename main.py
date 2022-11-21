import random

minusc = "abcdefghijklmnopqrstuvwxyz"
maiusc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "1234567890"
cedilha = "ç"

randomize = minusc + maiusc + numeros
tamanho = 7

password = "".join(random.sample(randomize, tamanho)) + cedilha

print("Recomendação de senha:", password)