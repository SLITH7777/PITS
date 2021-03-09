per = int(input("Введите число"))
neSumma = ("не нашлось")
for p in range(2,per):
    if per%p == 0:
      neSumma = "нашлось"



if neSumma == "нашлось":
   print("cocтавное число")
if neSumma == "не нашлось":
   print("простое число")
  
