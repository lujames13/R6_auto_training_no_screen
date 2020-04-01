import ctypes
import time
import pyautogui as gui

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
def HotPress(hexKeyCode):
    PressKey(hexKeyCode)
    time.sleep(0.05)
    ReleaseKey(hexKeyCode)
    time.sleep(0.05)

# hex code keyboard
enter = 0x1C
esc = 0x1
alt = 0x5D
f4 = 0x05
leftClick = 0x100
F = 0x21
W = 0x11
A = 0x1E
S = 0x1F
D = 0x20
right = 0xCD
down = 0xD0

# click menu and quit game in R6
def close_game():
    HotPress(esc)
    time.sleep(0.5)
    HotPress(esc)
    time.sleep(0.5)
    gui.click(1669, 964, duration=0.2)
    time.sleep(0.5)
    HotPress(enter)

    #     gui.click(1765, 119, duration=0.2)
    time.sleep(20)
    HotPress(esc)
    time.sleep(0.5)
    #     gui.click(1644, 301, duration=0.2)
    #     time.sleep(0.5)
    HotPress(down)
    time.sleep(0.5)
    #     gui.click(867, 990, duration=0.2)
    #     time.sleep(0.5)
    HotPress(enter)



x = float(input("Please input the auto training time(in hour), input grater then 999 will training no stop: "))
print("start auto training in 5 seconds.")
print("please turn the screen into R6.")
init_time = time.time()
time.sleep(5)
while(True):
    if (x < 999):
        if (time.time() - init_time) > 3600*x:
            print("{} hour time out!".format(x))
            time.sleep(200)
            close_game()
            break
    '''
        while in game labby, it will click the training mode and create a 1 person training game
        while in character choosing part, it will spam enter to quick skip this part
        while in rematch part, it will press esc to get out of the daily mission screen, and press enter to quick rematch
    '''
    gui.click(512,350, duration=0.2)
    HotPress(enter)
    time.sleep(3)
    gui.click(1612,719, duration=0.2)
    HotPress(enter)
    time.sleep(0.5)
    HotPress(esc)
    time.sleep(0.5)
    HotPress(enter)
    time.sleep(0.5)
    gui.click(1612,719, duration=0.2)
    HotPress(enter)
    time.sleep(0.5)
    gui.click(1612,719, duration=0.2)
    HotPress(enter)
    time.sleep(0.5)
    gui.click(1612,719, duration=0.2)
    HotPress(enter)
    time.sleep(0.5)
    gui.click(1612,719, duration=0.2)
    HotPress(enter)
    time.sleep(0.5)
    gui.click(1612,719, duration=0.2)
    HotPress(enter)
    time.sleep(0.5)
    gui.click(1612,719, duration=0.2)
    HotPress(enter)
    time.sleep(0.5)
    gui.click(1612,719, duration=0.2)
    HotPress(enter)
    time.sleep(0.5)
    gui.click(1612,719, duration=0.2)
    HotPress(enter)
    time.sleep(0.5)
    gui.click(1612,719, duration=0.2)
    HotPress(enter)
    time.sleep(0.5)
    gui.click(1612,719, duration=0.2)
    HotPress(enter)
    time.sleep(0.5)
    gui.click(1612,719, duration=0.2)
    HotPress(enter)
    time.sleep(0.5)
    gui.click(1612,719, duration=0.2)
    HotPress(enter)
    time.sleep(0.5)
    gui.click(1612,719, duration=0.2)
    HotPress(enter)
    time.sleep(5)
    gui.click(1040, 214, duration=0.2)

    gui.click(1013,955, duration=0.2)
