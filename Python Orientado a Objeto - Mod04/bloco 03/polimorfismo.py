class Argentina():
    def capital(self):
        print("Buenos Aires é a capital da argentina.")
    def linguaOficial(self):
        print("Lingua Oficial = Espanhol")

class Brasil():
    def capital(self):
        print("Brasília é a capital do Brasil.")

    def linguaOficial(self):
        print("Lingua Oficial = Português.")

obj_arg = Argentina()
obj_br = Brasil()
for pais in (obj_arg, obj_br):
    pais.capital()
    pais.linguaOficial()

