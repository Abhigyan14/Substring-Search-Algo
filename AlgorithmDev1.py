## Input Genomic FASTA File
inputFile = 'genomic.fna'

# Input File Formatting (Removing of "\n" and headers)
# Reference to (https://stackoverflow.com/questions/11968998/remove-lines-that-contain-certain-string)
tempFile = 'tempGenomic.txt'
removeChar = ['>']

with open(inputFile) as oldfile, open(tempFile, 'w') as newfile:
    for line in oldfile:
        if not any(removeChar in line for removeChar in removeChar):
            line = line.replace('\n', '')
            newfile.write(line)

a = open(tempFile, 'r')
a = a.read()

# Input Sequence
inputSequence = input("Enter sequence: ")

# Brute Force Method
i = 0
j = 0
# cnt_Brute counts the number of comparisons for Brute Force
cnt_Brute = 0
occurOnceFlag = 0  # To check if there is at least once occurrence
while i < len(a):
    # To check for the first character of the input sequence & file
    cnt_Brute += 1
    if a[i] == inputSequence[j]:
        # Increase the index of the sequence to check for the next character
        j = j + 1
    else:
        cnt_Brute += 1
        if j > 0:
            i = i - j
        # To re-check for the input sequence
        j = 0
    cnt_Brute += 1
    if j == len(inputSequence):
        # Bringing the index of input sequence back to 0 to check for other match sequence in the file
        j = 0
        print("(BRUTE FORCE)There is an occurrence at position:", ((i + 2) - len(inputSequence)))
        # i is incremented to increase the position of the character in the Genome file
        occurOnceFlag = 1

    if (i == len(a) - 1 and occurOnceFlag == 0):  # When there is COMPLETELY no occurence
        print("(BRUTE FORCE)There is no occurrence for your input: " + inputSequence)

    i += 1

# KMP
i,j=1,0
l=[]
l.append(0)
# cnt_KMP counts the number of comparisons for KMP
cnt_KMP=0
while i<len(inputSequence):
    cnt_KMP+=1
    if inputSequence[i]==inputSequence[j]:
        l.append(1+j)
        i+=1
        j+=1
    else:
        cnt_KMP+=1
        if j!=0:
            j=l[j-1]
        else:
            l.append(0)
            i+=1
# Re-initailising i and j
i = 0
j = 0
occurOnceFlag=0 #To check if there is at least once occurence

# Main KMP algorithm

while (i < len(a)):
    cnt_KMP+=1
    if a[i] == inputSequence[j]:
        i += 1
        j += 1
        cnt_KMP+=1
        if j == len(inputSequence):
            print("(KMP)There is an occurrence at position:", (i - j + 1))
            i = i + len(inputSequence) - 1
            occurOnceFlag=1
            j = l[j - 1]
    elif i < len(a) and inputSequence[j] != a[i]:
        cnt_KMP+=1
        if j != 0:
            j = l[j - 1]
        else:
            i += 1
#When there is COMPLETELY no occurence
if(i == len(a) and occurOnceFlag == 0):
    print("(KMP)There is no occurence for your input: " + inputSequence)

# Boyer Moore
# To calculate the maximum number of repetitions in inputSequence
maximum = 1
# cnt_Boyer counts the number of comparisons for Boyer Moore
cnt_Boyer = 0
for k in range(0, len(inputSequence)):
    cnt = 1
    while (k + 1 < len(inputSequence) and inputSequence[k] == inputSequence[k + 1]):
        cnt += 1
        k += 1
        cnt_Boyer += 1
    if cnt > maximum:
        maximum = cnt

Count_A1 = 0
Count_A2 = 0
Count_G1 = 0
Count_G2 = 0
Count_T1 = 0
Count_T2 = 0
Count_C1 = 0
Count_C2 = 0
star = len(inputSequence)
l = []

# Making the prerequisite table for Boyer Moore

for i in range(0, len(inputSequence)):
    cnt_Boyer += 1
    off = len(inputSequence) - i - maximum
    if inputSequence[i] == 'A':
        Count_A1 = max(1, off)
        Count_A2 += 1
    elif inputSequence[i] == 'G':
        Count_G1 = max(1, off)
        Count_G2 += 1
    elif inputSequence[i] == 'T':
        Count_T1 = max(1, off)
        Count_T2 += 1
    elif inputSequence[i] == 'C':
        Count_C1 = max(1, off)
        Count_C2 += 1
if Count_A2 == 0:
    l.append(0)
else:
    l.append(Count_A1)
if Count_G2 == 0:
    l.append(0)
else:
    l.append(Count_G1)
if Count_T2 == 0:
    l.append(0)
else:
    l.append(Count_T1)
if Count_C2 == 0:
    l.append(0)
else:
    l.append(Count_C1)
l.append(star)
i = 0

# %%

i = 0
occurOnceFlag = 0  # To check if there is at least once occurence

# Main code for Boyer Moore

while i < len(a) - len(inputSequence) + 1:
    j = len(inputSequence) - 1
    while j >= 0:
        cnt_Boyer += 1
        if (inputSequence[j] == a[i + j]):
            j -= 1
            if j == -1:
                print("(BOYAR MOORE)There is an occurrence at position: ", i + 1)
                occurOnceFlag = 1
                i += len(inputSequence)
        else:
            cnt_Boyer += 1
            if a[i + j] == 'A' and Count_A1 != 0:
                i += (l[0])
            elif a[i + j] == 'G' and Count_G1 != 0:
                i += (l[1])
            elif a[i + j] == 'T' and Count_T1 != 0:
                i += (l[2])
            elif a[i + j] == 'C' and Count_C1 != 0:
                i += (l[3])
            else:
                i += (l[4])
            break
if (occurOnceFlag == 0):
    print("(BOYAR MOORE)There is no occurence for your input: " + inputSequence)