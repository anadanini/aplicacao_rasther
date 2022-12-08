import requests

def requisitarveiculoMontadora():
    requisicao = requests.api.get("http://service.tecnomotor.com.br/iRasther/veiculo?pm.platform=1&pm.version=23&pm.type=LEVES&pm.assemblers=29")
    veiculoMontadora = requisicao.json()
    return veiculoMontadora

print(requisitarveiculoMontadora())
