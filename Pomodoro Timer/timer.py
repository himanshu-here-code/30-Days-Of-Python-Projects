import time

print("\n---WELCOME TO POMODORO TIMER---\n")

def countdown(minutes):
    total_seconds = minutes * 60
    
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        print(f"\rTime Remaining: {time_format}" ,end="")
        time.sleep(1)       
        total_seconds -= 1 
    print() 


def pomodoro_timer(work_duration, break_duration, cycles):
    for cycle in range(1, cycles + 1):
        print(f"\n▶️ Cycle {cycle} - Work for {work_duration} minutes.")
        countdown(work_duration) 
        
        print("\a")  
        
        print(f"\n⏸️ Cycle {cycle} - Break for {break_duration} minutes.")
        countdown(break_duration)
        
        print("\a")
        
    print("\n✅ All cycles completed! Take a longer break now.")  
    print("Pomodoro session completed! Great job!")

work_duration = int(input("Enter work duration in minutes: "))
break_duration = int(input("Enter break duration in minutes: "))
cycles = int(input("Enter number of cycles: "))

pomodoro_timer(work_duration, break_duration, cycles)