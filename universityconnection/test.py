cursos = ['a', 'b']

c =[]
holitas = []


for i in range(len(cursos)):
    aa = [cursos[i],cursos[i]] 
    c.extend(aa)

print(c)

for i in range(len(cursos)):
    esquema = (cursos[i],c[i])
    holitas.append(esquema)

