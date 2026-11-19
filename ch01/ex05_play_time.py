# Operation to calculate time played with an input (without datetime) - 19/11/26

time_played_ask = int(input("How many seconds did you play? : "))

hours = time_played_ask // 3600
rest = time_played_ask % 3600
minutes = rest // 60
seconds = rest % 60

time_played = f"{hours:02d}h {minutes:02d}m {seconds:02d}s"

print(f"You played {time_played} !")