fl = input("Enter an ASCII file: ")
f1 = open(fl, "r", encoding="utf-8")
list = []
chars = []
for line in f1:
  list.extend(line.split())  #ftiaxnw mia lista pou periexei to keimeno

reversed_list = []
for i in list:
    reversed_list.append(i[::-1])  #antistrefw to keimeno

reversed_chars = []
for i in reversed_list:
  for c in i:
    reversed_chars.append(c)  #antistrefw ta grammata tis kathe lekshs tou keimenou

katoptriko = []
for i in range(len(reversed_chars)):
  katoptriko.append(chr(128 - ord(reversed_chars[i])))

print(katoptriko)