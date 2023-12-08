import random
class DataNascimento:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

class Aluno:
    def __init__(self, nome, cpf, matricula, data_nascimento, sexo, ativo=True):
        self.nome = nome
        self.cpf = cpf
        self.matricula = matricula
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.ativo = ativo

    def exibir_informacoes(self):
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("Matrícula:", self.matricula)
        print("Data de Nascimento:", f"{self.data_nascimento.dia}/{self.data_nascimento.mes}/{self.data_nascimento.ano}")
        print("Sexo:", self.sexo)
        print("Ativo:", "Sim" if self.ativo else "Não")

def verificar_data_nascimento(dia, mes, ano):
    dias_no_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        dias_no_mes[1] = 29

    return 1 <= mes <= 12 and 1 <= dia <= dias_no_mes[mes - 1]

def verificar_sexo(sexo):
    return sexo.upper() in ['M', 'F']

def gerar_matricula():
    return f"20{random.randint(10000, 99999)}"

def validar_cpf(cpf):
    cpf_numeros = [int(digit) for digit in cpf if digit.isdigit()]

    if len(cpf_numeros) != 11:
        return False

    soma_produtos = sum(a * b for a, b in zip(cpf_numeros[:9], range(10, 1, -1)))
    primeiro_dv = (soma_produtos * 10) % 11 % 10

    soma_produtos1 = sum(a * b for a, b in zip(cpf_numeros[:10], range(11, 1, -1)))
    segundo_dv = (soma_produtos1 * 10) % 11 % 10

    return primeiro_dv == cpf_numeros[9] and segundo_dv == cpf_numeros[10]

def verificar_cpf_unico(cpf, lista_alunos):
    cpf = ''.join(filter(str.isdigit, cpf))

    if not validar_cpf(cpf):
        print("CPF inválido.")
        return False

    if any(aluno.cpf == cpf for aluno in lista_alunos):
        print("CPF já cadastrado para outro aluno.")
        return False

    return True

def verificar_nome(nome):
    return isinstance(nome, str) and nome.strip() != "" and all(c.isalpha() or c.isspace() for c in nome)

def inserir_aluno(nome, cpf, data_nascimento, sexo, lista_alunos):
    if not verificar_nome(nome):
        print("Nome inválido. Deve ser uma string.")
        return

    if not verificar_data_nascimento(*data_nascimento):
        print("Data de nascimento inválida.")
        return
    
    if not verificar_sexo(sexo):
        print("Sexo inválido.")
        return

    if not verificar_cpf_unico(cpf, lista_alunos):
        return

    matricula = gerar_matricula()
    while any(aluno.matricula == matricula for aluno in lista_alunos):
        matricula = gerar_matricula()

    aluno = Aluno(nome, cpf, matricula, DataNascimento(*data_nascimento), sexo)
    lista_alunos.append(aluno)
    
    print(f"Aluno cadastrado com sucesso. Matrícula: {matricula}")

def remover_aluno(matricula, lista_alunos):
    aluno_encontrado = None

    for aluno in lista_alunos:
        if aluno.matricula == matricula:
            aluno_encontrado = aluno
            break

    if aluno_encontrado:
        lista_alunos.remove(aluno_encontrado)
        print(f"Aluno com matrícula {matricula} removido com sucesso.")
    else:
        print(f"Aluno com matrícula {matricula} não encontrado.")
        
