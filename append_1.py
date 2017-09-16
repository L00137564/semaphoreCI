# AUTHOR: Owen Lyons
# DATE: 21/08/17
# PROGRAM: appends to file.

import datetime
import time


def date_time(): # prints current date and time
    project_init_date = datetime.datetime.now()

    date = str(project_init_date)[:-15] # splices date for use in the string below
    time = str(project_init_date)[11:19] # splices time for use in the string below

    date_time = "Date: " + date + " | Time: "+ time # more aesthetic that printing 'datetime()'

    return date_time

###################################################################################################
###################################################################################################

if __name__ == "__main__":



    f = open("to_be_appended.txt", "a")
    f.write("\n")
    f.write("APPEND_1 : This line was appended on: " + date_time())

    #time.sleep(1)
    #print("SLEPT for 1 second")

    print("")
    print("####################################################")
    print("Append_1")
    print("####################################################")


    f.close()
