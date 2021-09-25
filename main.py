import pyautogui
import serial

num = 0
CHARS = ('a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9')

# puerto = input("Puerto: ")
# serialArduino = serial.Serial(puerto,9600)

while True:
    # estadoAux = serialArduino.readline()
    # estado = int(estadoAux.decode('Ascii'))
    # estado = int(input("ola: "))
    estado = 2
    
    if estado == 1:
        pyautogui.press("space", interval=0.3)
        num = 0

    elif estado == 2:
        char = CHARS[num]
        pyautogui.press("backspace", interval=0.3)
        pyautogui.press(char, interval=0.3)
        num = num + 1
        if num == 36:
            num = 0
    
    elif estado == 3:
        pyautogui.press("backspace", interval=0.3)
        num = 0