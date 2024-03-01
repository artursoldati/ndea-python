import re
import requests
from pymongo.mongo_client import MongoClient

#Criando conexão com o MongoDB
connection_string = "mongodb+srv://admin:database@cluster0.wwxowvk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(connection_string)
db = client["velidador_CEP"]
collection = db.get_collection("CEP")

def verificador(cep):
    # Função que verifica a validade do CEP
    cep_str = str(cep)

    if not (10000000 <= cep <= 99999999):
        print("\nCEP inválido. Tente novamente.")

    # Utiliza regex para verificar se o CEP possui dígitos consecutivos iguais
    if re.search(r'(\d)(\d)\1', cep_str):
        print("\nCEP inválido. Tente novamente.")
        return False

    else:
        # for i in range(9):
        print(f"\nO CEP {cep_str[0:5]}-{cep_str[5:]} é válido!")
        api(cep_str)
        return True

def api(cep):
    cp = str(cep)

    # Chama a API para coletar mais informações do CEP fornecido
    url = requests.get(f'https://viacep.com.br/ws/{cp}/json/')
    url = url.json()
    return url

on = True
#Formato de registro do Mongo
mongo = {"_id":{"$oid": "65de4f9472521a3ebabd1c2f"}}

while on:
    # Solicita o usuário para inserir um CEP válido
    c = int(input("\nDigite o CEP a ser validado: "))

    if verificador(c):
        a = api(c)
        #Coloca as informações do CEP junto com o registro de entrada do mongo
        mongo.update(a)
        print(a)
        #Transforma o imput em string para pesquisar no banco e retornará se já foi inserido ou não
        cp = str(c)
        find = cp[0:5]+"-"+cp[5:]
        cc = {"cep":find}
        repetido = collection.find_one(cc)
        if repetido:
            print("\nCEP já inserido!")
        else:
            print("\nCEP inserido com sucesso!")
            resultado = collection.insert_one(a)

    # Pergunta ao usuário se quer inserir outro CEP
    novo = input("\nDeseja validar outro CEP? [s/n]").lower()
    if novo == "n":
        on = False
        print("______________________")
        print("Obrigado volte sempre!")