"""
author

"""
import pywinmacro as pw
import time

def your_function():
    # implement your function here
    pw.key_on("window")
    pw.key_on("r")
    pw.key_off("window")
    pw.key_off("r")
    time.sleep(1)
    pw.type_in("chrome")
    time.sleep(1)
    pw.key_press_once("enter")


your_function()