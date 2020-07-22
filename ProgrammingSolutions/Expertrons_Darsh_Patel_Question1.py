s = input()

if(any([x.isalpha() for x in s])):
    print("INVALID")
elif((s.startswith("7") or s.startswith("8") or s.startswith("9")) and (len(s) == 10)):
    print("VALID")
else:
    print("INVALID")