def atualizar_informacoes_aluno(matricula, lista_alunos, novo_nome=None, novo_cpf=None, nova_data_nascimento=None, novo_sexo=None, novo_status_ativo=None):
    aluno_encontrado = None

    for aluno in lista_alunos:
        if aluno.matricula == matricula:
            aluno_encontrado = aluno
            break

    if aluno_encontrado:
        if novo_data_nascimento is not None and not verificar_data_nascimento(*nova_data_nascimento):
            print("Data de nascimento inválida.")
            return

        if novo_sexo is not None and not verificar_sexo(novo_sexo):
            print("Sexo inválido.")
            return

        if novo_cpf is not None and not verificar_cpf_unico(novo_cpf, lista_alunos):
            print("CPF já cadastrado para outro aluno.")
            return
        
        if novo_nome is not None and not verificar_nome(novo_nome):
            print("Nome inválido.")
            return

        # Atualiza as informações conforme fornecido
        if novo_nome is not None:
            aluno_encontrado.nome = novo_nome
        if novo_cpf is not None:
            aluno_encontrado.cpf = novo_cpf
        if nova_data_nascimento is not None:
            aluno_encontrado.data_nascimento = DataNascimento(*nova_data_nascimento)
        if novo_sexo is not None:
            aluno_encontrado.sexo = novo_sexo
        if novo_status_ativo is not None:
            aluno_encontrado.ativo = novo_status_ativo

        print(f"Informações do aluno com matrícula {matricula} atualizadas com sucesso.")
    else:
        print(f"Aluno com matrícula {matricula} não encontrado.")

def listar_alunos(lista_alunos):
    if not lista_alunos:
        print("Lista de alunos vazia.")
        return

    print("Lista de Alunos:")
    for aluno in lista_alunos:
        print("\nMatrícula:", aluno.matricula)
        print("Nome:", aluno.nome)
        print("CPF:", aluno.cpf)
        print("Data de Nascimento:", f"{aluno.data_nascimento.dia}/{aluno.data_nascimento.mes}/{aluno.data_nascimento.ano}")
        print("Sexo:", aluno.sexo)
        print("Ativo:", "Sim" if aluno.ativo else "Não")
        print("-" * 30)

def menu():
    lista_de_alunos = []

    while True:
        print("\n=== Menu ===")
        print("1. Inserir Aluno")
        print("2. Remover Aluno")
        print("3. Atualizar Informações do Aluno")
        print("4. Listar Alunos")
        print("5. Sair")

        escolha = input("Escolha a opção (1-5): ")

        if escolha == "1":
            nome = input("Digite o nome do aluno: ")
            cpf = input("Digite o CPF do aluno: ")
            dia = int(input("Digite o dia de nascimento: "))
            mes = int(input("Digite o mês de nascimento: "))
            ano = int(input("Digite o ano de nascimento: "))
            sexo = input("Digite o sexo do aluno (M/F): ").upper()

            data_nascimento = (dia, mes, ano)

            inserir_aluno(nome, cpf, data_nascimento, sexo, lista_de_alunos)

        elif escolha == "2":
            matricula = input("Digite a matrícula do aluno a ser removido: ")
            remover_aluno(matricula, lista_de_alunos)

        elif escolha == "3":
            matricula = input("Digite a matrícula do aluno a ser atualizado: ")
            novo_nome = input("Novo nome (pressione Enter para manter o mesmo): ")
            novo_cpf = input("Novo CPF (pressione Enter para manter o mesmo): ")
            novo_dia = int(input("Novo dia de nascimento (pressione Enter para manter o mesmo): ") or -1)
            novo_mes = int(input("Novo mês de nascimento (pressione Enter para manter o mesmo): ") or -1)
            novo_ano = int(input("Novo ano de nascimento (pressione Enter para manter o mesmo): ") or -1)
            novo_sexo = input("Novo sexo (pressione Enter para manter o mesmo): ").upper()
            novo_status_ativo = input("Novo status ativo (S/N) (pressione Enter para manter o mesmo): ")

            nova_data_nascimento = (novo_dia, novo_mes, novo_ano) if (novo_dia != -1 and novo_mes != -1 and novo_ano != -1) else None
            novo_status_ativo = True if novo_status_ativo.upper() == "S" else False if novo_status_ativo.upper() == "N" else None

            atualizar_informacoes_aluno(matricula, lista_de_alunos, novo_nome, novo_cpf, nova_data_nascimento, novo_sexo, novo_status_ativo)

        elif escolha == "4":
            listar_alunos(lista_de_alunos)

        elif escolha == "5":
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    menu()


