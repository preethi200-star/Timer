import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60) 
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end='\r')  # Overwrite the line each second
        time.sleep(1)
        t -= 1

    print("💥 Fire in the hole!! 💥 ")

try:
    t = int(input("Enter the time in seconds: "))
    print("Countdown starting...\n")
    time.sleep(1)
    countdown(t)
except ValueError:
    print("❌ Please enter a valid number.")
