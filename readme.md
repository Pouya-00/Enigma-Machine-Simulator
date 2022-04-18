# Enigma-Machine-Simulator
 
Enigma is a machine to encrypt text.
This version of enigma support __digits number__ : __0123456789__
__Signs__ : __? ! .__
and __space__
Also you can enter manual plug board configuration for advance encryption.
## Installation

There is nothing to install everything is ready already.

## Usage

First run the rotors.py with command __python rotors.py__ this will generate a file named __rotors_today_configuration.enigma__ this is the rotors pattern to encrypt your text be careful if you run __rotors.py__ again the pattern will change and you can't decrypt your text without that pattern.
After that run enigma.py with command __python enigma.py__ program ask you about plug board if you wanna enter plug board config you need to answer yes and the format of plug board should be A-Z chracters 0-9 numbers and !?. signs and space, there shouldn't be duplicate characters and the length of input should be a even number to pair them, after that program ask you about encrypt or decrypt you can answer with enc or dec then enter your text to encrypt or decrypt (if you already encrypted that and now you want to decrypt that) after that in the program folder you will see a file named encrypted.enigma or decrypted.enigma (depending on your choice) you can open it with any text editor like notepad.

