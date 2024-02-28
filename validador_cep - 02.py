import re
import requests
def verificador(cep):
    # Função que verifica a validade do CEP
    cep_str = str(cep)

    if not (10000000 <= cep <= 99999999):
        print("\nCEP inválido. Tente novamente.")

    # Utiliza regex para verificar se o CEP possui dígitos consecutivos iguais
    if re.search(r'(\d)(\d)\1', cep_str):
        print("\nCEP inválido. Tente novamente.")

    else:
        # for i in range(9):
        print(f"\nO CEP {cep_str[0:5]}-{cep_str[5:]} é válido!")
        api(cep_str)


def api(cep):
    cp = str(cep)

    # Chama a API para coletar mais informações do CEP fornecido
    url = requests.get(f'https://viacep.com.br/ws/{cp}/json/')
    url = url.json()
    print(url)

on = True

while on:
        # Solicita o usuário para inserir um CEP válido
    c = int(input("\nDigite o CEP a ser validado: "))

    verificador(c)

    # Pergunta ao usuário se quer inserir outro CEP
    novo = input("\nDeseja validar outro CEP? [s/n]").lower()
    if novo == "n":
        on = False
        print("______________________")
        print("Obrigado volte sempre!")