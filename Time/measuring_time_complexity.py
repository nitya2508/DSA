import time

start=time.time()

# for i in range(1,101):
#     print(i)
i=1
while i<101:
    print(i)
    i+=1
print(time.time()-start)

# using big o notation

A = [1,2,3,4,5]
sum = 0
for i in A:
    sum += i
print(sum)

product = 1
for i in A:
    product *= i
print(product)

# time complexity = O(n) + O(n) = O(n+n) = O(2n) = O(n)= linear

A = [1,2,3,4,5]

for i in A:
    for j in A:
        print(f'[{i},{j}]')

# time complexity = O(n) * O(n) = O(n*n) = O(n^2) = quadratic

def int_to_str(i):
    digits ='0123456789'
    if i ==0:
        return '0'
    result=''
    while i>0:
        result = digits[i%10]+result
        i=i//10 #integer division by 10 result will be a whole number
    return result
    
print(int_to_str(12345))

# for increase in number of digits in input the loop is executing 1 time more so 1=1iteration, 12=2iteration,
# 123=3iteration, 1234=4iteration and so on time complexity is O(log n) = logarithmic

# if division is involved then there is a possibility that complexity will be log n