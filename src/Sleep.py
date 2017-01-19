import time
import sys
import datetime

def calculate_bed_times(wake_up_time):
    """
    Calculate perfect times to go to bed
    if you want to wake up on certain time
    """
    bed_times = []
    for i in range(1,7):
        bed_time = wake_up_time - datetime.timedelta(minutes=(90*i))
        epoch = (time.mktime(bed_time.timetuple()))
        bed_times.append(epoch)

    return bed_times


def calculate_wakeup_times(bed_time):
    """
    Calculate perfect times to go to bed
    if you want to wake up on certain time
    """
    wakeup_times = []
    for i in range(1,7):
        wakeup_time = bed_time + datetime.timedelta(minutes=(90*i))
        epoch = (time.mktime(wakeup_time.timetuple()))
        wakeup_times.append(epoch)

    return wakeup_times

def main():

    func = int(sys.argv[-2])
    epoch_time = int(sys.argv[-1])

    t = datetime.datetime.fromtimestamp(time.time())

    if func == 0:
        print (calculate_wakeup_times (t))

    if func == 1:
        print (calculate_bed_times(t))

main()
