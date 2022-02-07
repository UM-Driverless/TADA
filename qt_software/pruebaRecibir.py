import serial

import time
txt = ""
txt = ""

end_serial = serial.Serial(port='COM3', baudrate=9600, bytesize=8, parity='N', stopbits=1)
end_serial.reset_input_buffer()
print("antes")
while (1):
    if end_serial.in_waiting > 0 :
        while end_serial.in_waiting > 0 :
        
            #se lee la informacion y se guarda en una variable
            txt = txt + " " + end_serial.read().decode()
            print("leido")
            print(txt)

        txt2 = txt
        print("txt2:")
        print(txt2)
        print("print")
        txt = ""
        txt2 = ""
        end_serial.reset_input_buffer()
        time.sleep(1)
        
        