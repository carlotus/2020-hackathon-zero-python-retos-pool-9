#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    #
    #
    
    #
    #
    password = ""
    print (random.choices(string.ascii_letters)[0])

    for index in range(passLen-4):
        password = password + random.choices(string.ascii_letters)[0]
    password = password + random.choices(string.ascii_uppercase)[0]
    password = password + random.choices(string.digits)[0]
    password = password + random.choices(string.punctuation)[0]
    password = password + random.choices(string.ascii_lowercase)[0]


    print (password)
    return password

RandomPasswordGenerator()
