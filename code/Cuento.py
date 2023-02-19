class Autor:
    def __init__(self, nombre, genero, fecha_nacimiento, fecha_deceso=None):
        self.nombre = nombre
        self.genero = genero
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_deceso = fecha_deceso
        
    def __repr__(self):
        if self.fecha_deceso is None:
            return f"{self.nombre}: {self.genero}, nacido/a en {self.fecha_nacimiento}"
        else:
            return f"{self.nombre}: {self.genero}, nacido/a en {self.fecha_nacimiento}, fallecido/a en {self.fecha_deceso}"

class Cuento:   
    def __init__(self, autor, genero, anio):
        self.autor = autor
        self.genero = genero
        self.anio = anio
        
    def __repr__(self):
        return f"{self.autor}: {self.genero}, {self.anio}"
    
    def get_autor(self):
        return self.autor
    
    def set_autor(self, autor):
        self.autor = autor
    
    def get_genero(self):
        return self.genero
    
    def set_genero(self, genero):
        self.genero = genero
    
    def get_anio(self):
        return self.anio
    
    def set_anio(self, anio):
        self.anio = anio
    
    def es_autor_rafael_pombo(self):
        return self.autor == "Rafael Pombo"
    
    def es_anio_2000_o_anterior(self):
        return self.anio <= 2000
    
    def autor_esta_vivo(self):
        return self.autor.fecha_deceso is None and self.fecha_nacimiento is not None

    def autor_es_femenino(self):
        return self.autor.genero == "Femenino"

cuentos = []

for i in range(5):
    print("cuento ", str(i+1), ":")
    autor = Autor(input("Ingrese el nombre del autor:\n"),input("Ingrese el género del autor\n"),input("Ingrese la fecha de nacimiento del autor\n"),input("Ingrese la fecha de deceso del autor\n"))
    genero = input("Ingrese el género del cuento: \n")
    anio = int(input("Ingrese el año del cuento: \n"))
    cuento = Cuento(autor, genero, anio)
    cuentos.append(cuento)

print("Todos los cuentos:\n")
for cuento in cuentos:
    print(cuento)
    
print("\nCuentos de Rafael Pombo:\n")
for cuento in cuentos:
    if cuento.es_autor_rafael_pombo():
        print(cuento)
        
print("\nCuentos del año 2000 hacia atrás:\n")
for cuento in cuentos:
    if cuento.es_anio_2000_o_anterior():
        print(cuento)

print("\nAutores femeninos:\n")
for cuento in cuentos:
    if cuento.autor_es_femenino():
        print(autor)
         
print("\nAutores vivos:\n")
for cuento in cuentos:
    if cuento.autor_esta_vivo():
        print(autor)
