from datetime import datetime
import os
import pytz

IST = pytz.timezone("Asia/Kolkata")

timestamp = datetime.now().timestamp()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(BASE_DIR,"logs.txt")
formattedDate = datetime.now(IST).strftime("%d-%m-%y %H-%M-%S")

with open(log_path,"a") as file:
    file.write(formattedDate+"\n")
