sentence = "Příliš žluťoučký kůň úpěl ďábelské ódy"
# a = input("Naiš slovo")
index = -1

while index >= -len(sentence):
    print(sentence[index], end="")
    index -= 1
print()
index = len(sentence)-1
while index >= 0:
    print(sentence[index], end="")
    index -= 1

print()
