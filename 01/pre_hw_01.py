#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
name=raw_input("Please enter your name:")
print("Hi "+ name)
print("Welcome to play the guess number game...")

if name.lower()=="eric":
    print "Hi" + name + ", how are you ?"
else:
    print "Who are you ? get out!"

while True:
    print("Hi "+ name + ", are you ready ?")
    time.sleep(0.5)