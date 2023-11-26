import PySimpleGUI as sg

label1 = sg.Text("Select file to compress:")
input1 = sg.Input()
chose_button1 = sg.FileBrowse("Choose")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
chose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, chose_button1],
                           [label2, input2, chose_button2],
                           [compress_button]])

window.read()
window.close()
