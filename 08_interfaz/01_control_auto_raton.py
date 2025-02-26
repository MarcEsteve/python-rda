import pyautogui #pip install pyautogui

pyautogui.size() # Devuelve el tamaño de la pantalla

# Posición actual del ratón
pyautogui.position()

#Mover a un píxel concreto
pyautogui.moveTo(100, 100)

#Mover a un píxel concreto en un tiempo determinado
pyautogui.moveTo(100, 100, duration=1)

#Mover a un píxel concreto en un tiempo determinado con un efecto de aceleración
pyautogui.moveTo(100, 100, duration=1, tween=pyautogui.easeInOutQuad)

#Mover de manera relativa a la posición actual
pyautogui.moveRel(100, 100)

#Mover de manera relativa a la posición actual en un tiempo determinado
pyautogui.moveRel(100, 100, duration=1) # x_offser / y_offset

#Hacer clic en posición concreta
pyautogui.click(100, 100)

#Hacer doble clic en posición concreta
pyautogui.doubleClick(100, 100)

#Mover ratón mientras se mantiene pulsado el botón izquierdo
pyautogui.dragRel(100, 100, duration=1) #dragTo también es válido
 