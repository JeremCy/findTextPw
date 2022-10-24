#!/usr/bin/env python3
import re

def use_regex(line):
    pattern = re.compile(r'^\[[^\]]*] -(\s+([a-zA-Z]+\s+)+)"Document" with identifier "[0-9]+" has not been modified\.$', re.IGNORECASE)
    return pattern.match(line)

def main():
    count = 0
    # get the file input and the name of the output file
    print("Entrez le path du fichier a scanner : ")
    readfile = input()
    print("Entrez le path du fichier resulte : ")
    writefile = input()

    # Using readlines()
    inputfile = open(readfile, 'r')
    outputfile = open(writefile +'.csv', 'w')
    lines = inputfile.readlines()
  
    # Strips the newline character
    outputfile.writelines('failed id \n')
    for line in lines:
        if use_regex(line):
            l = [""]
            for t in line.split():
                l.append(t)
            l.reverse()
            outputfile.writelines(l[4]+'\n')
        count +=1
    outputfile.close()

main()