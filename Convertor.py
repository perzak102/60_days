import PySimpleGUI as sg


label1 = sg.Text("Enter feet:")
input_box1 = sg.InputText(key="feets")

label2 = sg.Text("Enter inches:")
input_box2 = sg.InputText(tooltip="Enter todo", key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output")


window = sg.Window("Convertor",
                   layout=[[label1, input_box1],
                           [label2, input_box2],
                           [convert_button, output_label]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event, values)
    print(event)
    print(values)
    result = float(values["feets"]) / 3.2808 + float(values["inches"]) * 0.0254
    result_out = f"{result:.2f} m"
    window["output"].update(value=result_out)

window.close()