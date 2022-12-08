import requests

def requisitarSistemaMotor():
    requisicao = requests.api.get("http://service.tecnomotor.com.br/iRasther/tiposistema?pm.platform=1&pm.version=23&pm.type=LEVES&pm.assemblers=29&pm.vehicles=1057&pm.engines=22")
    sistemaMotor = requisicao.json()
    return sistemaMotor

print(requisitarSistemaMotor())