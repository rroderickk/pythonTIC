import uuid


class Client:

    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4()

    def to_dict(self):  #! <- Método para convertir un objeto en un diccionario
        return vars(self)

    @staticmethod       #! <- Método estático
    def schema():
        return ['name', 'company', 'email', 'position', 'uid']