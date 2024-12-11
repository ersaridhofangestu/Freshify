import sys
import time

def loading_bar():
    total = 50 
    progress = 0 
    
    while progress <= total:
        percent = (progress / total) * 100
        bar = '=' * progress  
        spaces = ' ' * (total - progress)  
        sys.stdout.write(f'\r[{bar}{spaces}] {percent:.2f}%') 
        sys.stdout.flush()
        time.sleep(0.1)  
        progress += 1  

    sys.stdout.write('\r[{}] 100.00%\n'.format('=' * total)) 
    
loading_bar()