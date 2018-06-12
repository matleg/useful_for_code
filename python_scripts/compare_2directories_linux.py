import os
import filecmp
import sys
import time

cwd = os.getcwd()
list_files = os.listdir(cwd)

old_stdout = sys.stdout  # save original stdout

dir1 = "/path/to/dir1"
dir2 = "/path/to/dir2"

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

star = "********************************************************************************\n"
summa = []
for ll in range(len(rep)):
    # get lines starting by "Only in..."
    if "Only in " in rep[ll]:
        summa.append(rep[ll])
        summa.append('\n')

    if "Differing files :" in rep[ll]:
        # get lines starting by "diff" and "Differing"
        ii = ll
        while "diff " not in rep[ii]:
            ii -= 1
        summa.append(rep[ii])
        summa.append(rep[ll])
        summa.append('\n')

# process and write only interesting lines in the file
with open('report_differences.txt', 'w') as f:
    f.write(str(time.ctime()) + "\n")  # date time
    f.write(dir1 + "\n")
    f.write('vs.\n')
    f.write(dir2 + "\n\n\n")

    for i in range(len(summa)):
        if "Only" in summa[i]:
            a, b = summa[i].split(":")
            f.write(star)
            f.write(a + ":\n")  # a : "Only in ..."
            f.write(star)
            for l in b.split("'"):  # b : "['file1,'file2'..]"
                if (("[" not in l) and ("]" not in l) and
                        ("," not in l)):
                    # write only file names
                    f.write(str(l) + "\n")
            f.write('\n')

        if "Differing files :" in summa[i]:
            f.write(star)
            phra = summa[i - 1].split()  # 'diff' 'path1' 'path2'
            a, b = summa[i].split(":")
            f.write(summa[i - 1])  # diff...
            listfiles = ""
            for l in b.split("'"):
                if (("[" not in l) and ("]" not in l) and
                        ("," not in l)):
                    #                    listfiles += l+", "
                    listfiles += l + "\n"
            #            f.write("Differing files :"+listfiles[:-2]+"\n") # [-2] to remove ", "
            # print ("listfiles = "+str(listfiles)+"End")

            f.write(star + "Differing files :\n" + star + listfiles[:-1] + "\n" + star)  # [-2] to remove ", "

            for l in b.split("'"):
                if (("[" not in l) and ("]" not in l) and
                        ("," not in l)):
                    # write shell command to copy
                    #                    toWrite=(l+"\n"+"tkdiff "+phra[1]+ "/"+l+
                    toWrite = ("tkdiff " + phra[1] + "/" + l +
                               " " + phra[2] + "/" + l + " &" + "\n")
                    f.write(toWrite)
            f.write('\n')
