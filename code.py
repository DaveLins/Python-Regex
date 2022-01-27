import re

texto = "Curso de Python do CFB Cursos canal do Youtube"

pesq = input(": ")

res = re.findall(pesq, texto)

print(res)

qtde = len(res)

print("Qtde: " + str(qtde))

for t in res:
    print(t)