def merge_sorted_list(list_1, list_2):
    merged_list = []
    i = 0
    j = 0

    # სიის გავლა და დალაგებული მიმდევრობით შეერთება
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            merged_list.append(list_1[i])
            i += 1
        else:
            merged_list.append(list_2[j])
            j += 1
    
    # რა ელემენტებიც დარჩა იმის ჩამატება სიაში
    while i < len(list_1):
        merged_list.append(list_1[i])
        i += 1
    
    while j < len(list_2):
        merged_list.append(list_2[j])
        j += 1

    return merged_list

list_1 = [1, 3]
list_2 = [0, 4, 7, 9]
merged = merge_sorted_list(list_1, list_2)
print("Merged list: ", merged)