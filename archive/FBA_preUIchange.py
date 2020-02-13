import pyautogui
import time
import ctypes
import sys
import os
import numpy as np
import win32gui

from imagesearch import *
from directkeys import PressKey, ReleaseKey, Esc, W, A, S, D, R, Space, Lctrl

from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

from ctypes import windll
import pyscreeze

hdc= windll.user32.GetDC(0)

def staticBlue():
  bluebar = sRGBColor(86, 140, 168)
  bluebar = convert_color(bluebar, LabColor)
  return bluebar

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

def isBlue(pix):
  color = sRGBColor(*(pix))
  color = convert_color(color, LabColor)
  similarity = delta_e_cie2000(color, minigame_blue)
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
    pix = pyscreeze.pixel(1030,405) #default is 1030
    if (isBlue(pix) <= 85):
      pressSpace()
      break
  #pause before captcha shows up
  time.sleep(3.2)
  
  captchaProcess()
  time.sleep(2)

  checkLoot()
  time.sleep(1) #leave here for testing purposes

def checkLoot():
  #                                                                1724, 735 
  #lootWin = pyautogui.screenshot('lootWin1.png', region=(1537, 595, 188, 141))
  lootWin = pyautogui.screenshot(region=(1537, 595, 188, 141))
  time.sleep(1.5)
  #if(lootWin == None):
    #print("not found")
  #else:
    #print("found")
  lootFiles = os.listdir("loot_images/")
  #scans row wise
  for col in range (0,3):
    for row in range(0,4): 
      for image in lootFiles:
        obtained = pyautogui.locate("loot_images/%s" % image, lootWin, region=((row*46)+row, (col*46)+col, 46, 46), confidence=0.95  )
        if (obtained != None):
          print(image)
          pressR()
          return

def captchaFinder():
  BarLocation = pyautogui.locateOnScreen('captcha_bar.png', region=(690, 300, 460, 280))
  #print(BarLocation)
  return BarLocation
  
def captchaProcess():
  coords = captchaFinder()
  if(coords == None):
    print("perfect")
    return
  #convert numpy.int64 to int
  X_coord = coords[0].item()
  Y_coord = coords[1].item()

  #image = pyautogui.screenshot('test.png', region=(X_coord-33, Y_coord-42, 345, 11))
  image = pyautogui.screenshot(region=(X_coord-33, Y_coord-42, 345, 11))
  word = ""
  for x in range (0,10):
    word += captcha(x, image)
    time.sleep(.16)
    if(word.endswith('-') == True):
      break
  print(word)

def captcha(loopVal, image):
  pix1 = image.getpixel( (((loopVal * 35) + 7), 2))
  pix2 = image.getpixel( (((loopVal * 35) + 7), 7))
  if(pix1 == pix2):
    pressA()
    return 'A'
  
  pix1 = image.getpixel( (((loopVal * 35) + 2), 2))
  pix2 = image.getpixel( (((loopVal * 35) + 2), 7))
  if(pix1 == pix2):
    pressD()
    return 'D'

  pix1 = image.getpixel( (((loopVal * 35) + 1), 2))
  pix2 = image.getpixel( (((loopVal * 35) + 7), 2))
  if(pix1 == pix2):
    pressS()
    return 'S'

  pix1 = image.getpixel( (((loopVal * 35) + 2), 7))
  pix2 = image.getpixel( (((loopVal * 35) + 6), 7))
  if(pix1 == pix2):
    pressW()
    return 'W'
  
  return'-'

def findbar():
  pix1 = pyscreeze.pixel(849,368)
  pix2 = pyscreeze.pixel(849,372)
  if ((isWhite(pix1) <= 10) and (isWhite(pix2) <= 10)):
    return True

def castRodState():
  #766,53/55/57
  pix1 = pyscreeze.pixel(766,53)
  pix2 = pyscreeze.pixel(766,57)
  #print(pix1)
  #print(pix2)
  if ((isGold(pix1) <= 10) and (isGold(pix2) <= 10)):
    return True
  #pix1 = pyautogui.pixelMatchesColor(766, 53, (249,208,67), tolerance=5)
  #pix2 = pyautogui.pixelMatchesColor(766, 55, (249,208,67), tolerance=5)
  #pix3 = pyautogui.pixelMatchesColor(766, 57, (249,208,67), tolerance=5)
  #if (pix1 == pix2):
  #  if (pix2 == pix3):
  #    return pix1
  #return False

def reelRodState():
  #993,53/55/57
  pix1 = pyscreeze.pixel(993,53)
  pix2 = pyscreeze.pixel(993,57)
  #print(pix1)
  #print(pix2)
  #apparently is (255,255,-1) after 35 mins
  if ((isGold(pix1) <= 10) and (isGold(pix2) <= 10)):
    return True

def activateBDO():
  app = win32gui.FindWindow("BlackDesertWindowClass", None)  
  win32gui.SetForegroundWindow(app)
  return

minigame_blue = staticBlue()
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
      time.sleep(5)
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
