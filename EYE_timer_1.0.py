import time

def work():
        while True:
            duration_input = input("Duration (minutes): ")
            try:
                duration = int(duration_input)
                if duration <= 0:
                    print("Please enter a positive number for duration.")
                    continue
                break
            except ValueError:
                print("Invalid input: please enter a number for duration.")
        if duration > 20:
            print("You will a experience a 20s break every 20 minutes")
            breaks = duration // 20
            timer_duration = 20*60
            while breaks > 0:
                time.sleep(timer_duration)
                breaks -= 1
                print("Time for a 20s break! Look away 20ft")
                time.sleep(20)
                print("Now you can return to what you where doing :)")
        else:
            print("You won't experience any breaks!")

work()

            
        


