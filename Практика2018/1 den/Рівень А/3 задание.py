import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

тиск=int(input("Введіть тиск у паскалях :"))
килотиск=тиск/1000
тиск3=килотиск* 0.145038
тиск4=килотиск*7.5006375
тиск5=килотиск*0.00986923266716
print("Еквівалентний тиск у фунтах на квадратний дюйм: ",тиск3,"тд/дм**2")
print("Еквівалентний тиск у міліметрах ртутного стовпчика: ",тиск4,"мм рт.ст.")
print("Еквівалентний тиск у атмосферах: ",тиск5,"физ. атмосфер")