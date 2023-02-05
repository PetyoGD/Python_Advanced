string_sample = list(input())
reversed_string = []

for x in range(len(string_sample)):
    reversed_string.append(string_sample.pop())

print("".join(reversed_string))