# funcoes2.py

def loginUsuario(perfil):
    # normaliza para minúsculas para evitar diferença entre 'Admin', 'ADMIN', etc.
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')


loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')
loginUsuario('ADMINISTRADOR')  # não é exatamente "admin", então cai no else


