import json
from time import time,localtime,strftime

def read_TXT(file):
    temp_json_dct = {}
    with open("%s.txt"%(file),"r+") as json_file:
        for i in json_file:
            temp_json_dct = i
    return temp_json_dct
    

def write_TXT(currency,price,file,initial_time_stamp,prev_time_stamp):
    temp_json_dct = {}
    __localtime = localtime()
    onTime_time_stamp = strftime("%m/%d/%Y, %H:%M:%S",__localtime)
    temp_json_dct[currency] = {price:{"Original_Timestmp":initial_time_stamp}, "Prev_Timestamp":prev_time_stamp,"OnTime_Stamp":onTime_time_stamp}
    with open("%s.txt"%(file),"a") as json_file:
        return json.dump(temp_json_dct,json_file)
    

def TXT_handler(file):
    __localtime = localtime()
    initial_time_stamp = strftime("%m/%d/%Y, %H:%M:%S", __localtime)

    #with open("%s.txt"%(file),w+) as json_file:

        #if json_file == None:
            #temp_json_dct = {}
        
        #else:
            #pass
            
 
    prev_time_stamp = initial_time_stamp
    imp = input("Stop , Write, Read: ").upper()

    while imp != "S":
        
        if imp == "W":
            impt = input("Currency: ")
            impt2 = input("Price_at_time: ")
            write_TXT(impt,impt2,file,initial_time_stamp,prev_time_stamp)
            #json.dump(temp_json_dct,json_file)
            #prev_time_stamp = temp_json_dct[impt][impt2]['Original_Timestmp']
        
        elif imp == "R":
            print(read_TXT(file))
            
        else:
            print("Select: S,R,W")

        imp = input("Stop , Write, Read: ")
    

    



#modularize the function. 

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
#print(data)
        
 # program that reads the console. reads or writes to the file.


     #infinite loop- ask if you want to read or write. if write send to fucntion, if read sent ot read.

import os
os.chdir(os.path.dirname(__file__))
print(os.getcwd())

if __name__ == "__main__":
    TXT_handler("data")


