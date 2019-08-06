from tkinter import *
import sys
out = sys.stdout
sys.stdout = open('Button.txt','w')
help(Button)
sys.stdout.close()
sys.stdout = out
