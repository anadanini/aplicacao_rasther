import requests

def requisitarSistemaSistema():
    requisicao = requests.api.get("http://service.tecnomotor.com.br/iRasther/sistema?pm.platform=1&pm.version=23&pm.type=LEVES&pm.assemblers=29&pm.vehicles=1057&pm.engines=22&pm.typeOfSystems=2")
    sistemaSistema = requisicao.json()
    return sistemaSistema

print(requisitarSistemaSistema())