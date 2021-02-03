from collections import defaultdict
def find_duplicates(string):
    duplicates = defaultdict(lambda:"default")
    for item in string:
        if duplicates[item] != "default":
            duplicates[item]+=1
        else:
            duplicates[item]=1

    return duplicates

duplicates = find_duplicates("Anshoo Mishra")
print(duplicates)                