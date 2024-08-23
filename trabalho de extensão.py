import json

# Inicializa os registros
voluntarios_ensino = []
voluntarios_materiais = []
idosos_necessitam_ensino = []
idosos_necessitam_materiais = []

def salvar_dados():
    with open('voluntarios_ensino.json', 'w') as f:
        json.dump(voluntarios_ensino, f, indent=4)
    with open('voluntarios_materiais.json', 'w') as f:
        json.dump(voluntarios_materiais, f, indent=4)
    with open('idosos_necessitam_ensino.json', 'w') as f:
        json.dump(idosos_necessitam_ensino, f, indent=4)
    with open('idosos_necessitam_materiais.json', 'w') as f:
        json.dump(idosos_necessitam_materiais, f, indent=4)

def carregar_dados():
    global voluntarios_ensino, voluntarios_materiais, idosos_necessitam_ensino, idosos_necessitam_materiais
    try:
        with open('voluntarios_ensino.json', 'r') as f:
            voluntarios_ensino = json.load(f)
    except FileNotFoundError:
        voluntarios_ensino = []
    
    try:
        with open('voluntarios_materiais.json', 'r') as f:
            voluntarios_materiais = json.load(f)
    except FileNotFoundError:
        voluntarios_materiais = []
    
    try:
        with open('idosos_necessitam_ensino.json', 'r') as f:
            idosos_necessitam_ensino = json.load(f)
    except FileNotFoundError:
        idosos_necessitam_ensino = []
    
    try:
        with open('idosos_necessitam_materiais.json', 'r') as f:
            idosos_necessitam_materiais = json.load(f)
    except FileNotFoundError:
        idosos_necessitam_materiais = []

def registrar_voluntario_ensino():
    nome = input("Nome do voluntário para ensino: ")
    telefone = input("Telefone: ")
    bairro = input("Bairro: ")
    
    voluntario = {
        "nome": nome,
        "telefone": telefone,
        "bairro": bairro
    }
    voluntarios_ensino.append(voluntario)
    salvar_dados()
    print("Voluntário para ensino registrado com sucesso!")

def registrar_voluntario_materiais():
    nome = input("Nome do voluntário para disponibilização de materiais: ")
    telefone = input("Telefone: ")
    bairro = input("Bairro: ")
    
    voluntario = {
        "nome": nome,
        "telefone": telefone,
        "bairro": bairro
    }
    voluntarios_materiais.append(voluntario)
    salvar_dados()
    print("Voluntário para disponibilização de materiais registrado com sucesso!")

def registrar_idoso_necessita_ensino():
    nome = input("Nome do idoso que precisa de treinamento: ")
    telefone = input("Telefone: ")
    bairro = input("Bairro: ")
    voluntario_ensino = input("Nome do voluntário que irá ensinar (se já houver um): ")
    
    idoso = {
        "nome": nome,
        "telefone": telefone,
        "bairro": bairro,
        "voluntario_ensino": voluntario_ensino
    }
    idosos_necessitam_ensino.append(idoso)
    salvar_dados()
    print("Idoso que precisa de treinamento registrado com sucesso!")

def registrar_idoso_necessita_materiais():
    nome = input("Nome do idoso que precisa de materiais: ")
    telefone = input("Telefone: ")
    bairro = input("Bairro: ")
    voluntario_ensino = input("Nome do voluntário que irá ensinar: ")
    
    idoso = {
        "nome": nome,
        "telefone": telefone,
        "bairro": bairro,
        "voluntario_ensino": voluntario_ensino
    }
    idosos_necessitam_materiais.append(idoso)
    salvar_dados()
    print("Idoso que precisa de materiais registrado com sucesso!")

def listar_voluntarios_ensino():
    if voluntarios_ensino:
        print("\nVoluntários para ensino registrados:")
        for v in voluntarios_ensino:
            print(f"Nome: {v['nome']}, Telefone: {v['telefone']}, Bairro: {v['bairro']}")
    else:
        print("Nenhum voluntário para ensino registrado.")

def listar_voluntarios_materiais():
    if voluntarios_materiais:
        print("\nVoluntários para disponibilização de materiais registrados:")
        for v in voluntarios_materiais:
            print(f"Nome: {v['nome']}, Telefone: {v['telefone']}, Bairro: {v['bairro']}")
    else:
        print("Nenhum voluntário para disponibilização de materiais registrado.")

def listar_idosos_necessitam_ensino():
    if idosos_necessitam_ensino:
        print("\nIdosos que precisam de treinamento registrados:")
        for i in idosos_necessitam_ensino:
            print(f"Nome: {i['nome']}, Telefone: {i['telefone']}, Bairro: {i['bairro']}, Voluntário de Ensino: {i['voluntario_ensino']}")
    else:
        print("Nenhum idoso que precisa de treinamento registrado.")

def listar_idosos_necessitam_materiais():
    if idosos_necessitam_materiais:
        print("\nIdosos que precisam de materiais registrados:")
        for i in idosos_necessitam_materiais:
            print(f"Nome: {i['nome']}, Telefone: {i['telefone']}, Bairro: {i['bairro']}, Voluntário de Ensino: {i['voluntario_ensino']}")
    else:
        print("Nenhum idoso que precisa de materiais registrado.")

def main():
    carregar_dados()
    
    while True:
        print("\nSistema de Registro de Voluntários e Idosos")
        print("1. Registrar Voluntário para Ensino")
        print("2. Registrar Voluntário para Disponibilização de Materiais")
        print("3. Registrar Idoso que Precisa de Treinamento")
        print("4. Registrar Idoso que Precisa de Materiais")
        print("5. Listar Voluntários para Ensino")
        print("6. Listar Voluntários para Disponibilização de Materiais")
        print("7. Listar Idosos que Precisam de Treinamento")
        print("8. Listar Idosos que Precisam de Materiais")
        print("9. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            registrar_voluntario_ensino()
        elif escolha == '2':
            registrar_voluntario_materiais()
        elif escolha == '3':
            registrar_idoso_necessita_ensino()
        elif escolha == '4':
            registrar_idoso_necessita_materiais()
        elif escolha == '5':
            listar_voluntarios_ensino()
        elif escolha == '6':
            listar_voluntarios_materiais()
        elif escolha == '7':
            listar_idosos_necessitam_ensino()
        elif escolha == '8':
            listar_idosos_necessitam_materiais()
        elif escolha == '9':
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
