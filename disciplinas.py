from campus import listar_campus
from cursos import listar_cursos_campus as selecionar_curso

class  Disciplinas:
    def __init__(self, nome_disciplina, codigo_disciplina, curso):  
        self.nome_disciplina = nome_disciplina
        self.codigo_disciplina = codigo_disciplina
        self.curso = curso

def adicionar_disciplina():
    print("\n==== Adicionar nova Disciplina ====")
    curso_selecionado = selecionar_curso()
    if curso_selecionado is None:
        return 
    curso_selecionado.curso = curso
    nome_disciplina = input("Insira o nome da disciplina:\n ")
    codigo_disciplina = int(input('Insira o código da Disciplina:\n'))

    for nome_disciplina in curso_selecionado: 
        if curso.curso_selecionado == nome_disciplina: #vai dar algum problema aqui
            print(f"A disciplina '{nome_disciplina}' já existe no curso '{curso_selecionado.nome}'.")
            return
    nome_disciplina = Disciplinas(nome_disciplina) 
    curso_selecionado.cursos.append(nome_disciplina) 
    
    print(f"Disciplina {nome_disciplina} adicionada com sucesso!")

def listar_disciplinas_curso(): 
    print("\n==== Lista de Disciplinas por Curso ====")
    curso_selecionado = selecionar_curso()
    if curso_selecionado is None:
        return 
    print(f"Disciplinas no Curso '{curso_selecionado.nome}':")
    if not curso_selecionado.cursos:
        print("Nenhuma disciplina cadastrada neste curso.")
    else:
        for nome_disciplina in curso_selecionado.cursos:
            print(f"Disciplina: {nome_disciplina.nome_disciplina}, Código: {nome_disciplina.codigo_disciplina}")
    
def editar_disciplina():
    print("\n====Editar Disciplina====")
    curso_selecionado = selecionar_curso()
    if len(curso_selecionado.cursos) == 0:
        print(f"O Curso {curso_selecionado.nome} não tem disciplinas para editar.")
        return
    
    print(f"\n--- Disciplinas para editar no Curso: {curso_selecionado.nome} ---")
    
    #mostra as disciplinas disponíveis
    contador_disciplina = 1
    for nome_disciplina in curso_selecionado.cursos:
        print(f"[{contador_disciplina}] {nome_disciplina.nome_disciplina} | Código: {nome_disciplina.codigo_disciplina}")
        contador_disciplina = contador_disciplina + 1
        

    while True:
        entrada_disciplina = input("\nDigite o NÚMERO da Disciplina que você quer mudar (ou 0 para cancelar):\n ")
        
        if entrada_disciplina == '0':
            return
        
def excluir_disciplina():
    print("\n====Excluir Disciplina====")
    curso_selecionado = selecionar_curso()
    if len(curso_selecionado.cursos) == 0:
        print(f"O Curso {curso_selecionado.nome} não tem disciplinas para excluir.")
        return
    
    print(f"\n--- Disciplinas para excluir no Curso: {curso_selecionado.nome} ---")
    
    #mostra as disciplinas disponíveis
    contador_disciplina = 1
    for nome_disciplina in curso_selecionado.cursos:
        print(f"[{contador_disciplina}] {nome_disciplina.nome_disciplina} | Código: {nome_disciplina.codigo_disciplina}")
        contador_disciplina = contador_disciplina + 1
        

    while True:
        entrada_disciplina = input("\nDigite o NÚMERO da Disciplina que você quer excluir (ou 0 para cancelar):\n ")
        
        if entrada_disciplina == '0':
            return
        
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


