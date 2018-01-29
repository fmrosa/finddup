# finddup

Use this script to parse long ip/mask lists and find network duplicates and overlapping.
My motivation to write this script was to reduce the size of access lists one of my customers had in their proxy. Its simple and objective... it can process 2500 entries in about 4 minutes, which represent 2500*2500 checks.

I have no intention to add threads to this but will accept help in case someone wants to.

It will parse a file called all_networks.txt that contains ip,mask separated by a comma. Output is STDOUT.

makes use of the ipaddress module so run command below to use it:

> pip install ipaddress.
