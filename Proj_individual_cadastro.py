# Função para adicionar candidatos
def adicionar(valores_candidatos):
    num_candidatos = int(input("Quantos candidatos deseja adicionar? "))
    for i in range(1, num_candidatos + 1):
        nome_candidato = input("Insira o nome do candidato {}: ".format(i))
        ba = int(input(f'Digite um valor para o candidato {nome_candidato} (E): '))
        bb = int(input(f'Digite um valor para o candidato {nome_candidato} (T): '))
        bc = int(input(f'Digite um valor para o candidato {nome_candidato} (P): '))
        bd = int(input(f'Digite um valor para o candidato {nome_candidato} (S): '))
        valor_candidato = "E{}_T{}_P{}_S{}".format(ba, bb, bc, bd)
        valores_candidatos[nome_candidato] = valor_candidato

# Função para imprimir os valores dos candidatos
def imprimir(valores_candidatos):
    print("Valores dos candidatos:")
    for nome, valor in valores_candidatos.items():
        print("{}: {}".format(nome, valor))

# Função para buscar candidatos por valor
def buscar(valores_candidatos):
        aa = int(input(f'Digite um valor para  (E) que voce deseja consultar: '))
        ba = int(input(f'Digite um valor para  (T) que voce deseja consultar '))
        cc = int(input(f'Digite um valor para  (P) que voce deseja consultar'))
        dd = int(input(f'Digite um valor para  (S) que voce deseja consultar'))
        valor_desejado = "E{}_T{}_P{}_S{}".format(aa, ba, cc, dd)
        candidatos_encontrados = []
        for nome, valor in valores_candidatos.items():
                if valor >= valor_desejado:
                 candidatos_encontrados.append(nome)
        if candidatos_encontrados:
             print("Candidatos com o valor {}: {}".format(valor_desejado, candidatos_encontrados))
        else:
                print("Nenhum candidato encontrado com o valor {}.".format(candidatos_encontrados))

# Número de candidatos

 
def inicio():
	print('para exibir os csndidatos : 1.')
	print('para buscar algum resultado : 2 .')
	print('para adicionar algum candidato : 3.')
	print('digite 5 para sair.')

valores_candidatos = {}
adicionar(valores_candidatos)
inicio()
choice = int(input('Qual escolha a opção que voce deseja:'))

# Adicionando candidatos
while choice != 5:
    if choice == 1 :
        imprimir(valores_candidatos)
        choice = int(input('Qual escolha a opção que voce deseja:'))
    elif choice == 2 :
        buscar(valores_candidatos)
        choice = int(input('Qual escolha a opção que voce deseja:'))
    elif choice == 3 :
        adicionar(valores_candidatos)
        choice = int(input('Qual escolha a opção que voce deseja:'))
    inicio()
    choice = int(input('Qual escolha a opção que voce deseja:'))