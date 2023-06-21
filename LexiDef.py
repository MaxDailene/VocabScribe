import os

input_file = 'OneFile.txt'
words_file = 'Lexi.txt'
examples_file = 'Examples.txt'

with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

word_lines = []
example_lines = []

for line in lines:
    line = line.strip()
    if line:
        components = line.split('\t')
        if len(components) == 3:
            word, definition, example = components
            example_lines.append(example)
        elif len(components) == 2:
            word, definition = components
        else:
            continue
        word_lines.append(f'{word}: {definition}')

with open(words_file, 'w', encoding='utf-8') as file:
    file.write('\n'.join(word_lines))

with open(examples_file, 'w', encoding='utf-8') as file:
    file.write('\n'.join(example_lines))

if os.path.exists(examples_file) and os.stat(examples_file).st_size == 0:
    os.remove(examples_file)