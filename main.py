from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.text('Usuario'), sg.Input(key='Usuario')],
    [sg.text('Senha'), sg.Input(key='senha',password_char='*')],
    [sg.Checkbox('Salvar login?')],
    [sg.Button('Entrar')]
]

janela = sg.Window('Tela de login', layout)

def VerificacaoDeSenha(self, Usuario, Senha):
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Entrar':
            if valores['Usuario'] == 'boy' and valores['Senha'] == '123':
                print(f'Bem vindo {valores['Usuario']}')