word = input()

location = [-1] * 26

for i in range(len(word)):
    if location[ord(word[i]) - ord('a')] == -1:
        location[ord(word[i]) - ord('a')] = i
    else:
        continue

print(' '.join(map(str, location)))