import requests

def requisitarMontadora():
    requisicao = requests.api.get("http://service.tecnomotor.com.br/iRasther/montadora?pm.platform=1&pm.version=23&pm.type=LEVES")
    montadora = requisicao.json()
    return montadora
