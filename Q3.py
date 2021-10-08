dictionary={'language': 'python', 'version': '3.8', 'app':None, 'ide': None}
res={k:v for k,v in dictionary.items() if v is not None}
print(res)