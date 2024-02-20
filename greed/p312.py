n = input()
result = int(n[0])
for i in n[1:]:
    added = int(i)+result
    multied = int(i)*result
    if added>multied:
        result = added
    else:
        result = multied

print(result)