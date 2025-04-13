while True:
    line = input('>> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break

    print(line)
print('Loop is terminated')

#this is an infinite loop that will keep prompting you to enter a value until the value input is 'done'