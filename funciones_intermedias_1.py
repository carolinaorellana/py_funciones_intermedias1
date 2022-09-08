
#1 Actualizar valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1][0]=15
print(x)

#Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes[0])

#En el directorio_deportes, cambia "Messi" por "Andrés".
# print (directorio_deportes['fútbol'][0]) --> este lo use para saber ubicarme
directorio_deportes['fútbol'][0]= 'Andrés'
print(directorio_deportes['fútbol'])

#Cambia el valor 20 en z a 30.
# print(z[0]['y']) --> este lo use para saber ubicarme
z[0]['y']=30
print(z)

print("///////////////////////////////////////////////////////////")
#Iterar a través de una lista de diccionarios 
# Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

"""
Opcion con cada llave-valor en sitinta linea

def iterateDictionar(listaAlumnos):
    for alumno in listaAlumnos:
        for key, val in alumno.items():
            print(f"{key} - {val}")
iterateDictionar(estudiantes)

"""
def iterateDictionar(listaAlumnos):
    for alumno in listaAlumnos:
        alumno1=[]
        for key, val in alumno.items():
            alumno1.append(f"{key} - {val}")
        # print(alumno1)
        print(f"{alumno1[0]}, {alumno1[1]}")

iterateDictionar(estudiantes)


print("///////////////////////////////////////////////////////////")
# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;

#3 Obtener valores de una lista de diccionarios
'''
Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:
Michael
John
Mark
KB
copy
Y iterateDictionary2('last_name', estudiantes) debería generar:
'''
def iterateDictionary2(llave, listaAlumnos):
    for alumno in listaAlumnos:
        print(alumno[llave])
            
iterateDictionary2('first_name',estudiantes)
iterateDictionary2('last_name',estudiantes)

print("///////////////////////////////////////////////////////////")
#4Iterar a través de un diccionarios con valores de lista 
# Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(algunDiccionario):
    for iterador in algunDiccionario: # aca no entiendo porque sólo accede al primer llave y no a la llave valor
        # print(iterador)
        print(str(len(algunDiccionario[iterador])) +" "+ iterador)
        for nombre in algunDiccionario[iterador]:
            print(nombre)
printInfo(dojo)
