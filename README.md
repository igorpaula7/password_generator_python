# Password Generator. Made in Python.

This is an 8 character password generator. Made in Python.

## Source Code
```python
import random

minusc = "abcdefghijklmnopqrstuvwxyz"
maiusc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "1234567890"
cedilha = "ç"

randomize = minusc + maiusc + numeros
tamanho = 7

password = "".join(random.sample(randomize, tamanho)) + cedilha

print("Recomendação de senha:", password)
```

## Logic
This code randomize the lower case, upper case and numbers and prints seven characters. After this, adds the "ç".

## Examples
- ShZPRmDç
- A4crGOTç
- zIlYmb6ç
