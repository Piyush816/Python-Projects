import string

letters = string.ascii_lowercase*2

DECRYPT = "decrypt"
ENCRYPT = "encrypt"


def cipher(text,shift,mode):

	"""cypher helps to encrypt or decrypt a text using caeser cypher"""

	result = ""

	# reducing shift value 
	shift = shift%26

	# changing shift sign 
	if(mode==DECRYPT):
		shift *= -1

	for char in text.lower():
		if (char in letters):
			position = letters.find(char)
			new_position = position+shift
			result += letters[new_position]

		else:
			result += char
		

	return result






