import requests

def requisitardados():
    requisicao = requests.api.get("http://service.tecnomotor.com.br/iRasther/tipo?pm.platform=1&pm.version=23")
    categoria = requisicao.json()
    return categoria