import sys
import time

logo = """
 ______   _         ______   _______  
|  ____| | |       |  __  | |  ___  | 
| |__    | |       | |  | | | |___| | 
|  __|   | |       | |  | | |  _____| 
| |      | |_____  | |__| | | |       
|_|      |_______| |______| |_|       

   [$FLOP is food for your AI agent.]
"""

def boot_sequence():
    for char in logo:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.004)

if __name__ == "__main__":
    boot_sequence()
