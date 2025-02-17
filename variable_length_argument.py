
def sum(*nums):
    sum=0
    (sum:=sum+num for num in nums)
    print(sum)

sum(10,20)
sum(10, 20, 30)
sum(10, 20, 30, 40)