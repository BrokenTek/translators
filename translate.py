
def translate(phrase):
	translation = ""
	for letter in phrase:
		if letter.lower() == "a":
			translation = translation + "m"
		elif letter.lower() == "b":
			translation = translation + "n"
		elif letter.lower() == "c":
			translation = translation + "o"	
		elif letter.lower() == "d":
			translation = translation + "p"
		elif letter.lower() == "e":
			translation = translation + "q"
		elif letter.lower() == "f":
			translation = translation + "r"
		elif letter.lower() == "g":
			translation = translation + "s"
		elif letter.lower() == "h":
			translation = translation + "t"
		elif letter.lower() == "i":
			translation = translation + "u"
		elif letter.lower() == "j":
			translation = translation + "v"
		elif letter.lower() == "k":
			translation = translation + "w"
		elif letter.lower() == "l":
			translation = translation + "x"
		elif letter.lower() == "m":
			translation = translation + "y"	
		elif letter.lower() == "n":
			translation = translation + "z"
		elif letter.lower() == "o":
			translation = translation + "a"
		elif letter.lower() == "p":
			translation = translation + "b"
		elif letter.lower() == "q":
			translation = translation + "c"
		elif letter.lower() == "r":
			translation = translation + "d"
		elif letter.lower() == "s":
			translation = translation + "e"
		elif letter.lower() == "t":
			translation = translation + "f"
		elif letter.lower() == "u":
			translation = translation + "g"
		elif letter.lower() == "v":
			translation = translation + "h"
		elif letter.lower() == "w":
			translation = translation + "i"
		elif letter.lower() == "x":
			translation = translation + "j"
		elif letter.lower() == "y":
			translation = translation + "k"
		elif letter.lower() == "z":
			translation = translation + "l"							
		else:
			translation = translation + letter										
	return translation

phrase = input("Enter a message: ")
print(translate(phrase))
input("Press ENTER to exit")				