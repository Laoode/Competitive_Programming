n= int(input())
lis_loc=[]
loc_count={}
for i in range(n):
    inp_name = input()
    inp_loc = input()
    lis_loc.append(inp_loc)
    if inp_loc in loc_count:
        loc_count[inp_loc]+=1
    else:
        loc_count[inp_loc]=1
        
for loc, count in loc_count.items():
    print(loc, count)