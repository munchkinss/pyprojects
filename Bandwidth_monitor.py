''' import time
import psutil

def main():
    old_value = 0    

    while True:
        new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

        if old_value:
            send_stat(new_value - old_value)

        old_value = new_value

        time.sleep(1)

def convert_to_gbit(value):
    return value/1024./1024.*8

def send_stat(value):
    print ("%0.3f" % convert_to_gbit(value)+"MB/s")

main() '''


import psutil as ps
import time

def main():
    old_value_sent = 0
    old_value_recieve=0    

    while True:
        new_value_sent = ps.net_io_counters().bytes_sent
        new_value_recieve = ps.net_io_counters().bytes_recv
        if old_value_sent:
            print("SENT:",end="")
            send_stat(new_value_sent-old_value_sent)
        if old_value_recieve:
            print("RECIEVED:",end="")
            send_stat1(new_value_recieve-old_value_recieve)
        old_value_sent = new_value_sent
        old_value_recieve = new_value_recieve
        time.sleep(1)
def convert_to_gbit(value):
    return value/1024./1024.*8

def send_stat(value):
    print("%0.3f" % convert_to_gbit(value)+"MB/s",end=" ")
def send_stat1(value):
    print("%0.3f" % convert_to_gbit(value)+"MB/s")

main()