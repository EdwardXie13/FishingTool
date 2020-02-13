import pyautogui
import time
import ctypes
import random
import sys
import os
import numpy as np
import win32gui

from imagesearch import *
from directkeys import PressKey, ReleaseKey, Esc, W, A, S, D, R, I, Space, Lctrl

from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

from ctypes import windll
import pyscreeze
from grabscreen import grab_screen

hdc= windll.user32.GetDC(0)

def staticred():
  redbar = sRGBColor(148, 100, 116)
  redbar = convert_color(redbar, LabColor)
  return redbar

def staticGold():
  gold = sRGBColor(255, 200, 0)
  gold = convert_color(gold, LabColor)
  return gold

def staticWhite():
  white = sRGBColor(255, 255, 255)
  white = convert_color(white, LabColor)
  return white

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()  
    except:
        return False

def pressLctrl():
  PressKey(Lctrl)
  time.s;eep(.1)
  ReleaseKey(Lctrl)
    
def pressSpace():
  PressKey(Space)
  time.sleep(.1)
  ReleaseKey(Space)

def pressW():
  PressKey(W)
  time.sleep(.1)
  ReleaseKey(W)

def pressA():
  PressKey(A)
  time.sleep(.1)
  ReleaseKey(A)

def pressS():
  PressKey(S)
  time.sleep(.1)
  ReleaseKey(S)

def pressD():
  PressKey(D)
  time.sleep(.1)
  ReleaseKey(D)

def pressR():
  PressKey(R)
  time.sleep(.1)
  ReleaseKey(R)

def pressI():
  PressKey(I)
  time.sleep(.1)
  ReleaseKey(I)

def isred(pix):
  color = sRGBColor(*(pix))
  color = convert_color(color, LabColor)
  similarity = delta_e_cie2000(color, minigame_red)
  return similarity

def isGold(pix):
  color = sRGBColor(*(pix))
  color = convert_color(color, LabColor)
  similarity = delta_e_cie2000(color,statusGold)
  return similarity

def isWhite(pix):
  color = sRGBColor(*(pix))
  color = convert_color(color, LabColor)
  similarity = delta_e_cie2000(color,statusWhite)
  return similarity

def reelIn():
  #const 1000, 405, 1090, 424
  pressSpace()

  #find the bar
  while True:
    if (findbar() == True):
      break
  
  #press space at the right time
  while True:
    pix = pyscreeze.pixel(983,407) #default is 1030
    if (isred(pix) <= 30):
      pressSpace()
      break
  #pause before captcha shows up
  time.sleep(3.2)
  
  captchaProcess()
  time.sleep(2)

  checkLoot()
  time.sleep(1) #leave here for testing purposes

def checkLoot():
  lootWin = pyautogui.screenshot(region=(1417, 510, 315, 99))
  #lootWin = pyautogui.screenshot('lootwin1.png',region=(1417, 510, 315, 99))
  time.sleep(1.5)

  lootFiles = os.listdir("loot_images/")
  #scans row wise
  for col in range (0,2):
    for row in range(0,6): 
      for image in lootFiles:
        obtained = pyautogui.locate("loot_images/%s" % image, lootWin, region=((row*46)+(row*8), (col*46)+(col*8), 46, 46), confidence=0.99  )
        if (obtained != None):
          print(image)
          #if press R loot
          pressR()
          #if click loot
          return

def captchaFinder():
  BarLocation = pyautogui.locateOnScreen('captcha_bar.png', region=(690, 300, 460, 280))
  return BarLocation
  
def captchaProcess():
  coords = captchaFinder()
  if(coords == None):
    print("perfect")
    return
  #convert numpy.int64 to int
  X_coord = coords[0].item()
  Y_coord = coords[1].item()

  screen = grab_screen(region=(X_coord-33, Y_coord-42, X_coord + 312, Y_coord-31))

  word = ""
  #time.sleep(.16)
  for x in range (0,10):
    word += captcha(x, screen)
    time.sleep(.16)
    if(word.endswith('-') == True):
      break
  print(word)

