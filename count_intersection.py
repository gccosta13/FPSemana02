frase_1=input('').split()
frase_2=input('').split()

set_1=set()
set_2=set()
set_3=set()

for frase in frase_1:
    set_1.add(frase)

for frase in frase_2:
    set_2.add(frase)

for frase in set_1:
    if frase in set_2:
        set_3.add(frase)

texto=""
for comum in set_3:
    texto+=f'{comum} '

print(texto.strip())