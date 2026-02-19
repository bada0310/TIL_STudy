text1 = input()
text2 = input()

count = 0
for i in text1: #
    if i not in text2:
        text1.remove(i)
        count += 1

print(text1)
for j in text2:
    if j not in text1:
        text2.remove(j)
        count += 1

print(text2)

