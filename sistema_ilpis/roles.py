from rolepermissions.roles import AbstractUserRole


class Gerente(AbstractUserRole):
    available_permissions = {
        'cadastrar_usuario': True,
        'cadastrar_medicamentos': True,
        'cadastrar_responsaveis': True,
        'agendar_visitas': True,
    }


class Usuario(AbstractUserRole):
    available_permissions = {
        'cadastrar_usuario': False,
        'cadastrar_medicamentos': True,
        'cadastrar_responsaveis': True,
        'agendar_visitas': True,
    }
