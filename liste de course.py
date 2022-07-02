prix = [9,5,12,15,7,42,13,10,1,20]
cout_total = 0
i=0
for i in range (0,10):
    quantité = int(input())
    cout_total = cout_total + quantité*prix[i]
    print(cout_total)