
# Таймер pomodoro
# При запуске консоли будет запускаться таймер длительностю в 25 минут
#1. импорт
#2. должен выводиться время, в минутах и секундах, и потом перезаписываться каждую секунду.
#3. time.sleep() для задержки 
#

import time


minutes = int(input("Введите количество минут: "))
pause_minutes = int(input("Введите сколько будет пауза: "))
work_time = minutes * 60
pause_time = pause_minutes * 60



while work_time > 0:
        m = work_time // 60
        s = work_time % 60

        print(f"\rFocus: {m:02d}:{s:02d}", end="", flush=True)
        time.sleep(1)
        work_time1 -= 1
        
while pause_time > 0:       
        m = pause_time // 60
        s = pause_time % 60
        
        print(f"\rPause: {m:02d}:{s:02d}", end="", flush=True)
        time.sleep(1)
        pause_time -= 1
    