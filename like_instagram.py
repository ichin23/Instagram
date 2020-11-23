import pyautogui as pg
#import webbrowser as wb
import time

#wb.open("instagram.com")
#time.sleep(30)

x,y=pg.size()

print(x, y)

time.sleep(2)

pg.moveTo(500, 400)

pg.scroll(-4)
pg.doubleClick()

while True:
    pg.scroll(-20)
    time.sleep(1)
    pg.click()
    pg.sleep(1)
    pg.doubleClick()
    time.sleep(3)