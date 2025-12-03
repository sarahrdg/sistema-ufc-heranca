from campus import listar_campus
from cursos import listar_cursos_campus as selecionar_curso

class  Disciplinas:
    def __init__(self, nome_disciplina, codigo_disciplina, curso):  
        self.nome_disciplina = nome_disciplina
        self.codigo_disciplina = codigo_disciplina
        self.curso = curso

    def exibir_info_basica(self):
        print(f"Disciplina: {self.nome_disciplina}, Código: {self.codigo_disciplina}, Curso: {self.curso.nome}")

def adicionar_disciplina():
    print("\n==== Adicionar nova Disciplina ====")
    curso_selecionado = selecionar_curso()
    if curso_selecionado is None:
        return 
    novo_nome_disciplina = input("Insira o nome da disciplina:\n ")
    codigo_disciplina = input('Insira o código da Disciplina:\n')
    while True:
        tem_letra = False
        tem_numero = False
    
        if not codigo_disciplina: 
            print("Código inválido. O código não pode ser vazio.")
        else:
            for char in codigo_disciplina: 
                if char.isalpha():
                    tem_letra = True
                elif char.isdigit():
                    tem_numero = True
            
            if tem_letra and tem_numero: 
                break 
            else:
                print("Código inválido. Por favor, insira letras e números (ex: POO101).")
        
        
        codigo_disciplina = input('Insira o código da Disciplina:\n')
    

    for nome_disciplina in curso_selecionado.disciplinas_curso: 
        if nome_disciplina.nome_disciplina == novo_nome_disciplina: 
            print(f"A disciplina '{nome_disciplina.nome_disciplina}' já existe no curso '{curso_selecionado.nome}'.")
            return
    nome_disciplina = Disciplinas(novo_nome_disciplina, codigo_disciplina, curso_selecionado) 
    curso_selecionado.disciplinas_curso.append(nome_disciplina) 
    
    print(f"Disciplina {novo_nome_disciplina} adicionada com sucesso!")

def listar_disciplinas_curso(): 
    print("\n==== Lista de Disciplinas por Curso ====")
    curso_selecionado = selecionar_curso()
    if curso_selecionado is None:
        return 
    print(f"Disciplinas no Curso '{curso_selecionado.nome_curso}':")
    if not curso_selecionado.disciplinas_curso:
        print("Nenhuma disciplina cadastrada neste curso.")
    else:
        for nome_disciplina in curso_selecionado.disciplinas_curso:
            print(f"Disciplina: {nome_disciplina.nome_disciplina}, Código: {nome_disciplina.codigo_disciplina}")

#tá dando muito erro aqui ae excluir_disciplina  
def editar_disciplina():
    print("\n====Editar Disciplina====")
    curso_selecionado = selecionar_curso()
    if len(curso_selecionado.disciplinas_curso) == 0:
        print(f"O Curso {curso_selecionado.nome_curso} não tem disciplinas para editar.")
        return
    
    print(f"\n--- Disciplinas para editar no Curso: {curso_selecionado.nome_curso} ---")
    
    #mostra as disciplinas disponíveis
    contador_disciplina = 1
    for nome_disciplina in curso_selecionado.disciplinas_curso:
        print(f"[{contador_disciplina}] {nome_disciplina.nome_disciplina} | Código: {nome_disciplina.codigo_disciplina}")
        contador_disciplina = contador_disciplina + 1
        

    while True:
        entrada_disciplina_str = input("\nDigite o NÚMERO da Disciplina que você quer mudar (ou 0 para cancelar):\n ")
        
        if entrada_disciplina_str == '0': 
            return
        
        try:
            escolha = int(entrada_disciplina_str)
            
            if 1 <= escolha <= len(curso_selecionado.disciplinas_curso):
                
                break 
            else:
                print("Opção inválida. Por favor, digite um número da lista ou 0 para cancelar.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    disciplina_selecionada = curso_selecionado.disciplinas_curso[escolha - 1]
    novo_nome_disciplina = input(f"Insira o novo nome para a disciplina '{disciplina_selecionada.nome_disciplina}' (ou pressione Enter para manter o nome atual):\n ")
    if novo_nome_disciplina:
        disciplina_selecionada.nome_disciplina = novo_nome_disciplina

        novo_codigo_disciplina = input(f"Insira o novo código para a disciplina '{disciplina_selecionada.codigo_disciplina}' (ou pressione Enter para manter o código atual):\n ")
    if not novo_codigo_disciplina_temp: 
                print("Código inválido. O código não pode ser vazio.")
                
    else:
               
        for char in novo_codigo_disciplina_temp:
            if char.isalpha():
                tem_letra = True
            elif char.isdigit():
                tem_numero = True
                
                if tem_letra and tem_numero:
                   
                    disciplina_selecionada.codigo_disciplina = novo_codigo_disciplina_temp
                    break 
                else:
                    
                    print("Código inválido. Por favor, insira letras e números (ex: POO101).")
            
           
            novo_codigo_disciplina_temp = input(f"Insira o NOVO código para a disciplina '{disciplina_selecionada.nome_disciplina}' (alfanumérico): \n")
            

    print(f"Disciplina atualizada com sucesso para: Nome: {disciplina_selecionada.nome_disciplina}, Código: {disciplina_selecionada.codigo_disciplina}")

def excluir_disciplina():
    print("\n====Excluir Disciplina====")
    curso_selecionado = selecionar_curso()
    if len(curso_selecionado.disciplinas_curso) == 0:
        print(f"O Curso {curso_selecionado.nome_curso} não tem disciplinas para excluir.")
        return
    
    print(f"\n--- Disciplinas para excluir no Curso: {curso_selecionado.nome_curso} ---")
    
    contador_disciplina = 1
    for nome_disciplina in curso_selecionado.disciplinas_curso:
        print(f"[{contador_disciplina}] {nome_disciplina.nome_disciplina} | Código: {nome_disciplina.codigo_disciplina}")
        contador_disciplina = contador_disciplina + 1

    
    while True:
        entrada_disciplina_str = input("\nDigite o NÚMERO da Disciplina que você quer excluir (ou 0 para cancelar):\n ")
        
        if entrada_disciplina_str == '0': 
            return
        
        try:
            escolha = int(entrada_disciplina_str)
            
            if 1 <= escolha <= len(curso_selecionado.disciplinas_curso):
                break 
            else:
                print("Opção inválida. Por favor, digite um número da lista ou 0 para cancelar.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    
    indice_para_excluir = escolha - 1 
    disciplina_excluida = curso_selecionado.disciplinas_curso.pop(indice_para_excluir)
    
    print(f"Disciplina '{disciplina_excluida.nome_disciplina}' excluída com sucesso do curso '{curso_selecionado.nome_curso}'.")
   

        
#subclasses de Disciplinas
class disciplinasObrigatorias(Disciplinas):
    def __init__(self, nome_disciplina, codigo_disciplina, curso, creditos):
        #chama a superclasse (disciplinas)
        super().__init__(nome_disciplina, codigo_disciplina, curso)
        self.creditos = creditos
    def exibir_info_completa(self):
        self.exibir_info_basica()
        print(f"Tipo: Obrigatória")
        print(f"Créditos: {self.creditos}")

class disciplinasOptativas(Disciplinas):
    def __init__(self, nome_disciplina, codigo_disciplina, curso, carga_horaria):
        super().__init__(nome_disciplina, codigo_disciplina, curso)
        self.carga_horaria = carga_horaria

    def exibir_info(self):
        self.exibir_info_basica()
        print(f"Tipo: Optativa")
        print(f"Carga Horária: {self.carga_horaria} horas")


