import pyautogui #pip install pyautogui

pyautogui.size() # Devuelve el tamaño de la pantalla
pyautogui.position() # Posición actual del ratón en la pantalla donde escribir
#Insertar cadena de texto
pyautogui.click(100, 100) #antes especificar donde se quiere escribir
pyautogui.typewrite("Hola, esto es una prueba")

#Pulsar teclas de difícil acceso
pyautogui.click(100, 100) 
pyautogui.typewrite(["a", "b", "left", "left", "X", "Y"])

#Obtener todos los nombres de las teclas
pyautogui.KEYBOARD_KEYS

#Pulsar una tecla
pyautogui.press("enter")
pyautogui.press("f1")

#Pulsar combinaciones de teclas
pyautogui.click(100, 100) 
pyautogui.hotkey("ctrl", "c")
pyautogui.click(100, 100) 
pyautogui.hotkey("ctrl", "v")

pyautogui.click(100, 100) 
pyautogui.hotkey("ctrl", "s") #guardar

#Alternativa a pyautogui
import keyboard #pip install keyboard

pyautogui.click(100, 100) 
keyboard.release("ctrl") 
keyboard.write("Hola Mundo")

pyautogui.click(100, 100) 
keyboard.press_and_release("ctrl + s") #Combinación teclas  