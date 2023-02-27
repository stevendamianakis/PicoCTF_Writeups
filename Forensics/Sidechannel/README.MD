# Sidechannel
**A simple side-channel timing attack.**

- Download the executable file. Executing the file, we can check that we provide an 8 pin password as an input, the program checks if the pin is correct and replies with the appropriate response and then exits.

- The name of the challenge and the hints, can indicate the solution of this challenge. 

- In side-channel timing attacks, the adversaries measure the duration of the password verification mechanism, by alternating only 1-bit at a time. If the executable programs are not well protected, then it is very easy for adversaries to guess the pin by finding the correct bit each time. Normally, the correct bit will take the longest verification duration compared to the other bits(in case the engineers of the program have not added random delays to the verification duration, to protect it).

- Using bruteforce we would need 10^8 combinations, but with a side-channel timing attack it only takes 8*10 combinations.

- Running the script will generate over-time the correct pin. Then you can submit the pin through connecting to the picoCTF server that is mentioned in the description of the challenge.
