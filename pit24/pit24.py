delo = input("введите математическое действие: ")
while delo != "exit":
    
    chi1 = int(input("введите число: "))
    chi2 = int(input("ведите число: "))
    if delo == "+":
       print(chi1 + chi2)
    if delo == "-":
       print(chi1 - chi2)
    if delo == "/":
       print(chi1/chi2)
    if delo == "*":
       print(chi1*chi2)
    delo = input("введите математическое действие: ")
print("bye")
    
    
