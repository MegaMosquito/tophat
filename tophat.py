#!/usr/bin/env python3
import os
import sys
import time
import unicornhathd

unicornhathd.rotation(0)
unicornhathd.brightness(0.5)
u_width, u_height = unicornhathd.get_shape()

def get_from_env(v, d):
  if v in os.environ and '' != os.environ[v]:
    return os.environ[v]
  else:
    return d
selector = get_from_env('SELECTOR', '').lower()
CHOICES = {
  'red'   : 1,
  'green' : 2,
  'blue'  : 3
}
if selector in CHOICES.keys():
  SELECTED = CHOICES[selector]
else:
  sys.stderr.write('ERROR: Envronment variable "SELECTOR" must contain one of: "red", "green", or "blue"! Found "' + selector + '".\n')
  sys.exit(1)

COLORS = [
  [ 0, 0, 255 ], # 0 -> the logo area at the top
  [ 255, 0, 0 ], # 1 -> the R selection (red)
  [ 0, 255, 0 ], # 2 -> the G selection (green)
  [ 0, 0, 255 ]  # 3 -> the B selection (blue)
]

MATRIX = [
  '.***.***..*...*.',
  '..*..*..*.**.**.',
  '..*..*..*.*****.',
  '..*..***..* *.*.',
  '..*..*..*.*.*.*.',
  '..*..*..*.*...*.',
  '.***.***..*...*.',
  '................',
  '..**********....',
  '...**********...',
  '...***....****..',
  '...**********...',
  '...********.....',
  '...***...***....',
  '...***....***...',
  '..****.....****.',
  '....********....',
  '..***********...',
  '..***...........',
  '..***...******..',
  '..***...******..',
  '..***......***..',
  '...**********...',
  '.....*******....',
  '..**********....',
  '...**********...',
  '...***....****..',
  '...**********...',
  '...*********....',
  '...***....****..',
  '...***********..',
  '..***********...'
]

def rainbow(pos):
  if pos < 0 or pos > 255:
    r = g = b = 0
  elif pos < 85:
    r = int(pos * 3)
    g = int(255 - pos * 3)
    b = 0
  elif pos < 170:
    pos -= 85
    r = int(255 - pos * 3)
    g = 0
    b = int(pos * 3)
  else:
    pos -= 170
    r = 0
    g = int(pos * 3)
    b = int(255 - pos * 3)
  return (r, g, b)

def show(s):
  for i in range(8):
    row = MATRIX[i]
    for j in range(16):
      c = row[j]
      if '*' == c:
        unicornhathd.set_pixel(i, j, COLORS[0][0], COLORS[0][1], COLORS[0][2])
      else:
        unicornhathd.set_pixel(i, j, 0, 0, 0)
  for i in range(8):
    row = MATRIX[8 * s + i]
    for j in range(16):
      c = row[j]
      if '*' == c:
        unicornhathd.set_pixel(8 + i, j, COLORS[s][0], COLORS[s][1], COLORS[s][2])
      else:
        unicornhathd.set_pixel(8 + i, j, 0, 0, 0)
  unicornhathd.show()

def animate():
  pos = 0
  pix = 0
  while True:
    c = rainbow(pos)
    for i in range(16):
      if pix == i:
        unicornhathd.set_pixel(7, i, c[0], c[1], c[2])
      else:
        unicornhathd.set_pixel(7, i, 0, 0, 0)
    pix = (pix + 1) % 16
    pos = (pos + 1) % 256
    unicornhathd.show()
    time.sleep(0.05)

try:
  show(SELECTED)
  animate()
    
except:
  unicornhathd.off()

