number = int(raw_input("Input some number: "))

if int(number) % 2 == 0:
     print number, "is Even Number"
else:
    print number, "is Odd Number"


divFactor = []

for i in range(1,number+1):
    if number % i == 0:
        divFactor.append(i)

print "Division Factor of",number,"is =",divFactor

if len(divFactor) == 2:
    print number, "is Prime."
else:
    print number, "is NOT Prima"