def captcha(loopVal, image):
  pix1 = image[2, (loopVal*35)+7]
  pix2 = image[7, (loopVal*35)+7]
  if(np.array_equal(pix1, pix2) == True):
    pressA()
    return 'A'
  
  pix1 = image[2, (loopVal*35)+2]
  pix2 = image[7, (loopVal*35)+2]
  if(np.array_equal(pix1, pix2) == True):
    pressD()
    return 'D'

  pix1 = image[2, (loopVal*35)+1]
  pix2 = image[2, (loopVal*35)+7]
  if(np.array_equal(pix1, pix2) == True):
    pressS()
    return 'S'

  pix1 = image[7, (loopVal*35)+2]
  pix2 = image[7, (loopVal*35)+6]
  if(np.array_equal(pix1, pix2) == True):
    pressW()
    return 'W'
  
  return'-'

def rodSwitch():
  inventoryRegion = pyautogui.screenshot(region)

def findbar():
  pix1 = pyscreeze.pixel(849,368)
  pix2 = pyscreeze.pixel(849,372)
  if ((isWhite(pix1) <= 10) and (isWhite(pix2) <= 10)):
    return True

def castRodState():
  #766,53/55/57
  pix1 = pyscreeze.pixel(766,53)
  pix2 = pyscreeze.pixel(766,57)

  if ((isGold(pix1) <= 10) and (isGold(pix2) <= 10)):
    return True

def reelRodState():
  #993,53/55/57
  pix1 = pyscreeze.pixel(993,53)
  pix2 = pyscreeze.pixel(993,57)

  if ((isGold(pix1) <= 10) and (isGold(pix2) <= 10)):
    return True

def invOpen(): #                                                      1486, 230
  invState = pyautogui.locateOnScreen('inv_icon.png', region=(1463, 203, 23, 27))
  if(invState == None):
    return False
  else:
    return True

def checkRod():
  shutdown = False
  #open inventory
  if (invOpen() == False):
    pressI()
  time.sleep(2)
  #move out of the way of inv(right on pearl tab)
  pyautogui.moveTo(1600, 260, .4)
  bustedHeld = pyautogui.locateOnScreen('broke_rod.png', region=(1136, 549, 44, 44))
  if(bustedHeld == None):
    pressI()
    time.sleep(.4)
    return
  else:
    inventoryRegion = pyautogui.screenshot(region=(1463,328,423,423))

    for col in range(0,8):
      for row in range(0,8):
        rod_search = pyautogui.locate('eph_10_rod.png', inventoryRegion, region=( (row*45)+(row*8)+row, (col*45)+(col*8)+col, 45, 45) )
        if(rod_search == None):
          #os.system("shutdown /s /t 10")
          shutdown = True
          #print('shutdown')
        else:
          pyautogui.moveTo(1463 + rod_search[0] + 20, 328 + rod_search[1] + 20, .4)
          time.sleep(.5)

          pyautogui.mouseDown(button='right')
          time.sleep(.1)
          pyautogui.mouseUp(button='right')

          time.sleep(.4)
          pressI()
          time.sleep(1.5)
          return

  #if(shutdown == True):
    #print("shutdown confirmed")


def activateBDO():
  app = win32gui.FindWindow("BlackDesertWindowClass", None)  
  win32gui.SetForegroundWindow(app)
  return

minigame_red = staticred()
statusGold = staticGold()
statusWhite = staticWhite()
def main():
  print("start")
  activateBDO()
  time.sleep(2)
  fishing = False
  while True:
    #if ((fishing == False and castRodState() == True) or (castRodState() == True) ):
    if (castRodState() == True ):
      print("cast")
      pressSpace()
      #startTimer
      fishing = True
      time.sleep(7)
      if(castRodState() == True ):
        print('checking rod')
        checkRod()
    #elif (fishing == True and reelRodState() == True):
    elif (reelRodState() == True):
      print("reel")
      fishing = False
      reelIn()
    elif (fishing == True):
      print("waiting")
      #checkTimer
      time.sleep(1)
  
if is_admin():
  main()
else:
  ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
