import os
os.system("cls")

import os
from archivo_2 import control

class CatalogoPelicula:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = f"{nombre}.txt"
        self.peliculas = []

    def agregar(self, pelicula):
        self.peliculas.append(pelicula)
        with open(self.ruta_archivo, 'a') as archivo:
            archivo.write(f"{pelicula}\n")

    def listar(self):
        with open(self.ruta_archivo, 'r') as archivo:
            peliculas = archivo.readlines()
            for pelicula in peliculas:
                print(pelicula.strip())

    def eliminar(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print(f"✅ El catálogo '{self.nombre}' ha sido eliminado correctamente.")
        else:
            print(f"❎ El catálogo '{self.nombre}' no existe.")

class Pelicula(CatalogoPelicula):
    def __init__(self, nombre, duracion, idioma_original, estreno):
        super().__init__(nombre)
        self.__duracion = duracion # Atributo privado
        self.idioma_original = idioma_original
        self.estreno = estreno

    def __str__(self):
        return f"{self.nombre} - {self.__duracion} - {self.idioma_original} - {self.estreno}"
    
def main():
    nombre_catalogo = input("Hola!👋 Espero te encuentres muy bien! Por favor, ingresa a continuación, el nombre del catálogo de películas \ncon el que necesites trabajar, según las siguientes opciones: \nACCION 🔫 \nANIMACION 🧸 \nCOMEDIA 🤣\nDRAMA 😭\nROMANTICA 💗 \nSUSPENSO 😨\nTERROR 😱\n")
    # Verificamos si el archivo ya existe
    if os.path.exists(f"{nombre_catalogo}.txt"):
        # Si existe, abrimos el archivo para modificarlo
        with open(f"{nombre_catalogo}.txt", 'r') as archivo:
            print(f"✅ El catálogo '{nombre_catalogo.upper()}' forma parte nuestra lista de catálogos. Ingresa al menu de opciones. ")
    else:
        # Si no existe, se crea un nuevo archivo
        with open(f"{nombre_catalogo}.txt", 'w') as archivo:
            print(f"✅ El catálogo '{nombre_catalogo.upper()}'se ha incorporado a la lista. Ingresa al menu de opciones")
    
    catalogo = CatalogoPelicula(nombre_catalogo)

    while True:        
        print("\n✨ Menú de opciones:")       
        print("1. Agregar Película")
        print("2. Listar Películas")
        print("3. Eliminar catálogo de películas")
        print("4. Cambiar de catálogo")
        print("5. Listar catálogos")
        print("0. Salir")
        opcion = input("✨ Seleccione una opción: ")

        if opcion == '1':
            nombre_catalogo = input(f"\n✨ Ingresa nuevamente '{nombre_catalogo.upper()}' para agregar los datos de la película en este catálogo: ")
            # Verificamos si el archivo ya existe
            control(nombre_catalogo.upper()) # traigo la funcion de control de errores del archivo_2
            nombre_pelicula = input("✨ Ingresa el nombre de la película: ")
            duracion = input("✨ Ingresa la duración de la película (en minutos): ")
            idioma_original = input("✨ Ingresa el idioma original de la película: ")
            estreno = input("✨ Ingresa el año en que se estrenó la película: ")
            pelicula = Pelicula(nombre_pelicula, duracion, idioma_original, estreno)
            catalogo.agregar(pelicula)
            print(f"✅ \nLa película '{nombre_pelicula}' fue agregada al catálogo {nombre_catalogo.upper()} correctamente.")

        elif opcion == '2':
            catalogo_pelic = input("✨ Ingresa el nombre del catálogo a listar: ")
            # Verificamos si el archivo ya existe
            if os.path.exists(f"{catalogo_pelic}.txt"):
                # Si existe, abrir el archivo para modificarlo
                with open(f"{catalogo_pelic}.txt", 'r') as archivo:
                    print(f"✅ El catálogo '{catalogo_pelic.upper()}' se abrirá para listar las peliculas.")
            else:
                print("❎ El catálogo no existe, elija la opción para crearlo")
                continue
            print("✨ Listado de películas: ")
            catalogo = CatalogoPelicula(catalogo_pelic)
            catalogo.listar()

        elif opcion == '3':
            elimin_catalogo = input("✨ Ingresa el nombre del catálogo a eliminar: ")
            catalogo = CatalogoPelicula(elimin_catalogo)
            try:
                catalogo.eliminar()
            except FileNotFoundError:
                print(f"❎ El catálogo '{elimin_catalogo}' no existe.")
            except Exception as e:
                print(f"❎ Error al eliminar el catálogo: {e}")

        elif opcion == '4':
            print("👇 En este momento dispones de los siguientes catálogos:")
            for archivo in os.listdir():
                if archivo.endswith('.txt'):
                    print(archivo[:-4]) # menos la terminacion .txt
            nombre_catalogo = input("Ingresa el nombre del catálogo a usar según las siguientes opciones: \nACCION 🔫 \nANIMACION 🧸 \nCOMEDIA 🤣\nDRAMA 😭\nROMANTICA 💗 \nSUSPENSO 😨\nTERROR 😱\n")
            # Verificamos si el archivo ya existe
            control(nombre_catalogo) # traigo la funcion de control de errores del archivo_2
            catalogo = CatalogoPelicula(nombre_catalogo)
            
        elif opcion == '5':
            print("✨ Listado de catálogos: ")
            for archivo in os.listdir():
                if archivo.endswith('.txt'):
                    print(archivo[:-4])
                    catalogo = CatalogoPelicula(archivo[:-4])  
                    print("✨ Listado de películas: ")
                    catalogo.listar()

        elif opcion == '0':
            print("Se ha realizado correctamente la edicion de los catálogos. Muchas gracias! 😊")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

main()

