# define function
# არგუმენტად მიიღებს სტრინგს
# return სტრინგის ხმოვნების რაოდენობნა

def number_of_vowels():
    vowels = ["a", "e", "i", "o", "u"] 
    string = input("Please input a sring: ")
    count = 0
    for vowel in string:
        if vowel.lower() in vowels:
            count += 1
    return count
    
print("The number of vowels are ", number_of_vowels())