words = 'Lorem Ipsum is simply dummy text of the printing and typesetting industryU Аu'
letters = ['a', 'e', 'i', 'o', 'u', 'y', 'а', 'у', 'о', 'ы', 'э', 'я', 'ю', 'ё', 'и', 'е', 'і']
result = 0
for word in words.split(' '):
    vowels_in_word = 0
    for letter in word:
        vowels_in_word = vowels_in_word + 1 if letter.lower() in letters else 0
        if vowels_in_word == 2:
            result += 1
            break

print(result)
