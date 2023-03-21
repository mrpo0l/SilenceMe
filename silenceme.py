import keyboard
import pyautogui
import win32gui
import win32con

# Nombre de la ventana de Discord
discord_window_name = "Discord"

# variable booleana para indicar si la tecla "v" ya ha sido detectada
v_pressed = False

# función para enviar el atajo a Discord


def send_shortcut():
    # buscar la ventana de Discord
    discord_window = None
    windows = []

    def enum_callback(hwnd, results):
        if win32gui.IsWindowVisible(hwnd) and discord_window_name.lower() in win32gui.GetWindowText(hwnd).lower():
            results.append(hwnd)
        return True

    win32gui.EnumWindows(enum_callback, windows)

    if windows:
        # obtener el identificador de la ventana de Discord
        discord_window = windows[0]

    try:
        # cambiar el enfoque a la ventana de Discord
        win32gui.SetForegroundWindow(discord_window)

        # enviar el atajo a Discord
        pyautogui.hotkey('ctrl', 'shift', 'm')
    except Exception as e:
        print(
            f"Error al establecer la ventana de Discord como activa: {str(e)}")

# función para actualizar la variable booleana "v_pressed" y enviar el atajo a Discord


def set_v_false(event):
    global v_pressed
    if event.name == 'v':
        v_pressed = False
        send_shortcut()


# agregar un oyente para la tecla "v" cuando se suelta
keyboard.on_release(set_v_false)

# bucle para detectar la tecla "v" cuando se mantiene presionada
while True:
    # verificar si la tecla "v" está siendo presionada
    if keyboard.is_pressed('v'):
        # verificar si la tecla "v" ya ha sido detectada
        if not v_pressed:
            # marcar la tecla "v" como detectada y enviar el atajo a Discord
            v_pressed = True
            send_shortcut()
    else:
        # marcar la tecla "v" como no detectada cuando se suelta
        v_pressed = False
