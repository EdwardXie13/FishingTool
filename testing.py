##from ctypes import *
##user= windll.LoadLibrary("c:\\windows\\system32\\user32.dll") #I am in windows 2000, may be yours will be windows
##h = user.GetDC(0)
##gdi= windll.LoadLibrary("c:\\windows\\system32\\gdi32.dll")
##counter=0
##while True:
##  counter+=1
##  print(counter)
##  print(gdi.GetPixel(h,1023,767))


##from ctypes import windll
import time
import pyautogui
#import pyscreeze

##dc= windll.user32.GetDC(0)
##
##def getpixel(x,y):
##    return windll.gdi32.GetPixel(dc,x,y)
##counter=0

##def pixel(x, y):
##    # On Windows, calling GetDC() and GetPixel() is twice as fast as using our screenshot() function.
##    hdc = windll.user32.GetDC(0)
##    color = windll.gdi32.GetPixel(hdc, x, y)
##    # color is in the format 0xbbggrr https://msdn.microsoft.com/en-us/library/windows/desktop/dd183449(v=vs.85).aspx
##    r = color % 256
##    g = (color // 256) % 256
##    b = color // (256 ** 2)
##    return (r, g, b)
##    with __win32_openDC(0) as hdc: # handle will be released automatically
##        color = windll.gdi32.GetPixel(hdc, x, y)
##        if color < 0:
##            raise WindowsError("windll.gdi32.GetPixel faild : return {}".format(color))
##        # color is in the format 0xbbggrr https://msdn.microsoft.com/en-us/library/windows/desktop/dd183449(v=vs.85).aspx
##        bbggrr = "{:0>6x}".format(color) # bbggrr => 'bbggrr' (hex)
##        b, g, r = (int(bbggrr[i:i+2], 16) for i in range(0, 6, 2))
##        return (r, g, b)
##
##
##def __win32_openDC(hWnd):
##        hDC = windll.user32.GetDC(hWnd)
##        if hDC == 0: #NULL
##            raise WindowsError("windll.user32.GetDC failed : return NULL")
##        try:
##            yield hDC
##        finally:
##            if windll.user32.ReleaseDC(hWnd, hDC) == 0:
##                raise WindowsError("windll.user32.ReleaseDC failed : return 0")


from grabscreen import grab_screen
import cv2
import numpy as np

#while(True):
screen = grab_screen(region=(1500,876,1845,887))
# resize to something a bit more acceptable for a CNN
#screen = cv2.resize(screen, (345,11))
# run a color convert:
screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

cv2.imshow('window',cv2.resize(screen,(345,11)))

print(screen[10,10])
print(screen[10,11])
print(screen[10,12])
print( np.array_equal(screen[10,10], screen[10,11]) )
  
if cv2.waitKey(25) & 0xFF == ord('q'):
  cv2.destroyAllWindows()

