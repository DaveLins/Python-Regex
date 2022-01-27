import re

texto = "Curso de Python do CFB Cursos canal do Youtube"

res = re.search("Python", texto)

pi = res.start()

pf = res.end()

tam = pf-pi

print(res.start())

print(res.end())

print(tam)