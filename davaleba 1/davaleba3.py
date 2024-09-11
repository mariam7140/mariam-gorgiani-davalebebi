# გვერდი a ჩაწერა
# გვერდი b ჩაწერა
# გვერდი c ჩაწერა
# პერიმეტრი a+b+c
# ჰერონის ფორმულა area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

a = int(input("please write length of triangle side a: "))
b = int(input("please write length of triangle side b: "))
c = int(input("please write length of triangle side c: "))

perimeter = a + b + c

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print("The perimeter of this triangle is: ", perimeter)
print("The area of this triangle is: ", area)
