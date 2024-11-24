def generate_sequence(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n //= 2  # თუ ლუწია გავყოთ 2ზე
        else:
            n = n * 3 + 1  # თუ კენტია გავამრავლოთ 3-ზე და გავყოთ 2-ზე
    sequence.append(1)
    return sequence

def generate_sequence_cache(n, cache={}):
    if n in cache:
        return cache[n]

    sequence = []
    original_n = n  # თავდაპირველი რიცხვი რაც გვქონდა

    while n != 1:
        if n in cache:  # ვამოწმებთ ეს რიცხვი არის თუ არა მიმდევრობაში
            sequence.extend(cache[n])
            break
        sequence.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    sequence.append(1)
    cache[original_n] = sequence
    return sequence

n = int(input("Enter a number: "))

ordinary_sequence = generate_sequence(n)
print("Sequence (ordinary):", ordinary_sequence)

cached_sequence = generate_sequence_cache(n)
print("Sequence (with caching):", cached_sequence)
