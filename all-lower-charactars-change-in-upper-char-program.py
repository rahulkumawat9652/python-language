my_string = "asdf12234GFDS"
result = ""
for ch in my_string:
    ascii = ord(ch)
    if ascii >= 97 and ascii <= 122:
        new_ascii = ascii-32
        char = chr(new_ascii)
        result += char
    else:
        result += ch
print(result)