import logging 
import os 
from datetime import datetime 


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #"C:/project/logs"
logs_path = os.path.join(os.getcwd(), "logs",LOG_FILE) #"05_19_2026_10_30_20.log"
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) #"C:/project/logs/05_19_2026_10_30_20.log"

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
#[ 2026-05-19 22:45:30 ] 10 root - INFO - Program started

