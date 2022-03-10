

import datetime
from datetime import datetime
from Features.csv_writer import prev_time


def inactive(file, time_difference):
        time_now = datetime.now().strftime("%H:%M:%S")  
        time_prev = prev_time(file)
        FMT = '%H:%M:%S'
        print(time_now) 
        print(time_prev)
        difference =(datetime.strptime(time_now, FMT) - datetime.strptime(time_prev, FMT))
        print("__________________Time Difference_______________")
        print(difference)
        total_seconds_difference = difference.total_seconds()
        print("______________Time Differnce in seconds______________")
        print(total_seconds_difference)
        
        if total_seconds_difference >=time_difference:
            print("___________The status turned False__________")
            return False
        else:
            print("___________The status turned True__________")
            return True