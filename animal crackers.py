
def animal_crackers(mystring):
    split_string= mystring.split()
    print(f"list {split_string}")
    return split_string[0][0] == split_string[1][0]

print(animal_crackers("hello how are you"))