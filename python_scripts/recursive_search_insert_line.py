#! /usr/bin/python
# adds sheebang and coding at the beginning of each python file
# os.walk is also a good example of generator

import os

cwd = os.getcwd()
print(cwd)

for root, dirnames, filenames in os.walk(cwd):
    print("root = " + str(root))
    print("dirnames = " + str(dirnames))
    for filename in filenames:
        if filename.endswith(".py"):
            print(" --- " + str(filename))
            os.chdir(root)
            # with open(filename, 'r+') as f:
            #         content = f.read()
            #         f.seek(0)
            #         f.write("""#! /usr/bin/python \n# -*- coding: utf-8 -*- \n""" + content)
