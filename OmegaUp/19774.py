initial=input()
count=int(input())
array=[]
for i in range(count):
    array.append(input())
for i in array:
    if (i[0].lower()==initial.lower()):
        print(i+"\n")