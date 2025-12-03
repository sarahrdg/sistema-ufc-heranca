from campus import listar_campus 

class Curso:
    def __init__(self, nome_curso, vagas_total):  #método construtor
        self.nome_curso = nome_curso
        self.vagas_total = vagas_total
        self.vagas_ocupadas = 0 
        self.disciplinas_curso = []

def adicionar_curso():
    print("\n==== Adicionar novo Curso ====")
    campus_selecionado = listar_campus()
    if campus_selecionado is None:
        return 
    nome_curso = input("Insira o nome do Curso:\n ") 
    vagas_total = int(input("Insira o total de vagas:\n "))

    for curso in campus_selecionado.cursos: 
        if curso.nome_curso == nome_curso:
            print(f"O Curso '{nome_curso}' já existe no Campus '{campus_selecionado.nome}'.")
            return
    novo_curso = Curso(nome_curso, vagas_total) 
    campus_selecionado.cursos.append(novo_curso) 
    
    print(f"Curso {nome_curso} criado com sucesso!")


def listar_cursos_campus(): 
    print("\n==== Lista de Cursos por Campus ====")
    campus_selecionado = listar_campus()
    if campus_selecionado is None:
        return None
    print(f"Cursos no Campus '{campus_selecionado.nome}':")
    if not campus_selecionado.cursos:
        print("Nenhum curso cadastrado neste campus.")
        return None
    else:
        for curso in campus_selecionado.cursos:
            print(f"Curso: {curso.nome_curso}, Vagas Totais: {curso.vagas_total}, Vagas Ocupadas: {curso.vagas_ocupadas}")
        while True:
                try:
                    escolha = int(input("\nEscolha o NÚMERO do Curso (ou 0 para cancelar): "))
                
                    if escolha == 0:
                        return None 
                    
                    if 1 <= escolha <= len(campus_selecionado.cursos):
                
                        curso_selecionado_pelo_usuario = campus_selecionado.cursos[escolha - 1] 
                        return curso_selecionado_pelo_usuario
                    else:
                     print("Opção inválida. Por favor, digite um número da lista ou 0 para cancelar.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")    


def editar_curso():
    print("\n====Editar Curso====")
    campus_selecionado = listar_campus()
    if len(campus_selecionado.cursos) == 0:
        print(f"O Campus {campus_selecionado.nome} não tem cursos para editar.")
        return
    
    print(f"\n--- Cursos para editar no Campus: {campus_selecionado.nome} ---")
    
    #mostra os cursos disponíveis
    contador_curso = 1
    for curso in campus_selecionado.cursos:
        print(f"[{contador_curso}] {curso.nome_curso} | Vagas: {curso.vagas_total} / Ocupadas: {curso.vagas_ocupadas}")
        contador_curso = contador_curso + 1
        

    while True:
        entrada_curso = input("\nDigite o NÚMERO do Curso que você quer mudar (ou 0 para cancelar):\n ")
        
        if entrada_curso == '0':
            print("Edição de curso cancelada.")
            return

        if entrada_curso.isdigit():
            numero_curso = int(entrada_curso)
            
         
            if 1 <= numero_curso <= len(campus_selecionado.cursos):
                
                indice_curso = numero_curso - 1
                curso_a_editar = campus_selecionado.cursos[indice_curso]
                break 
            else:
                print("Opção inválida, o número não está na lista.")
        else:
            print(" Por favor, digite apenas um número.")

    print(f"\n--- Editando: {curso_a_editar.nome_curso} ---")
    print("Se quiser manter o valor, apenas pressione ENTER.")
    

    novo_nome = input(f"Novo nome (Atual: {curso_a_editar.nome_curso}): ")
    if novo_nome != "": 
        curso_a_editar.nome_curso = novo_nome
        
    while True:
        nova_vagas_str = input(f"Novas vagas totais (Atual: {curso_a_editar.vagas_total}): ")
        
        if nova_vagas_str == "": 
            break
            
        if nova_vagas_str.isdigit():
            nova_vagas = int(nova_vagas_str)

            if nova_vagas >= curso_a_editar.vagas_ocupadas:
                curso_a_editar.vagas_total = nova_vagas
                break
            else:
                print(f"As novas vagas não podem ser menores que as vagas ocupadas ({curso_a_editar.vagas_ocupadas}).")
        else:
            print("Digite apenas números.")

    print("\n---")
    print(f"Curso '{curso_a_editar.nome_curso}' editado com sucesso!")
    print(f"Novo status: Vagas Totais: {curso_a_editar.vagas_total}")
    print("---")


def excluir_curso():
    print("\n====Excluir Curso====")
    campus_selecionado = listar_campus()
    if campus_selecionado is None:
        return
    if len(campus_selecionado.cursos) == 0:
        print(f"O Campus {campus_selecionado.nome} não tem cursos para excluir.")
        return
    print(f"\n--- Cursos disponíveis no Campus: {campus_selecionado.nome} ---")
    contador_curso = 1
    for curso in campus_selecionado.cursos:
        print(f"[{contador_curso}] {curso.nome_curso} | Vagas: {curso.vagas_total}")
        contador_curso = contador_curso + 1
    while True:
        entrada_curso = input("\nDigite o NÚMERO do Curso que você quer EXCLUIR (ou 0 para cancelar):\n ")
        if entrada_curso == '0':
            print("Exclusão de curso cancelada.")
            return
        if entrada_curso.isdigit():
            numero_curso = int(entrada_curso)
            if 1 <= numero_curso <= len(campus_selecionado.cursos):
                indice_curso = numero_curso - 1
                curso_excluido = campus_selecionado.cursos[indice_curso]
                nome_curso = curso_excluido.nome_curso
                campus_selecionado.cursos.pop(indice_curso) 

                print("\n---")
                print(f"Curso '{nome_curso}' EXCLUÍDO com sucesso do Campus {campus_selecionado.nome}.")
                print("---")
                return
                
            else:
                print(" Opção inválida, o número não está na lista.")
        else:
            print(" Por favor, digite apenas um número.")
