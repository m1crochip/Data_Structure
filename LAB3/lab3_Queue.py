from class_Queue import Queue

# print(series.item[0])

series = Queue()
series.Enqueue(50)
series.Enqueue(5)
series.Enqueue(6)
series.Enqueue(1)
series.Enqueue(8)
series.Enqueue(3)

def encode(Queue):
    length = Queue.size()
    for i in range(0,length):
        if ord(Queue.item[i])!=32:
            if ord(Queue.item[i])+series.get() in range(91,96) or ord(Queue.item[i])+series.get() in range(123,127):
                Queue.Enqueue(chr(ord(Queue.item[i])+series.get()-26))
                temp = series.get()
                series.Dequeue()
                series.Enqueue(temp)
            else:
                Queue.Enqueue(chr(ord(Queue.item[i])+series.get()))
                temp = series.get()
                series.Dequeue()
                series.Enqueue(temp) 
        else:
            Queue.Enqueue(chr(32))
 
    for i in range(0,length):
        Queue.Dequeue()
    for i in range(0,series.size()):
        series.Dequeue()
    series.Enqueue(2)
    series.Enqueue(5)
    series.Enqueue(6)
    series.Enqueue(1)
    series.Enqueue(8)
    series.Enqueue(3)
    

def decode(Queue):
    length = Queue.size()
    for i in range(0,length):
        if ord(Queue.item[i])!=32:
            if ord(Queue.item[i])+series.get() < 65 or ord(Queue.item[i])+series.get() in range(91,96):
                Queue.Enqueue(chr(ord(Queue.item[i])+26+series.get()))
                temp = series.get()
                series.Dequeue()
                series.Enqueue(temp)
            else:
                Queue.Enqueue(chr(ord(Queue.item[i])-series.get()))
                temp = series.get()
                series.Dequeue()
                series.Enqueue(temp) 
        else:
            Queue.Enqueue(chr(32))
 
    for i in range(0,length):
        Queue.Dequeue()

    for i in range(0,series.size()):
        series.Dequeue()
    series.Enqueue(2)
    series.Enqueue(5)
    series.Enqueue(6)
    series.Enqueue(1)
    series.Enqueue(8)
    series.Enqueue(3)
                
INPUT = 'I love Python'

code = Queue()
for i in range(0,len(INPUT)):
    code.Enqueue(INPUT[i])

print(code.show())
encode(code)
print(code.show())
# decode(code)
# print(code.show())
# encode(code)
# print(code.show())



