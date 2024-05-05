word=str(input())
repeat=int(input())
    
if len(word)<11 and len(word)>1:
    if repeat in range(1,10):
      print(word*repeat)
    else:
        None
else:
    None