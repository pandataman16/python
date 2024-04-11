num=int(input("enter the number"))
temp=num
result=0
lenth=len(str(num))
while(temp>0):
    lastdigit=temp%10
    result=result+lastdigit**lenth
    temp=temp//10
if(result==num):
    print("armstrong")
else:
    ("not armstrong")