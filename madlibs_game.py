#Madlibs game

print("Welcome to Mad libs!")
print("Please provide the following words to complete the story")

#user inputs
adjective = input("Enter an adjective: ")
noun = input("Enter a noun(plural): ")
verb = input("Enter a verb(past tense): ")
place = input("Enter a place: ")
adverb = input("Enter an adverb: ")

story = f"""
One {adjective} morning, a group of {noun} {verb} through the
forest. They were heading to a mysterious {place}, where they hoped
to discover ancient treasures. They moved {adverb} through the trees,
eager for adventure.
"""

print("Here's your Mad Libs Story:")
print(story)
