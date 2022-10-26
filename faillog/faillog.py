"""
It takes a line of text and a regular expression as input, and returns a match
:param line: the line of text to be searched
:param regex: The regular expression to use
:return: the match of the line with the regex
"""
#!/usr/bin/env python3

import re



def use_regex(line,regex):
    """
    It takes a line of text and a regular expression as input, and returns a match
    :param line: the line of text to be searched
    :param regex: The regular expression to use
    :return: the pattern.match(line)
    """
    pattern = re.compile(r''+ regex, re.IGNORECASE)
    return pattern.match(line)


def main():
    """
    get file to analyse et ouput, get the id in line matching regex
    """
    count = 0
    # get the file input and the name of the output file
    print("Entrez le path du fichier a scanner : ")
    readfile = input()
    print("Entrez le path du fichier result : ")
    writefile = input()
    regex_list = []
    print("Enter the regex you want to search (tap enter to stop adding regex):")
    boolea = False
    while boolea is False:
        print("enter the "+str(count)+" argument:")
        enter =input()
        regex_list.append(enter)
        if enter == "stop":
            boolea = True
        count+=1
    # Using readlines()
    inputfile = open(readfile, 'r',encoding='UTF-8')
    outputfile = open(writefile +'.csv', 'w',encoding='UTF-8')
    lines = inputfile.readlines()
    # Strips the newline character
    outputfile.writelines('failed id; regex \n')
    for line in lines:
        for regex in regex_list:
            if use_regex(line,regex):
                getidline = line.replace('"', "")
                getidline.replace('(', "")
                getidline.replace(')', "")
                getidline.replace('[', "")
                getidline.replace(']', "")
                lstnb = []
                for strnb in getidline.split():
                    try:
                        lstnb.append(int(strnb))
                    except ValueError:
                        pass
                if lstnb.__len__() != 0:
                    l_long = lstnb.__len__()
                    outputfile.writelines(str(lstnb[l_long-1])+";"+regex+"\n")
                else:
                    print("fail to retrieve id on regex :"+regex)
                    exit()
    print("Done! go see at "+writefile+" for the result")
    outputfile.close()

main()
