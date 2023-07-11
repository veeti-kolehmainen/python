# Veeti Language
# Vowels -> V

def translate(phrase):
    translation = ""
    for let in phrase:
        if let.lower() in "aeiou":
            if let.isupper():
                translation = translation + "V"
            else:
                translation = translation + "v"
        else:
            translation = translation + let
    return translation

print(translate(input("Enter a phrase: ")))