dna = input()
dna = dna.upper()
found = False
for i in range(len(dna)-2):
    if dna[i] =="C" and dna[i+1] == "O" and dna[i+2] == "V":
        found = True
        break
    else:
        None
if found:
    print("Veikur!")
else:
    print("Ekki veikur!")