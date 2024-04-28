import re
import numpy


def multiply_elements(myList):
    result = 1
    for el in myList:
        result *= el
    return result


pattern = r"(\*{2}|\:{2})[A-Z][a-z]{2,}\1"
data = input()
cool_emojis = []
all_emojis = re.finditer(pattern, data)
all_emojis = [emoji.group() for emoji in all_emojis]
cool_sum = [int(digit.group()) for digit in re.finditer(r"\d", data)]
cool_sum = multiply_elements(cool_sum)
for emoji in all_emojis:
    current_emoji_value = 0
    current_emoji = emoji[2:-2]
    for letter in current_emoji:
        current_emoji_value += ord(letter)
    if current_emoji_value >= cool_sum:
        cool_emojis.append(emoji)
print(f"Cool threshold is: {cool_sum}")
print(f"{len(all_emojis)} emojis found in the text. The cool ones are:")
if cool_emojis:
    print(*cool_emojis, sep="\n")