import json
# from google.colab import drive
# drive.mount('/content/drive')

dataB = 'usuario.json'

def cargar_base_datos():
    try:
        with open(dataB, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

def guardar_base_datos(base_datos):
    with open(dataB, 'w') as archivo:
        json.dump(base_datos, archivo, indent=2)

def registro_usuario(base_datos):
    nombre = input("Ingrese nombre de usuario: ")
    if nombre in base_datos:
        print("El usuario ya existe, elije otro nombre de usuario.")
        registro_usuario(base_datos)

    else:
        contraseña = input("Ingresar contraseña: ")
        base_datos[nombre] = contraseña
        print(f"Usuario '{nombre}' ha sido registrado.")
        respuesta = input("Desea agregar otro registro ?:")
        if respuesta == ("si"):
          registro_usuario(base_datos)

def mostrar_usuarios(base_datos):
  respuesta = input("Desea imprimir registro ? :")
  if respuesta == "si":
    print("\nUsuarios registrados:")
    for usuario, contraseña in base_datos.items():
        print(f"Usuario: {usuario}, Contraseña: {contraseña}")
        print("Gracias por registrarse")
  else:
    print("hasta luego")
    return {}


base_de_datos = cargar_base_datos()

registro_usuario(base_de_datos)

mostrar_usuarios(base_de_datos)

guardar_base_datos(base_de_datos)