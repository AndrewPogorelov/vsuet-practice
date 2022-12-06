def l():
    number=int(input(""))

    div=2
    if number%div==0:
        print(div)
    else:
        while number%div!=0:
            div+=1
        print(div)
l()