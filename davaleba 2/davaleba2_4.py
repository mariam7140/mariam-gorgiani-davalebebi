# მიიღებს მანქანის სიჩქარეს
# განსაზღვრავს სიჩქარის კატეგორიას
# < 30 კმ/სთ --> slow
# > 120 კმ/სთ --> very fast
# > 60 კმ/სთ --> fast
# > 30 კმ/სთ --> moderate
# თუ ორ კატეგორიაში ხვდება უნდა შეირჩეს უფრო სწრაფი

velocity = int(input("what is car's velocity in km/hr? "))

if velocity < 30:
    print("SLOW")
elif 30 <= velocity < 60:
    print("MODERATE")
elif 60 <= velocity < 120:
    print("FAST")
else:
    print("VERY FAST")