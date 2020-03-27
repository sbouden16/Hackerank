import json
from time import time,localtime,strftime


# Python time.strftime()

#y = localtime()
#print(localtime(time()))
#time_stamp_neded = strftime("%m/%d/%Y, %H:%M:%S",y)


def TEXT_push(file,function):
    y_1 = localtime()
    initial_time_stamp = strftime("%m/%d/%Y, %H:%M:%S", y_1)
    #x = {"Timestamp":{initial_time_stamp}}
    dct = {}
    count = 0
    with open("%s.txt"%(file),function) as json_file:
        if type(json_file.newlines) == type(None):
            prev_time_stamp = initial_time_stamp
            while count <=1:
                y_3 = localtime()
                onTime_time_stamp = strftime("%m/%d/%Y, %H:%M:%S",y_3)
                impt = input("Key: ")
                impt2 = input("Value: ")
                dct[impt] = {impt2:{"Original_Timestmp":initial_time_stamp}, "Prev_Timestamp":prev_time_stamp,"OnTime_Stamp":onTime_time_stamp}
                count += 1
                prev_time_stamp = onTime_time_stamp
        else:
            pass
        return json.dump(dct,json_file)
        
        
if __name__ == "__main__":
    TEXT_push("data","w")

