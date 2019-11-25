
def encode(CHA, x):
    if type(CHA) == str:
        if x == 0:
           temp = ord(CHA) + 2
           return temp
        elif x == 1:
            temp = ord(CHA) + 5
            return temp
        elif x == 2:
            temp = ord(CHA) + 6
            return temp
        elif x == 3:
            temp = ord(CHA) + 1
            return temp
        elif x == 4:
            temp = ord(CHA) + 8
            return temp
        elif x == 5:
            temp = ord(CHA) + 3
            return temp

def decode(CHA, y):
    if type(CHA) == str:
        if y == 0:
           temp = ord(CHA) - 2
           return temp
        elif y == 1:
            temp = ord(CHA) - 5
            return temp
        elif y == 2:
            temp = ord(CHA) - 6
            return temp
        elif y == 3:
            temp = ord(CHA) - 1
            return temp
        elif y == 4:
            temp = ord(CHA) - 8
            return temp
        elif y == 5:
            temp = ord(CHA) - 3
            return temp

# INPUT = input('Enter your code for <Caesar encode> :')
INPUT = 'I love Python'

length = len(INPUT)
word = []

for i in range(0,length):
    word.append(INPUT[i])

print(word)

code = 0
for i in range(0,length):
    if word[i] != ' ':
        if encode(word[i],code) in range(65,90):
            word[i] = chr(encode(word[i],code))
        elif encode(word[i],code) in range(91,96):
            word[i] = chr(encode(word[i],code)-26)
        elif encode(word[i],code) in range(97,122):
            word[i] = chr(encode(word[i],code))
        elif encode(word[i],code) in range(123,127):
            word[i] = chr(encode(word[i],code)-26)

        if code != 5:
            code = code + 1
        else:
            code = 0

print("")
print("ENCODE :")   
print(word)

for i in range(0,length):
    if word[i] != ' ':
        if decode(word[i],code) in range(65,90):
            word[i] = chr(decode(word[i],code))
        elif decode(word[i],code) in range(91,96):
            word[i] = chr(decode(word[i],code)+26)
        elif decode(word[i],code) in range(97,122):
            word[i] = chr(decode(word[i],code))
        elif decode(word[i],code) in range(123,127):
            word[i] = chr(decode(word[i],code)+26)

        if code != 5:
            code = code + 1
        else:
            code = 0
print("")
print("DECODE :")   
print(word)



