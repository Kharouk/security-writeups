#!/usr/bin/env python3
import sys
num = sys.argv[1:]
print(num)
print("".join([chr(int(x,int(8))) for x in num]))