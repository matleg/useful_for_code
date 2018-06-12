#! /usr/bin/python
# -*- coding: utf-8 -*-

import filecmp
import os
import sys
import time

cwd = os.getcwd()
print(cwd)
list_files = os.listdir(cwd)

old_stdout = sys.stdout  # save original stdout

# --------------------------- User input
# dir1 = os.path.abspath(os.path.realpath(os.path.join('C:','Users',...)))
dir1 = "C:\\Users\\mat\\Documents\\00001"
dir2 = "C:\\Users\\mat\\Documents\\00007"

directories_to_ignore = ['.svn', '.git', '.idea', 'docs']
files_to_ignore = ['.pyc', '.log']
write_command_for_compare = True

meld = "C:\\\\Program\ Files\ \(x86\)\\\\Meld\\\\Meld.exe "  # tool to compare files

star = "********************************************************************************\n"
# --------------------------- End User input

# --------------------------- Comparison, raw report
comparison = filecmp.dircmp(dir1, dir2)

# store differences in a file, in a python format
f = open('report_differences.txt', 'w')
sys.stdout = f  # changing system output to the file
comparison.report_full_closure()
f.close()

sys.stdout = old_stdout  # back to original system output

# read the differences to process them later
with open('report_differences.txt', 'r') as f:
    rep = f.readlines()
# --------------------------- End of comparison, raw report
for i in rep:
    print(i)
# --------------------------- Process differences
summa = []
to_pass = False
for ll in range(len(rep)):
    # get lines starting by "Only in..."
    if "Only in " in rep[ll]:
        # flag for ignoring directories 
        for directo in directories_to_ignore:
            if directo in rep[ll]:
                to_pass = True
                break
        if to_pass:
            to_pass = False
            continue
        summa.append(rep[ll])
        summa.append('\n')

    if "Differing files :" in rep[ll]:
        # get lines starting by "diff" and "Differing"
        ii = ll
        while "diff " not in rep[ii]:
            ii -= 1
        # flag for ignoring directories
        for directo in directories_to_ignore:
            if directo in rep[ii]:
                to_pass = True
                break
        if to_pass:
            to_pass = False
            continue
        summa.append(rep[ii])
        summa.append(rep[ll])
        summa.append('\n')

# process and write only interesting lines in the file
cdirs = 0
cfiles = 0
with open('report_differences.txt', 'w') as f:
    f.write(str(time.ctime()) + "\n")  # date time
    f.write(dir1 + "\n")
    f.write('vs.\n')
    f.write(dir2 + "\n\n\n")

    for i in range(len(summa)):
        if "Only" in summa[i]:
            _, a, b = summa[i].split(":")  # a:adress, b:list of files
            f.write(star)
            f.write("Only in C:" + a.replace("\\", "\\\\") + ":\n")  # a : "Only in ..."
            cdirs += 1
            f.write(star)
            for l in b.split("'"):  # b : "['file1,'file2'..]"
                if ("[" not in l) and ("]" not in l) and ("," not in l):
                    # write only file names
                    # flag for ignoring files
                    for fti in files_to_ignore:
                        if fti in l:
                            to_pass = True
                            break
                    if to_pass:
                        to_pass = False
                        continue
                    f.write(l + "\n")  # str(l)
                    cfiles += 1
            f.write('\n')

        if "Differing files :" in summa[i]:
            # f.write(star)
            phra = summa[i - 1].split()  # 'diff' 'path1' 'path2'
            a, b = summa[i].split(":")  # a: adress, b:list of files
            # f.write(summa[i-1])  # diff...
            listfiles = ""
            for l in b.split("'"):
                if ("[" not in l) and ("]" not in l) and ("," not in l):
                    # flag for files to ignore
                    for fti in files_to_ignore:
                        if fti in l:
                            to_pass = True
                            break
                    if to_pass:
                        to_pass = False
                        continue
                    listfiles += l + "\n"
                    cfiles += 1

            f.write(star + "Differing files between " + phra[1] + " and "
                    + phra[2] + "\n" + star + listfiles[:-1] + "\n" + star)  # [-2] to remove ", "
            cdirs += 1

            if write_command_for_compare:
                for l in b.split("'"):
                    if ("[" not in l) and ("]" not in l) and ("," not in l):
                        # flag for files to ignore
                        for fti in files_to_ignore:
                            if fti in l:
                                to_pass = True
                                break
                        if to_pass:
                            to_pass = False
                            continue
                        toWrite = ("nohup " + meld +  # all the \\\ for windobws
                                   phra[1].replace("\\", "\\\\") + "\\\\" + l + " " +
                                   phra[2].replace("\\", "\\\\") + "\\\\" + l + " &" + "\n")
                        f.write(toWrite)
            f.write('\n')

    summary = 'Total of ' + str(cfiles) + ' differences in ' + str(cdirs) + ' directories.'
    f.write(summary)

# --------------------------- End of Process differences

# --------------------------- Process identical
cdirs = 0
cfiles = 0
summa = []
to_pass = False
for ll in range(len(rep)):
    # get lines starting by "Identical files :"
    if "Identical files :" in rep[ll]:
        # flag for ignoring directories 
        ii = ll
        while "diff " not in rep[ii]:
            ii -= 1
        # flag for ignoring directories
        for directo in directories_to_ignore:
            if directo in rep[ii]:
                to_pass = True
                break
        if to_pass:
            to_pass = False
            continue
        summa.append(rep[ii])
        summa.append(rep[ll])
        summa.append('\n')

# process and write only interesting lines in the file
with open('report_identical.txt', 'w') as f:
    f.write(str(time.ctime()) + "\n")  # date time
    f.write(dir1 + "\n")
    f.write('vs.\n')
    f.write(dir2 + "\n\n\n")

    for i in range(len(summa)):
        if "Identical files :" in summa[i]:
            # f.write(star)
            phra = summa[i - 1].split()  # 'diff' 'path1' 'path2'
            a, b = summa[i].split(":")  # a: adress, b:list of files
            # f.write(summa[i-1])  # diff...
            listfiles = ""
            for l in b.split("'"):
                if ("[" not in l) and ("]" not in l) and ("," not in l):
                    # flag for files to ignore
                    for fti in files_to_ignore:
                        if fti in l:
                            to_pass = True
                            break
                    if to_pass:
                        to_pass = False
                        continue
                    listfiles += l + "\n"
                    cfiles += 1

            f.write(star + "Identical files between " + phra[1] + " and "
                    + phra[2] + "\n" + star + listfiles[:-1] + "\n\n")  # [-2] to remove ", "
            cdirs += 1
    summary = 'Total of ' + str(cfiles) + ' identical files in ' + str(cdirs) + ' directories.'
    f.write(summary)
