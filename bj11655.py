s = input()
result = ''
for i in s:
    if i.isupper():
        if (65 <= ord(i) <= 77): # +13해도 Z를 넘지 않음
            result += chr(ord(i)+13)
        else:
            result += chr(ord(i)-13)        
    elif i.islower():
        if (97 <= ord(i) <= 109): # +13해도 z를 넘지 않음
            result += chr(ord(i)+13)
        else:
            result += chr(ord(i)-13)
    else:
        result += i
print(result)