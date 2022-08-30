from os import system
import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def clear_shell():
	if sys.platform == 'win32':
		system('cls') or None
	else:
		system('clear') or None

def generate_new_alphabet(key):
	dictionaire = {}
	new_alphabet_array = []

	n = 26 - int(key)
	if n == 26:
		n = 0

	for letter in alphabet:
		dictionaire[n] = letter
		n += 1
		if n > 25:
			n -= 26

	n = 0
	for letter in dictionaire:
		new_alphabet_array.append(dictionaire[n])
		n += 1
	new_alphabet = ''.join(new_alphabet_array)

	return new_alphabet

def create_dictionaire(key):
	new_alphabet = generate_new_alphabet(key)

	dictionaire = {}
	n = 0
	for i in alphabet:
		dictionaire[i] = new_alphabet[n]
		n += 1

	return dictionaire

def encrypt(key, msg):
	msg = msg.lower()
	dictionaire = create_dictionaire(key)

	encryption = []

	for i in msg:
		if i in alphabet:
			encryption.append(dictionaire[i])
		else:
			encryption.append(i)
	encryption = ''.join(encryption)

	return encryption


def decrypt(key, msg):
	key = 26 - int(key)
	msg = msg.lower()
	dictionaire = create_dictionaire(key)

	encryption = []
	for i in msg:
		if i in alphabet:
			encryption.append(dictionaire[i])
		else:
			encryption.append(i)
	encryption = ''.join(encryption)

	return encryption

while __name__ == '__main__':
	main = ''
	while main == '':
		clear_shell()
		main = input ('Press 1 to encrypt and 2 to decrypt message:\n')
		clear_shell()

		if main == '1':
			key = input('Insert key. It must be a number between 1 and 25:\n')
			clear_shell()
			msg = input ('Insert msg to be encrypted.\n')
			clear_shell()

			try:
				print(encrypt(key, msg))
			except:
				print('You have to put a valid key. It must be between 1 and 25.')

		else:
			key = input('Insert key. It must be a number between 1 and 25:\n')
			clear_shell()
			msg = input('Insert msg to be decrypted:\n')
			clear_shell()

			try:
				print(decrypt(key, msg))
			except:
				print('You have to put a valid key. It must be between 1 and 25.')

		main = input('')
