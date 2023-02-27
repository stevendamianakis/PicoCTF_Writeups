import time, os
from pwn import *

digits = "0123456789"
pin_length = 8
current_pin = ""


for i in range(pin_length):

    max_time = 0

    print("\n#########    Digit-no: "+str(i+1)+"    ############\n")

    for num in list(digits):

        try:
            p = process("/home/user/Downloads/picoctf/forensics/sidechannel/pin_checker", level="warn")
        except Exception as e:
            print("Error! The process couldn't be called")
            sys.exit(1)

        input = current_pin + num + ("0" * (pin_length - len(current_pin) - 1))

        # Calculate time taken

        start = time.time()  
        p.sendlineafter(bytes("\n",'utf-8'), bytes(input,'utf-8'))
        p.recvlines(2)
        result = p.recvline()
        stop = time.time()
        duration = stop - start

        # Check time

        if duration > max_time:
            max_time = duration
            correct = str(num)

        # Update with results

        print("Pin entered: "+str(input))
        print("Time taken: "+str(duration))
       
    current_pin += correct

# Print results

print("Pin cracked! Correct pin: "+str(current_pin))