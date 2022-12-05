import PySimpleGUIQt as sg

import ReqCategoria

#Tema da interface
sg.theme("DarkTeal6")


layout = [
    [sg.Text("Categoria")],
    [sg.Listbox(ReqCategoria.requisitardados())],
    [sg.Button("Selecionar"),sg.Button("Cancelar")]

]

janela = sg.Window('Tabela de aplicação Rasther', size=(400, 400), layout=layout, element_justification='c')

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break
janela.close()