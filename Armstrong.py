# program:Armstrong number check
n=int(input("Enter a number:")) 
temp=n
sum1=0
digits=len(str(n))
while temp>0:
    digit=temp%10
    sum1=sum1+digit**digits
    temp=temp//10
if sum1==n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")