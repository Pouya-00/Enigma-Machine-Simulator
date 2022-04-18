from string import ascii_lowercase,digits
from random import shuffle,choice
alphabet = ascii_lowercase + digits
alphabet_list = [c for c in alphabet]
alphabet_list.insert(0, '.')
alphabet_list.insert(1, '?')
alphabet_list.append('!')
alphabet_list.append(' ')
del(alphabet)
alphabet = ''.join(alphabet_list)
rotor_1 = [c for c in alphabet]
rotor_2 = [c for c in alphabet]
rotor_3 = [c for c in alphabet]
shuffle(rotor_1)
shuffle(rotor_2)
shuffle(rotor_3)
for _ in alphabet:
    r1 = ''.join(rotor_1)
    r2 = ''.join(rotor_2)
    r3 = ''.join(rotor_3)
with open('today_rotors_configuration.enigma','w') as file:
    file.write(r1)
    file.write('\n')
    file.write(r2)
    file.write('\n')
    file.write(r3)