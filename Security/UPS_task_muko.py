# ups_simulator_base.py 

# Simulates a system running on UPS during a power outage. 

 

import time 

 

mains_power = False  # Simulate a power cut 

ups_battery_percent = 100 

critical_battery_level = 10 

 

print("System running on UPS. Mains power lost.") 

print(f"UPS Battery: {ups_battery_percent}%") 

 

while ups_battery_percent > critical_battery_level: 

    time.sleep(0.5)  # Simulate time passing 

    ups_battery_percent -= 5  # Battery drains 

    print(f"UPS Battery: {ups_battery_percent}%") 

 

    # --- YOUR TASK: ADD LOGIC HERE --- 

while ups_battery_percent <= critical_battery_level:
    
    if ups_battery_percent == 0:
        print("UPS BATTERY IS ABOUT TO FAIL: INITIATING GRACEFUL SHUTDOWN..")
        break
    else:
        print(f"UPS BATTERY CRITICAL: {ups_battery_percent}")
    

print("System has shut down.") 