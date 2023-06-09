input_file = 'OneFile.txt'
words_file = 'Lexi.txt'
definitions_file = 'Def.txt'

with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

word_lines = []
example_lines = []

for line in lines:
    line = line.strip()
    if line:
        word, definition, example = line.split('\t')
        word_lines.append(f'{word}: {definition}')
        example_lines.append(example)

with open(words_file, 'w', encoding='utf-8') as file:
    file.write('\n'.join(word_lines))

with open(definitions_file, 'w', encoding='utf-8') as file:
    file.write('\n'.join(example_lines))