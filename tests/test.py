
messages = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(list(range(0, len(messages), 2)))

chunks = [messages[x:x+2] for x in range(0, len(messages), 2)]
print(chunks)

