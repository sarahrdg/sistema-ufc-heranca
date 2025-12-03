from campus import novo_campus
from campus import listar_campus
from campus import excluir_campus
from cursos import adicionar_curso
from cursos import listar_cursos_campus
from cursos import editar_curso
from cursos import excluir_curso
from disciplinas import listar_disciplinas_curso
from disciplinas import editar_disciplina
from disciplinas import excluir_disciplina
from disciplinas import adicionar_disciplina

def menu():
    while True:
        print("\n===Sistema UFC===")
        
        print("\n--- 1. Campus ---")
        print("1. Novo Campus")
        print("2. Listar Campus")
        print("3. Excluir Campus")
        
        print("\n--- 2. Cursos ---")
        print("4. Adicionar Curso")
        print("5. Listar Cursos por Campus")
        print("6. Editar Curso")
        print("7. Excluir Curso")
        
        print("\n--- 3. Disciplinas (Usando Herança) ---")
        print("8. Adicionar Disciplina")
        print("9. Listar Disciplinas por Curso")
        print("10. Editar Disciplina")
        print("11. Excluir Disciplina")
        
        print("\n0. Sair")

        opcao = input("Escolha uma opção:\n ")
        #campus
        if opcao == "1":
            novo_campus()
        elif opcao == "2":
            listar_campus()
        elif opcao == "3":
            excluir_campus()
        
        #cursos
        elif opcao == "4":
            adicionar_curso()
        elif opcao == "5":
            listar_cursos_campus()
        elif opcao == "6":
            editar_curso()
        elif opcao == "7":
            excluir_curso()
        
        # disciplinas
        elif opcao == "8":
            adicionar_disciplina()
        elif opcao == "9":
            listar_disciplinas_curso()
        elif opcao == "10":
            editar_disciplina()
        elif opcao == "11":
            excluir_disciplina()
        
        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
