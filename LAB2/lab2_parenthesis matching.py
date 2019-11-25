from lab2_stack import Stack

################ CHANGE TEST HERE #####################

str = "(a+b-c*[d+e]/{f*(g+h)}"
# str = "[( a+b-c }*[d+e]/{f*(g+h)}"
# str = "(3+2)/{4**5}"


error = False
s = Stack()
count = [0,0,0,0,0,0]
length = len(str)
for i in range(0,length):
    if str[i] == "(" or str[i] == ")" or str[i] == "{" or str[i] == "}" or str[i] == "[" or str[i] == "]":
        s.push(str[i])
for i in range(0,s.size()):
    # print(s.item[i], end ="")
    if s.item[i] == "(":
        count[0]+=1
    elif s.item[i] == ")":
        count[1]+=1
    elif s.item[i] == "{":
        count[2]+=1
    elif s.item[i] == "}":
        count[3]+=1
    elif s.item[i] == "[":
        count[4]+=1
    elif s.item[i] == "]":
        count[5]+=1 

if count[0]!=count[1]: error = True
elif count[2]!=count[3]: error = True
elif count[4]!=count[5]: error = True
else : error = False

if error == True:
    print('MISMATCH')
else:
    if s.isEmpty == False:
        print('MISMATCH open paren. exceed')
    else:
        print('MATCH')


