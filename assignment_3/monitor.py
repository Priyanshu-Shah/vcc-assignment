import psutil
import time
import os

THRESHOLD = 75

while True:
    cpu = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu}%")

    if cpu > THRESHOLD:
        print("Threshold exceeded! Triggering cloud VM...")
        
        os.system("gcloud compute instances start cloud-vm --zone=YOUR_ZONE")
        time.sleep(2)
        os.system("gcloud compute ssh cloud-vm --zone=YOUR_ZONE --command='python3 app.py &'")
        break

    time.sleep(2)