#!/usr/bin/python3

# INET4031
# Amanda
# 3/24/2025
# 3/25/2025

#import os: use for reading/writing in the file
#import re: supports working with regular expression
#import sys: access to functions and variables
import os
import re
import sys


def main():
    for line in sys.stdin:

        #checks if the line starts with the # character
        #
        match = re.match("^#",line)

        #would remove any whitespace from the line while it also splits using the :
        fields = line.strip().split(':')

        #this if statement checks if the line of code starts with the # character or if the line dose not pass 5 fields if true it will continue
        #the if statement rely's with the two prior of lines to check for # characters not pass 5 fields. 
        if match or len(fields) != 5:
            continue

        #username = fields[0] has the username from the first field
        #password = fields[1] has the password from the second field
        #the final line would combine into the gecos
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #splits the fifth field into groups using the comma
        groups = fields[4].split(',')

        #the print statement will print a message how theres an account creating depending on the username used
        print("==> Creating account for %s..." % (username))

        #prints a message for a password set depending on the username that was set on the previous line
        #cmd: commands to adduser based on the gecos field and its username
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)


        #The first time you run the code...what should you do here?  If uncommented - what will the os.system(cmd) statemetn attempt to do?
        #print cmd
        #os.system(cmd)

        #print statement will print how it will set the password for its username
        print("==> Setting the password for %s..." % (username))
        #cmd line of code sets the said users password twice 
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        #the os.system(cmd) statement will try to execute in the systems command line
        #print cmd
        #os.system(cmd)

        for group in groups:
            #checks if group does not - if true it will print out adding said user to the group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                #os.system(cmd)

if __name__ == '__main__':
    main()
