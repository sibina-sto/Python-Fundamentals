# 08-02. TEXT PROCESSING [Exercise]
# 08. Letters Change Numbers

strings = input().split()
result = 0.00

for string in strings:
    first_letter = string[0]
    first_letter_position = ord(first_letter.lower()) - 96
    last_letter = string[-1]
    last_letter_position = ord(last_letter.lower()) - 96
    number = int(string[1:-1])

    if first_letter.isupper():
        number /= first_letter_position
    else:
        number *= first_letter_position

    if last_letter.isupper():
        number -= last_letter_position
    else:
        number += last_letter_position

    result += number

print(f'{result:.2f}')
