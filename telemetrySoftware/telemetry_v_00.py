import serial

coord_serial = serial.Serial(port='COM4', baudrate=9600, bytesize=8, parity='N', stopbits=1)
#end_serial = serial.Serial(port='COM6', baudrate=9600, bytesize=8, parity='N', stopbits=1)
for i in [0,1,2,3]:

    print("Escribe un mensaje que siga el concepto 'Velocidad actual,velocidad maxima,estado del coche'")
    txt = (input() + "\n").encode()
    coord_serial.write(txt)
    print(txt.decode())