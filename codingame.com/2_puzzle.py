import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
word = ''

for i in range(h):
    row = input()

    if t == 'E':
        l_idx = 4 * l
        word = word + row[l_idx : l_idx + l] + '\n' 
    
    if t == 'MANHATTAN' or t.upper() == 'MANHATTAN':
        idx_m = 12 * l
        idx_a = 0
        idx_n = 13 * l
        idx_h = 7 * l
        idx_t = 19 * l

        word = word + row[idx_m : idx_m + l] + row[idx_a : idx_a + l] + row[idx_n : idx_n + l] + row[idx_h : idx_h + l] + row[idx_a : idx_a + l] + row[idx_t : idx_t + l] + row[idx_t : idx_t + l] + row[idx_a : idx_a + l] + row[idx_n : idx_n + l] + '\n' 

    if '@' in t:
        idx_m = 12 * l
        idx_a = 26 * l
        idx_n = 13 * l
        idx_h = 7 * l
        idx_t = 19 * l

        word = word + row[idx_m : idx_m + l] + row[idx_a : idx_a + l] + row[idx_n : idx_n + l] + row[idx_h : idx_h + l] + row[idx_a : idx_a + l] + row[idx_t : idx_t + l] + row[idx_t : idx_t + l] + row[idx_a : idx_a + l] + row[idx_n : idx_n + l] + '\n' 

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(word)
