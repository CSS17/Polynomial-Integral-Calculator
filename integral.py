#Polynomial Integral Calculator
#Author Omer Faruk Ucer
step_number=0
point_value_cal=[]
coefficient=[]
point_values=[]
sum=0
result=0
polynomial_degree=int(input("Kaçıncı Dereceden bir Polinomun alanını hesaplayacaksınız?"))
for i in range(polynomial_degree+1):
    if i==0:
        coefficient.append(int(input("Sabit elemanı giriniz:")))
    else:
        coefficient.append(int(input(str(i)+".dereceden elemanın katsayısını giriniz:")))

start=int(input("İntegral Başlangıcı:"))
end=int(input("İntegral end:"))
if end>=start:
    point_number=(end-start)/0.5
else:
    point_number=(start-end)/0.5

lenght=len(coefficient)
sum=0
if end>=start:
    while start<=end:
        for i in range(lenght):
            sum+=(coefficient[i])*start**i
        point_values.append(sum)
        sum=0
        start+=0.25
else:
    while end<=start:
        for i in range(lenght):
            sum+=(coefficient[i])*end**i
        point_values.append(sum)
        sum=0
        end+=0.25            
print(point_values)  

for i in range(len(point_values)):
    if i==0 or i==len(point_values)-1:       
       print("Beginning or Ending number",str(point_values[i]))
       result+=point_values[i] 
    elif i%2==0:
        print("middle number",str(point_values[i]))
        result+=2*point_values[i]
    else:
        print("intermediate number",str(point_values[i]))
        result+=4*point_values[i]
print(result)    
if start>=end:   
    result=result*(0.5/6)
else:
    result=result*(0.5/6)*-1
print(result)





