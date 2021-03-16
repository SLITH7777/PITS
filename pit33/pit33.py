chislo = int(input("введите число"))
svinka = 1
korova = 0
korsvin = 0
while(chislo != "exit"):
  for f in range(1,chislo):
     korsvin = korova + svinka
     korova = svinka
     svinka = korsvin
     print(korsvin)
  chislo = int(input("введите число"))
  svinka = 1
  korova = 0
  korsvin = 0
print("uuuu")
