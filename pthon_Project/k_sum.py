# x={1,2, 3, 4, 5, 6}
# y=len(x)
# print("y:", y)
# for i in range(y):
#     for j in range(y):
#       for k in range(i):
#        print(j, end=" ")
#     print("x")
    # print(i,'x')
# k=2
# for i in x:
#     for j in range(i):
#      print(j,i)
#     print(" ")
x= [1, 20, 4, 53, 6, 7, 8, 9]
n= len(x)
print(n)
k= 3
current_sum=0
for i in range(n-k+1 ):
    m=0
    for j in range(i , k+i):
        m= m+x[j]
    print( m)
    if current_sum<m:
      current_sum=m
print("currentsum :", current_sum)
    
    # break
