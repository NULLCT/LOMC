#!/usr/bin/env python3

import subprocess

for i in range(1340):
    print(i)
    filename = "data/" + str(i) + ".py"
    print("cat " + filename + " | yapf > " + filename)
    subprocess.check_output("cat " + filename + " | yapf > " + filename, shell=True)
