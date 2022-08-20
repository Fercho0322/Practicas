import json

class Json(): 

    json_file=()

    def read(self):
        with open("datos.json") as file:
            self.json_file = json.load(file)
        print(self.json_file)

    def write(self):

        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        telefono = input("Telefono: ")

        persona = {
            "nombre" : nombre,
            "apellido" :apellido,
            "telefono" :telefono
        }
        self.json_file["persona"].append(persona)
        with open("datos.json", "w") as file:
            json.dump(self.json_file, file)

objeto = Json()
objeto.read()
objeto.write()
print(objeto.json_file)
