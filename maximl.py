d=input()
s=[]
for char in d[::]:
  if char  not in s:
    s.append(char)
print(len(s))
