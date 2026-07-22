from plyer import notification
import time
import winsound
timerduration = 20*60
while True:
    time.sleep(timerduration)
    winsound.Beep(1000, 750)
    notification.notify(
        title = "Time for a 20s break!",
        message = "Take a break and look away from your screen 20ft away until you hear the next beep signal!",
        app_name = "Eye Break Starts!",
        timeout = 5,
    )
    for seconds_left in range(20, 0, -1):
        #print(f"Break ends in: {seconds_left}s ", end="\r")
        time.sleep(1)
    winsound.Beep(1000, 750)
    notification.notify(
        title = "Your break is over!",
        message = "You can return to what you were doing :)",
        app_name = "Eye Break Over!",
        timeout = 5,
    )