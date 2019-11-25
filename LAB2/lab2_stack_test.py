from lab2_stack import Stack
name = ['s','e','v','e','n']
s = Stack()
for i in range(0,len(name)):
    s.push(name[i])

print(s.item)
print(s.size())
print(s.isEmpty())
print(s.peek())
print(s.item)

for i in range(0,s.size()):
    s.pop()
    if(s.isEmpty()==True):
        print("Stack is empty NOW")

print(s.item)