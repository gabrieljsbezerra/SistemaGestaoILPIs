from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    avaible_permisions = {
        'cadastrar_beneficiarios': True,
        'cadastrar_medicamentos': True,
        'cadastrar_responsaveis' : True,
        'agendar_visitas' : True
    }

class Administrador(AbstractUserRole):
    avaible_permisions = {
        'cadastrar_beneficiarios': True,
        'cadastrar_medicamentos': True,
        'cadastrar_responsaveis' : True,
        'agendar_visitas' : True
    }