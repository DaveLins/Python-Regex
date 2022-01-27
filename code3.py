import re

texto = "Curso de Python do CFB Cursos canal do Youtube"

res = re.split("\s", texto)

print(res)

for t in res:
    print(t)