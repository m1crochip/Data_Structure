def factorial(n):
    for i in range(1,n):
        n = n * i
        i+=1
    return n

def multiples_of_3_and_5(n):
    sum = 0
    for i in range(1,n):
        if i%3==0 or i%5==0:
            #print(i)
            sum+=i
        i+=1
    return sum

def integer_right_triangles(p):
    ans = []
    for a in range(1,p):
        for b in range(a,p):
            c = p-a-b
            if c<a or c<b:
                break
            if c*c == a*a + b*b:
                ans.append((a,b,c))
    return ans


def line(s):
    ans = ''
    for i in range(1,len(s)):
        ans = s[i]+ans
    ans = ans + s
    ans = '.'.join(ans)
    ans = ans
    return ans

def gen_pattern(c):
    n = (2*len(c)-1)+(2*len(c)-2)
    mid = line(c)+'\n'
    for i in range(1,len(c)):
        a = line(c[i:len(c)])
        a = a.center(n,'.')
        a = a + '\n'
        mid = a + mid + a
    return mid
    

#print(factorial(int(input('Enter number <4.1> : '))))
#print(multiples_of_3_and_5(int(input('Enter number <4.2> : '))))
#print(integer_right_triangles(int(input('Enter number <4.3> : '))))
print(gen_pattern(str(input('Enter character <4.4> : '))))
