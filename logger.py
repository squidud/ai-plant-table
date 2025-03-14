import time

LOG_FILE = "static/log.txt"

def log_action(action):
    timestamp = time.strftime("%m/%d/%y %H:%M")
    log_entry = f"{timestamp}, {action}\n"
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

log_action("hello2")