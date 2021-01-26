convert = [i.strip().split(' = ') for i in open('dictionary.txt')]
with open('output.txt', 'w') as outfile, open('input.txt') as infile:
    for line in infile:
        for oldword, newword in convert:
            line = line.replace(oldword, newword)
        outfile.write(line)
