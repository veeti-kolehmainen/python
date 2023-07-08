monthConversions = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December",
}

userInput = input("Give me a 3 letter month abbreviation: ")

print(monthConversions.get(userInput.lower(), "Not a valid key"))
# print(monthConversions["Jun"])