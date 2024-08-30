import time 
waiT_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempts",attempts +1 , "-wait time",waiT_time)
    time.sleep(waiT_time)
    waiT_time*=2
    attempts +=1