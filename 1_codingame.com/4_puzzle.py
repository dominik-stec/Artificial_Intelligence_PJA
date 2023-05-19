"""
author: Dominik Stec,
index:  s12623,
email:  s12623@pja.edu.pl

source link:
https://www.codingame.com/ide/puzzle/mime-type
"""

import sys
import math
from collections import Counter
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
ret_mime = ''
extension_list = []
mime_list = []
fname_split = []

for i in range(n):
        # ext: file extension
        # mt: MIME type.
    ext, mt = input().split()
    
    extension_list.append(ext.lower()) # lower() here
    mime_list.append(mt)

for i in range(q):
    fname = input()  # One file name per line.
    
    fname = fname.lower()

    fname_split = []

    # block_multiply_dot = False
    # multiplicates = Counter(name)
    # multi = [k for k,v in multiplicates.items() if v>1]
    # if '.' in multi:
    #     block_multiply_dot = True

    # split and correct size of list
    fname_len = len(fname)
    fname_split = fname.rsplit('.')
    
    # if len(fname_split) == 1:
    #     fname_split.append(fname_split[0])
    
    #big test
    #name_len = len(fname_split[1])

    #if len(name_split) > 2 and '.' in name_split:
    #   block_multiply_dot = False

    # string without dots
    fname_split_string = ''
    for i in fname_split:
        fname_split_string = fname_split_string + i
    
    #print(fname_split_string + " " + str(fname_len), file=sys.stderr, flush=True)

    # if no dot
    if not '.' in fname:
        ret_mime = ret_mime + 'UNKNOWN' +'\n'
        continue

    # # if no dot alternative
    # if len(fname_split_string) == (fname_len):
    #     ret_mime = ret_mime + 'UNKNOWN' +'\n'
    #     continue


    # for one dot
    # (fname_split[-1] in extension_list[:]) and 
    if (len(fname_split_string) == (fname_len - 1)):
        # if dot is last
        if '' == fname_split[-1] and not '' == fname_split[0]:
            ret_mime = ret_mime + 'UNKNOWN' +'\n'
            continue
        # if dot is first
        if '' == fname_split[0] and not '' == fname_split[-1]:
            try:
                extension_name = fname_split[-1]
                extension_idx = extension_list.index(extension_name)
                ret_mime = ret_mime + mime_list[extension_idx] + '\n'
                continue
            except:
                ret_mime = ret_mime + 'UNKNOWN' +'\n'
                continue
        # dot in the middle
        if '.' in fname and not '' == fname_split[-1] and not '' == fname_split[0]:
            try:
                extension_name = fname_split[-1]
                extension_idx = extension_list.index(extension_name)
                ret_mime = ret_mime + mime_list[extension_idx] + '\n'
                continue
            except:
                ret_mime = ret_mime + 'UNKNOWN' +'\n'
                continue
    # if extension none in set
    #elif (len(fname_split_string) == (fname_len - 1)):
        else:
            ret_mime = ret_mime + 'UNKNOWN' +'\n'
            continue
    
    #print(len(fname_split_string) + " test ", file=sys.stderr, flush=True)

    # minimum 2 dots
    if len(fname_split_string) < (fname_len - 1):
        # if one of dots is last
        if '' == fname_split[-1]:
            ret_mime = ret_mime + 'UNKNOWN' +'\n'
            continue
        # if one of dots is first
        if '' == fname_split[0]:
            ret_mime = ret_mime + 'UNKNOWN' +'\n'
            continue
        # if dots are neighbors in the middle
        if '' in fname_split[:] and not '' in fname_split[0] and not '' in fname_split:
            try:
                extension_name = fname_split[-1]
                extension_idx = extension_list.index(extension_name)
                ret_mime = ret_mime + mime_list[extension_idx] + '\n'
                continue
            except:
                ret_mime = ret_mime + 'UNKNOWN' +'\n'
                continue
    else:
        ret_mime = ret_mime + 'UNKNOWN' +'\n'
        continue
        # if dots are not neighor but are in the middle
    #     counter = 0
    #     for i in fname_split[1:-1]:
    #         if i == '':
    #             counter = counter + 1
    #     if counter > 1:
    #         ret_mime = ret_mime + 'UNKNOWN' +'\n'
    #         print(counter + " test ", file=sys.stderr, flush=True)
    #         continue
    # else:
    #     ret_mime = ret_mime + 'UNKNOWN' +'\n'
    #     continue


        # if fname_split_string[-1] == '.':
        #     ret_mime = ret_mime + 'UNKNOWN' +'\n'
        #     continue     
        # resume_loop = True  
        # if len(fname_split) > 2:

            # for i in range(0, len(fname_split)):
            #     if fname[i] == '.' and fname[i+1] == '.':
            #         print('test', file=sys.stderr, flush=True)
            #         extension_name = fname_split[-1]
            #         extension_idx = extension_list.index(extension_name)
            #         ret_mime = ret_mime + mime_list[extension_idx] + '\n'
            #         resume_loop = False
            #         break 
            # if resume_loop:               
            #     ret_mime = ret_mime + 'UNKNOWN' +'\n'
            #     continue
            # continue
        

    #     extension_name = fname_split[1]
    #     extension_idx = extension_list.index(extension_name)
    #     ret_mime = ret_mime + mime_list[extension_idx] + '\n'
    

    # elif len(name_split) >= 3:
    #     length = len(name_split)
    #     length = length - 1
    #     if '' in name_split:
    #         try:
    #             idx = ext_list.index(name_split[length])
    #             miret_mimeme = ret_mime + mt_list[1] + '\n'
    #         except ValueError:
    #             ret_mime = ret_mime + 'UNKNOWN' +'\n'
    #             continue
    #     else:
    #         ret_mime = ret_mime + 'UNKNOWN' +'\n'
    #         continue
    #     continue
    # else:
    #     ret_mime = ret_mime + 'UNKNOWN' +'\n'
   
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
print(ret_mime)
