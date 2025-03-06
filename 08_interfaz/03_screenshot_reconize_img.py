import pyautogui

# Screenshot
pyautogui.screenshot(r'C:/Users/artha/OneDrive/Escritorio/AKKODIS/python-rda/08_interfaz/captura.png')

# Pantallazo especificando region
pyautogui.screenshot(r'C:/Users/artha/OneDrive/Escritorio/AKKODIS/python-rda/08_interfaz/captura2.png', region=(0,0,300,400))

# Localiza una imagen en pantalla
pyautogui.locateOnScreen('galeria.png')


