
def untranslate(phrase):
	translation = ""
	for letter in phrase:
		if letter.lower() == "m":
			translation = translation + "a"
		elif letter.lower() == "n":
			translation = translation + "b"
		elif letter.lower() == "o":
			translation = translation + "c"	
		elif letter.lower() == "p":
			translation = translation + "d"
		elif letter.lower() == "q":
			translation = translation + "e"
		elif letter.lower() == "r":
			translation = translation + "f"
		elif letter.lower() == "s":
			translation = translation + "g"
		elif letter.lower() == "t":
			translation = translation + "h"
		elif letter.lower() == "u":
			translation = translation + "i"
		elif letter.lower() == "v":
			translation = translation + "j"
		elif letter.lower() == "w":
			translation = translation + "k"
		elif letter.lower() == "x":
			translation = translation + "l"
		elif letter.lower() == "y":
			translation = translation + "m"	
		elif letter.lower() == "z":
			translation = translation + "n"
		elif letter.lower() == "a":
			translation = translation + "o"
		elif letter.lower() == "b":
			translation = translation + "p"
		elif letter.lower() == "c":
			translation = translation + "q"
		elif letter.lower() == "d":
			translation = translation + "r"
		elif letter.lower() == "e":
			translation = translation + "s"
		elif letter.lower() == "f":
			translation = translation + "t"
		elif letter.lower() == "g":
			translation = translation + "u"
		elif letter.lower() == "h":
			translation = translation + "v"
		elif letter.lower() == "i":
			translation = translation + "w"
		elif letter.lower() == "j":
			translation = translation + "x"
		elif letter.lower() == "k":
			translation = translation + "y"
		elif letter.lower() == "l":
			translation = translation + "z"							
		else:
			translation = translation + letter										
	return translation

phrase = input("Enter a message: ")
print(untranslate(phrase))
input("Press ENTER to exit")
