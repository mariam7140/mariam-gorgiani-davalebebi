class Inset:
    
    def __init__(self):
        # ცარიელი სია
        self.elements = []

    def insert(self, element):
        # მხოლოდ უნიკალური ელემენტების დამატება
        if element not in self.elements:
            self.elements.append(element)

    def member(self, element):
        # შემოწმება არის თუ არა ელემენტი სიაში
        if element in self.elements:
            return True
        else:
            return False

    def remove(self, element):
        # ელემენტის წაშლის მცდელობა, თუ ვერ იპოვა გამოდის ValueError შეტყობინებით "ვერ ვიპოვნე"
        if element in self.elements:
            self.elements.remove(element)
        else:
            raise ValueError("ვერ ვიპოვნე")

    def __str__(self):
        # სიის დალაგება და სტრიქონად დაბრუნება
        sorted_elements = sorted(self.elements)
        return str(sorted_elements)

