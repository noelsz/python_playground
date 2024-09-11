print("Welcome to Mad Libs!")

adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
location = input("Enter a location: ")

story = f"Once upon a time, in a {location}, there was a {adjective} {noun}. " \
        f"This {noun} loved to {verb} in the {location}."

print("\nHere is your completed Mad Libs story:")
print(story)





