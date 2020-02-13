##import pyautogui
##import time
##import os
##
##im2 = pyautogui.screenshot('FBA_IMAGE.png', region=(0,0,300,300) )
##time.sleep(2)
##
##os.remove("FBA_IMAGE.png")

from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
from imagesearch import *
import pyautogui
import numpy as np
import os

from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

##useless_var = imagesearch_region_loop('nAuPglj.png', 0, 821, 403, 1097, 426, .9)
#useless_var = imagesearch_region_loop('nAuPglj.png', 0, 100, 100, 1920, 1080, .9)

#print(useless_var)
#pyautogui.moveTo(useless_var[0],useless_var[1],duration = .1)
#print(pytesseract.image_to_string(Image.open('enhanced_sample1.png')))

##def RGBtoINT(r,g,b):
##    RGBint = (r<<16) + (g<<8) + b
##    return RGBint
##
##def getRGBfromI(RGBint):
##    blue =  RGBint & 255
##    green = (RGBint >> 8) & 255
##    red =   (RGBint >> 16) & 255
##    return red, green, blue
##
def staticred():
  bluebar = sRGBColor(119,35,40)
  bluebar = convert_color(bluebar, LabColor)
  return bluebar
redColor = staticred()

###print(blueColor)
##
def isGold(pix):
  color = sRGBColor(119,35,40)
  color = convert_color(color, LabColor)
  similarity = delta_e_cie2000(color,statusGold)
  return similarity

def staticGold():
  gold = sRGBColor(199, 150, 170)
  gold = convert_color(gold, LabColor)
  return gold
statusGold = staticGold()

#pix1 = pyautogui.pixel(993,53)
#pix2 = pyautogui.pixel(993,57)
#print(pix1)
#print(pix2)
print(isGold(redColor))
#print(isGold(pix2))
##
##pix2 = (151,27,28)
##val2 = func(pix2)
##print(val2)
##
##pix3 = (255,0,0)
##val3 = func(pix3)
##print(val3)


##im = Image.open("temp.png") # the second one 
##im = im.filter(ImageFilter.MedianFilter())
##enhancer = ImageEnhance.Contrast(im)
##im = enhancer.enhance(2)
##im = im.convert('1')
##im.save('temp2.png')
##text = pytesseract.image_to_string(Image.open('temp2.png'))
##print(text)

#BarLocation = pyautogui.locateOnScreen('captcha_bar.png', region=(690, 300, 460, 280))
#print(BarLocation)

##def captcha():
##  #run the code for the first box
##  coords = (828,439,6,6) #expected values
##  print(type( coords[0] ) )
##  #letter = captcha0(coords)
##  #letter2_9 = captcha1_8(coords)
##  #letter10 =  
##  
##def captcha0(coords):
##  pix1 = pyautogui.pixel(coords[0]-26,coords[1]-35)
##  pix2 = pyautogui.pixel(coords[0]-26,coords[1]-40)
##  if(pix1 == pix2):
##    print('A')
##    return 'A'
##  
##  pix1 = pyautogui.pixel(coords[0]-31,coords[1]-34)
##  pix2 = pyautogui.pixel(coords[0]-31,coords[1]-41)
##  if(pix1 == pix2):
##    print('D')
##    return 'D'
##
##  pix1 = pyautogui.pixel(coords[0]-26,coords[1]-40)
##  pix2 = pyautogui.pixel(coords[0]-32,coords[1]-40)
##  if(pix1 == pix2):
##    print('S')
##    return 'S'
##
##  pix1 = pyautogui.pixel(coords[0]-27,coords[1]-35)
##  pix2 = pyautogui.pixel(coords[0]-32,coords[1]-35)
##  if(pix1 == pix2):
##    print('W')
##    return 'W'
##  
##  print('X')
##  return 'X'
##
##pix1 = pyautogui.pixel(100,100)
##print(type(pix1[0]))

# for example, numpy.float32 -> python float
##BarLocation = pyautogui.screenshot(region=(1273, 512, 345, 11))
##BarLocation = pyautogui.locate(
##print(BarLocation)
##if(BarLocation == None):
##  BarLocation="X"
##  if(BarLocation == "X"):
##    print('gone')
##image = pyautogui.screenshot('test1.png', region=(600-33, 600-42, 345, 11))
##lol = "1"
##for x in range (0,10):
##  lol += '0'
##  #print(x)
##  #pix1 = image.getpixel(((35*x+7), 2))
##  #print(pix1)
##print(lol)

##
##from pynput import keyboard
##
##def on_press(key):
##    try:
##        print('alphanumeric key {0} pressed'.format(
##            key.char))
##    except AttributeError:
##        print('special key {0} pressed'.format(
##            key))
##
##def on_release(key):
##    print('{0} released'.format(
##        key))
##    if key == keyboard.Key.esc:
##        # Stop listener
##        return False
##
### Collect events until released
##with keyboard.Listener(
##        on_press=on_press,
##        on_release=on_release) as listener:
##    listener.join()
