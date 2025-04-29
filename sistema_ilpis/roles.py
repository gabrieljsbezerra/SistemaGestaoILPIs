from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    avaible_permisions = {
        'cadastrar_usuario': True,
        'cadastrar_medicamentos': True,
        'cadastrar_responsaveis' : True,
        'agendar_visitas' : True
    }

class Usuario(AbstractUserRole):
    avaible_permisions = {
        'cadastrar_medicamentos': True,
        'cadastrar_responsaveis' : True,
        'agendar_visitas' : True
    }