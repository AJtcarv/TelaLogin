from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.text('Usuario'), sg.Input(key='Usuario')],
    [sg.text('Senha'), sg.Input(key='senha',password_char='*')],
    [sg.Checkbox('Salvar login?')],
    [sg.Button('Entrar')]
]

janela = sg.Window('Tela de login', layout)

