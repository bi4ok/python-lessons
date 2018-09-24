s='Это обычная строка, а в ней адрес почты golos@mail.ru'
words=s.split(" ")
print(words)
while(1==1):
    if('@mail.ru' in s):
        print("есть совпадение")
        for x in s:
            if(x in '@mail.r'):
                print(str(x))
            elif(x in 'u'):
                print(str(x))
        break
