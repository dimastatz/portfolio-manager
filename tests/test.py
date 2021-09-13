
data = [i for i in range(100)]
chunks = [data[x:x+10] for x in range(0, len(data), 10)]
res = ['\n'.join([str(i) for i in x]) for x in chunks]

print(res[0])