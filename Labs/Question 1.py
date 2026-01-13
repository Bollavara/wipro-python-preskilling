for i in range(1,21):
    print(i)
#filter
n=[1,2,3,4,5,6,7,8,9,10]
even=filter(lambda x:x%2==0,n)
for num in even:
    print(num)
#map & filter
y=filter(lambda x:x%2==0,n) #Even numbers
z=map(lambda x:x*x,y) #Square numbers
for num in z:
    print(num)

#sum_of_squares=reduce(lambda x,y:x+y, squared_numbers)
#print(sum_of_squares)
#using enumerate() to print index and value of the final result list
#a=[1,2,3,4]
#for index, value in
#enumerate(a):
 #   print(index,value)



