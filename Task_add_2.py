year=int(input("Введите год "))

if (year%4==0 and year%100==0 and year%400==0) or (year%4==0 and year%100!=0):
    print("Этот год високосный")

else:
    print("Этот год не високосный")