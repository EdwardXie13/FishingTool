import PySimpleGUI as sg

sg.ChangeLookAndFeel('GreenTan')
 
layout = [
    [sg.Text('Here is some text.... and a place to enter text')],            
    [sg.Text('Use Food'), sg.Checkbox('My first checkbox!', default=True), sg.Text('Hotkey'), sg.InputCombo(('1', '2'), size=(10, 3))],        
    [sg.Ok()]      
]

window = sg.Window('GUI').Layout(layout)

button, values = window.Read()
#sg.Popup('')

#sg.Popup()
print('lol')
