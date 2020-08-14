import json
from time import time,localtime,strftime
#__temp_Prev_Timestamp = None

def read_TXT(file):
    temp_json_dct = {}
    with open("%s.txt"%(file),"r") as json_file:
        for i in json_file:
            temp_json_dct = i
    return temp_json_dct
    

def write_TXT(currency,price,file,initial_time_stamp,prev_time_stamp):
    temp_json_dct = {}
    __localtime = localtime()
    onTime_time_stamp = strftime("%m/%d/%Y, %H:%M:%S",__localtime)
    temp_json_dct[currency] = {price:{"Original_Timestmp":initial_time_stamp}, "Prev_Timestamp":prev_time_stamp,"OnTime_Stamp":onTime_time_stamp}
    #__temp_Prev_Timestamp = prev_time_stamp
    with open("%s.txt"%(file),"a") as json_file:
        return json.dump(temp_json_dct,json_file)

    

def TXT_handler(file):
    __localtime = localtime()
    initial_time_stamp = strftime("%m/%d/%Y, %H:%M:%S", __localtime)
            
    imp = input("Stop , Write, Read: ").upper()
    #if __temp_Prev_Timestamp == None:
        #prev_time_stamp = strftime("%m/%d/%Y, %H:%M:%S", __localtime)
    #else:
    prev_time_stamp = initial_time_stamp

    while imp != "S":
        
        if imp == "W":
            impt = input("Currency: ")
            impt2 = input("Price_at_time: ")
            write_TXT(impt,impt2,file,initial_time_stamp,prev_time_stamp)
            prev_time_stamp = strftime("%m/%d/%Y, %H:%M:%S", __localtime)
        
        elif imp == "R":
            print(read_TXT(file))

        elif imp =="S":
            break
            
        else:
            print("Select: S,R,W")

        imp = input("Stop , Write, Read: ")
    


if __name__ == "__main__":
    TXT_handler("data")


