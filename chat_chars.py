frase=input().split()
contagem={}

for char in frase:
    if char.isalpha():  
        if char not in contagem:
            contagem[char] = 1
        else:
            contagem[char] += 1

resultado = {char: contagem[char] for char in frase if char.isalpha()}

print(resultado)