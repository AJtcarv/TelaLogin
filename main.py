from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Text('Usuario'), sg.Input(key='Usuario')],
    [sg.Text('Senha'), sg.Input(password_char='*',key='Senha' )],
    [sg.Checkbox('Salvar login?')],
    [sg.Button('Entrar')]
]

janela = sg.Window('Tela de login', layout)


while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['Usuario'] == 'boy' and valores['Senha'] == '123':
            print(f'Bem vindo {valores['Usuario']}')
        else:
            print('Senha ou Usuario incorretos! ')


