import robohat3 as rh
import sys
import tty
import termios

def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return chr(0x10 + ord(c3) - 65)  # 16=Up, 17=Down, 18=Right, 19=Left arrows

rh.init()
v = 50

try:
  while True:
    k = readkey()
    
    if ord(k) == 3:
      print("Bye.")
      break
    elif k == 'w':
      rh.forward(v)
    elif k == 's':
      rh.reverse(v)
    elif k == 'a':
      rh.spinLeft(v)
    elif k == 'd':
      rh.spinRight(v)
    else:
      rh.stop()
    
finally:
  rh.cleanup()
