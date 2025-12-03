
class Campus:
    def __init__(self, nome, localizacao):
        self.nome = nome
        self.localizacao = localizacao
        self.cursos = []
lista_campus_ufc = []


def novo_campus():
    print("====Criar novo campus====")
    nome = input("Insira o nome do Campus:\n ")
    localizacao = input("Insira a localização:\n ") 
    for campus_existente in lista_campus_ufc:
        if campus_existente.nome.lower() == nome.lower():
            print(f"O Campus '{nome}' já existe. Tente outro nome.")
            return 
    novo_campus = Campus(nome, localizacao)
    lista_campus_ufc.append(novo_campus)
    print(f"Campus {nome} criado com sucesso!\n")


def listar_campus():
    if not lista_campus_ufc:
        print("Nenhum Campus cadastrado no sistema.")
        return None

    print("\nCampus disponíveis:")
    contador = 1
    for campus in lista_campus_ufc:
        print(f"[{contador}] Nome: {campus.nome}, Local: {campus.localizacao}")
        contador = contador + 1 
        
    while True:
        entrada_usuario = input("Escolha o NÚMERO do Campus (ou 0 para cancelar):\n ")
        
        if entrada_usuario == '0':
            print("Seleção cancelada.")
            return None

        if entrada_usuario.isdigit():
            numero_campus = int(entrada_usuario)
            
            if 1 <= numero_campus <= len(lista_campus_ufc):
                indice_campus = numero_campus - 1
                return lista_campus_ufc[indice_campus]
            else:
                print("Opção inválida, o número não está na lista.")
        else:
            print("Por favor, digite apenas um número.")


def excluir_campus():
    print("\n====Excluir Campus====")
    if len(lista_campus_ufc) == 0:
        print("Ainda não há Campi cadastrados para excluir.")
        return
    print("\n--- Campi disponíveis para exclusão ---")
    contador_campus = 1
    for campus in lista_campus_ufc:
        print(f"[{contador_campus}] Nome: {campus.nome}, Local: {campus.localizacao}")
        contador_campus = contador_campus + 1
    while True:
        entrada_campus = input("\nDigite o NÚMERO do Campus que você quer EXCLUIR (ou 0 para cancelar):\n ")
        if entrada_campus == '0':
            print("Exclusão de Campus cancelada.")
            return

        if entrada_campus.isdigit():
            numero_campus = int(entrada_campus)
    
            if 1 <= numero_campus <= len(lista_campus_ufc):
                
                indice_campus = numero_campus - 1
                campus_excluido = lista_campus_ufc[indice_campus]
                lista_campus_ufc.pop(indice_campus) 
                
                print("\n---")
                print(f" Campus '{campus_excluido.nome}' e todos os seus cursos EXCLUÍDOS com sucesso.")
                print("---")
                return 
                
            else:
                print(" Opção inválida, o número não está na lista.")
        else:
            print("Por favor, digite apenas um número.")
