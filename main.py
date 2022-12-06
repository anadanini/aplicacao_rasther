import PySimpleGUI as sg

import ReqCategoria
import ReqMontadora


def janela_categoria():
    sg.theme("DarkTeal6")
    layout = [
        [sg.Text("Categoria")],
        [sg.Listbox(ReqCategoria.requisitardados())],
        [sg.Button("Selecionar"),sg.Button("Cancelar")]

    ]
    return sg.Window('Tabela de aplicação Rasther', size=(500, 500), layout=layout, element_justification='c',finalize=True)


def janela_montadora():
    sg.theme("DarkTeal6")
    layout = [
        [sg.Text("Montadora")],
        [sg.Listbox(ReqMontadora.requisitarMontadora())],

    ]
    return sg.Window('Tabela de aplicação Rasther', size=(500, 500), layout=layout, element_justification='c', finalize=True)


janela1, janela2 = janela_categoria(), None

while True:
    window, evento, valores = sg.read_all_windows()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break
    if window == janela1 and evento == "Selecionar":
        janela2 == janela_montadora()
        janela1.hide
