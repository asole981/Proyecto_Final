import os

def control(catalogo):
    if os.path.exists(f"{catalogo}.txt"):
        # si el archivo existe, se abre para modificarlo
        with open(f"{catalogo}.txt", 'r') as archivo:
            print(f"✅ El catálogo '{catalogo.upper()}' ya existe. Se abrirá para modificarlo.")
    else:
        # si no existe, se elige la opcion para crearlo
        print(f"❎ El catálogo '{catalogo.upper()}' no existe, elija la opcion para crearlo")
        
    return catalogo