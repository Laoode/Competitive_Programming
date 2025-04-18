fiz= int(input())

ing = {"ml gin":45, "ml fresh lemon juice":30, "ml simple syrup":10, "slice of lemon":1}

for key, value in ing.items():
    if fiz>1:
        if key=='slice of lemon':
            key="slices of lemon"
        print(value*fiz, key)
    else:
        print(value*fiz, key)