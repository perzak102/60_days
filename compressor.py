import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select file to compress:")
input1 = sg.Input()
chose_button1 = sg.FileBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
chose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text="green")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, chose_button1],
                           [label2, input2, chose_button2],
                           [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression completed!")

window.close()
