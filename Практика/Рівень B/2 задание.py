import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

Магнітура=float(input("Введіть бали: "))
if 2<= Магнітура<3:
    print("Землетрус за шкалой Ріхтера вважається микро")
elif 3<= Магнітура<4:
    print("Землетрус за шкалой Ріхтера вважається дуже слабким")
elif 4<= Магнітура<5:
    print("Землетрус за шкалой Ріхтера вважається слабким")
elif 5<= Магнітура<6:
    print("Землетрус за шкалой Ріхтера вважається легким")
elif 6<= Магнітура<7:
    print("Землетрус за шкалой Ріхтера вважається помірним")
elif 7<= Магнітура<8:
    print("Землетрус за шкалой Ріхтера вважається сильним")
elif 8<= Магнітура<9:
    print("Землетрус за шкалой Ріхтера вважається дуже сильним")
elif 9<= Магнітура<10:
    print("Землетрус за шкалой Ріхтера вважається великим")
elif Магнітура>=10:
    print("Землетрус за шкалой Ріхтера вважається рідкісно великим")