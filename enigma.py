from string import ascii_lowercase,digits
alphabet = ascii_lowercase + digits
alphabet_list = [c for c in alphabet]
alphabet_list.insert(0, '.')
alphabet_list.insert(1, '?')
alphabet_list.append('!')
alphabet_list.append(' ')
del(alphabet)
plug_board = []
while True:
    try:
        plg_ask = input('Do you wanna set plug board?(yes / no): ')
        plg_ask.lower()
        if plg_ask not in ['y','yes','n','no','1','0']:
            raise ValueError()
        else:
            break
    except(ValueError):
        print('Please enter only yes or no!')
while True:
    try:
        if plg_ask in ['y','yes','1']:
            plug_config = input('Enter whole plug board setting in one line: ')
            if len(plug_config) % 2 != 0:
                raise ValueError()
            else:
                plug_config.lower()
                rnd = 0
                for _ in range(len(plug_config) // 2):
                    plug_board.append(plug_config[rnd:rnd+2])
                    rnd += 2
                break
        else:
            break
    except(ValueError):
        print('Length of plug board should be even, characters are A-Z 0-9 and !? . signs. and it should not be duplicate characters.')

def plugboard(char):
    global plug_board
    for i in plug_board:
        if char == i[0]:
            return i[1]
        elif char == i[1]:
            return i[0]
        else:
            continue
    return char
def getrotors():
    with open('today_rotors_configuration.enigma','r') as file:
        r1 = file.readline()
        r2 = file.readline()
        r3 = file.readline()
        rotor_1 = [c for c in r1]
        rotor_2 = [c for c in r2]
        rotor_3 = [c for c in r3]
        rotor_1.pop()
        rotor_2.pop()
        rotor1 = ''.join(rotor_1)
        rotor2 = ''.join(rotor_2)
        rotor3 = ''.join(rotor_3)
    return rotor1,rotor2,rotor3
def reflector(char):
    return alphabet_list[len(alphabet_list)-alphabet_list.index(char)-1]
def enigma(char):
    character = ''
    index = 0
    if plg_ask in ['y','yes','1']:
        char = plugboard(char)
    index = alphabet_list.index(char)
    character = r1[index]
    index = alphabet_list.index(character)
    character = r2[index]
    index = alphabet_list.index(character)
    character = r3[index]
    reflected = reflector(character)
    index = r3.index(reflected)
    character = alphabet_list[index]
    index = r2.index(character)
    character = alphabet_list[index]
    index = r1.index(character)
    character = alphabet_list[index]
    if plg_ask in ['yes','y','1']:
        character = plugboard(character)
    return character
def rotate_rotors():
    global r1,r2,r3
    r1 = r1[1:] + r1[0]
    if state % 40 == 0:
        r2 = r2[1:] + r2[0]
    if state % (40*40) == 0:
        r3 = r3[1:] + r3[0]
def encrypt(plain):
    global state,cypher
    for char in plain:
        state += 1
        cypher += enigma(char)
        rotate_rotors()
    #print(f'encrypted : {cypher}')
    return cypher
def decrypt(plain):
    global state,cypher
    for char in plain:
        state += 1
        cypher += enigma(char)
        rotate_rotors()
    #print(f'decrypted : {cypher}')
    return cypher   
r1,r2,r3 = getrotors()
plain = ''
cypher = ''
state = 0
while True:
    try:
        print('Result will save into a .enigma file.')
        person_input = (input('Do you wanna encrypt or decrypt?(enc / dec): '))
        person_input.lower()
        if person_input not in ['enc','dec']:
            raise ValueError()
        else:
            break
    except(ValueError):
        print('Please only answer with enc or dec!')
if person_input == 'enc':
    plain = input('Enter your text to encrypt: ')
    encrypted = encrypt(plain)
    with open('encrypted.enigma','w') as file:
        file.write(encrypted)
elif person_input == 'dec':
    plain = input('Enter your text to decrypt: ')
    decrypted = decrypt(plain)
    with open('decrypted.enigma','w') as file:
        file.write(decrypted)
else:
    print('Wrong value')

