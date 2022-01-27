import re

texto = "Curso de Python do CFB Cursos canal do Youtube"

res = re.sub("\s", ".", texto)

print(res)