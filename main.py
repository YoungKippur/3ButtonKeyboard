import pyautogui
import serial

num = 0
CHARS = ('space', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9','a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

puerto = input("Puerto: ")
serialArduino = serial.Serial(puerto,9600)

while True:
    estadoAux = serialArduino.readline()
    estado = int(estadoAux.decode('Ascii'))
    # estado = int(input("ola: "))
    
    if estado == 1:
        pyautogui.press("space", interval=0.3)
        num = 0

    elif estado == 2:
        char = CHARS.index(num)
        pyautogui.press("del", interval=0.3)
        pyautogui.press(char, interval=0.3)
        num = num + 1
    
    elif estado == 3:
        pyautogui.press("del", interval=0.3)
        num = 0
