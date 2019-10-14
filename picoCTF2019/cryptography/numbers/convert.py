import string

numbers = [16,9,3,15,3,20,6,"{",20,8,5,14,21,13,2,5,18,19,13,1,19,15,14,"}"]
arrayed_string = []

for char in numbers:
    if (type(char) == int):
        arrayed_string.append(string.ascii_letters[char - 1])
    else:
        arrayed_string.append(char)

print("".join(arrayed_string))