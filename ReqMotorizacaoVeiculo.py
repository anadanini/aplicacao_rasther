import requests

def requisitarmotor():
    requisicao = requests.api.get("http://service.tecnomotor.com.br/iRasther/motorizacao?pm.platform=1&pm.version=23&pm.type=LEVES&pm.assemblers=29&pm.vehicles=1057")
    motor = requisicao.json()
    return motor

print(requisitamotor())