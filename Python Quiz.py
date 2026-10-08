S = "abracadabra"
d={}
for ch in S:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
result = sorted(d.items(), key=lambda x: (-x[1], x[0]))
print(result)