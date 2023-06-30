#You can check these builtin functions by using import sys and dir(sys) then all the builtin function are listed then you can check the module 
# you need to see and know then just type help('module').
#if you just use 'while true' function then you couldn't stop the program and
# give it time so you have to use 'time' function then from it use 'sleep'. to stop the script from running.
#modules have to be imported inorder to use them or else you will get an error.

import time
import os 
import pandas

while True:
    if os.path.exists("temps_today.csv"):
        
        data = pandas.read_csv("temps_today.csv")
        print(data.mean())
    else: 
        print("file does not exist")
    time.sleep(10)
    
#the program works fine which prints file does not exist if it really does not exist
#if you want to check os modules address then first you have to import sys and then import os  in the command prompt and 
# then type sys.prefix then it displays the address of the file.
#then lets 
#Like all the data types there is a data type of pandas called pandas.core.frame.Dataframe'

#Cheatsheets(imported Modules)

#Builtin objects are all objects that are written inside python interpreter in c language.
#Builtin modules contain builtins objects.
#some builtin objects are not immediately available in the global namespace. they are parts of a builtin module to use those objects the module needs to be imported first.
#Eg.
    import time
    time.sleep(5)
    
#A list of all builtin modules can be printed out with:
import sys
sys.builtin_module_names
  
#Standard libraries is a jargon that includes both builtin modules written in c and also modules written in python.
#Standard libraries written in python reside in the python installation directory as .py files. you can find their directory path with sys.prefix.
#packages are a collection of /py modules.
#third-party libraries are packages or modules written by third-party persons(not the python core development team.)
#third-party libraries can be intalled from the terminal/command line:
#Windows
#pip intall pandas or use python -m pip install pandas if that doesn't work.
