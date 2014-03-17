#!/usr/bin/env/ python3.3
# editing
 
import sys
import subprocess
import pty
import os
import select
 
def betterprocess(filename, command, p):
    #if (p is None):
    #   p=openFile(filename)
    #p = subprocess.Popen(['ed', filename], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
#user_info = raw_input("Please enter commands on individual lines: ")
#user_info should be each individual command entered, if taken as an array use a for loop
#while (user_info != "q"):
    if command == "p" or command == ",p":
        try:
            fi = open(filename, 'r')
            #p.communicate()
            return fi.read()
        except:
            return "File Not Found"
    else:
        if (command.isnumeric()):
            q = subprocess.Popen(['ed', filename], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            q.stdin.write(bytes(command,'UTF-8'))
            q.stdin.write(bytes('\n','UTF-8'))
            print ("command="+str(bytes(command,'ascii')))
            p.stdin.write(bytes(command, 'ascii'))
            p.stdin.write(bytes('\n','ascii'))
            p.stdin.flush()
            return str(q.communicate()[0])[2:-1]
        else:
            print ("command="+str(bytes(command,'ascii')))
            p.stdin.write(bytes(command,'UTF-8'))
            p.stdin.write(bytes('\n','UTF-8'))
            p.stdin.flush()
            return ""
    #user_info = raw_input("> ")
#p.stdin.write('q\n')
#p.communicate()[0]
#p.stdin.close()
 
 
 
 
#nfile = raw_input("Enter the file to be edited: ")
 
#subprocess.call(["ed", nfile], stdout=subprocess.PIPE)
def openFile(filename):
    #master, slave=pty.openpty()
    p = subprocess.Popen(['ed', bytes(filename,'UTF-8')], stdout=subprocess.PIPE, stdin=subprocess.PIPE, close_fds=True)
    #os.close(slave)
    return p
 
def processCommand(string, p):
    if (string=="q"):
        p.stdin.write(bytes('q\n','UTF-8'))
        #out=p.communicate()[0]
        #p.poll()
        #p.stdout.readline()
        p.stdin.close()
        return (None, "File closed")
    p.stdin.write(bytes(string,'UTF-8'))
    p.stdin.write(bytes('\n','UTF-8'))
    out=""
    if (string == "p" or string.isdigit() or string == ",p"):
        out=p.communicate()[0]
    #   while (p.poll is None):
    #       rlist, wlist, xlist=select.select([master],[],[])
    #       for f in rlist:
    #           out=out+os.read(f,1000)
    #       print(out)
        #out = p.stdout.readline()# p.communicate()[0]
         
#   p.stdin.write(bytes('.\nw\n','UTF-8'))
    return (p,out)
#while (user_info != "q"):
 #   p.stdin.write(user_info)
  #  p.stdin.write('\n')
#    if (user_info == "p" or
# float(user_info)):
#           print p.stdout.readline()
#if taken as an array end here, if the process is continual, back and forth response between the client and server replace the below line with any sort of command prompt/way to receive information
   # user_info = raw_input("> ")
#p.stdin.write('q\n')
#p.communicate()[0]
#p.stdin.close()
