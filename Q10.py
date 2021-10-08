d1 = {'1': 1, '2': 2, '3': 3}
d2 = {'4': 4, '5': 5, '6': 6}
#update method
comb=d1.update(d2)
print(comb)
print("dict by update method",d1)

#Merge method
res=dict(d2.items()|d1.items())
print("dict by union",res)
