#!/bin/python3

import math
import os
import random
import re
import sys


n = input()
try:
    print(int(n))
except ValueError:
    print("Bad String")