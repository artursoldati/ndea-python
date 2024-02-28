import re

def verificador(cep):
    # Função que verifica a validade do CEP
    cep_str = str(cep)

    if not (100000 <= cep <= 999999):
        print("\nCEP inválido. Tente novamente.")
        return

    # Utiliza regex para verificar se o CEP possui dígitos consecutivos iguais
    if re.search(r'(\d)(\d)\1', cep_str):
        print("\nCEP inválido. Tente novamente.")
    else:
        print("\nCEP validado!")

on = True

while on:
    # Solicita o usuário para inserir um CEP válido
    c = int(input("\nDigite o CEP a ser validado: "))

    verificador(c)

    # Pergunta ao usuário se quer inserir outro CEP
    nov = input("\nDeseja validar outro CEP? [s/n]").lower()
    if nov == "n":
        on = False
        print("______________________")
        print("Obrigado volte sempre!")