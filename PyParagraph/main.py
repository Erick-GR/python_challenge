import re

firstFile = "paragraph_1.txt"
secondFile = "paragraph_2.txt"
thirdFile = "paragraph_3.txt"

files = {"1" : firstFile, "2" : secondFile, "3" : thirdFile}

selection = input("What file do you want to analyze? [1,2,3]")

with open(files[selection], 'r', newline='') as p1:
    readText = p1.read()
    print(readText.split())
    print(re.split('(?<=[.!?])\n\n+', readText))
    w_count = len(readText.split())
    s_count = len(re.split('(?<=[.!?]) +|(?<=[.!?])\n\n+', readText))
    l_count = sum(len(w) for w in readText.split())

print(f"Total number of words: {w_count}")
print(f"Total number of sentences: {s_count}")
print(f"Average letter count: {l_count/w_count:.2f}")
print(f"Average sentence length: {w_count/s_count:.2f}")
