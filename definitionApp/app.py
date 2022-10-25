from pydictionary import Dictionary

word = input("Enter your word: ")

dict = Dictionary(word)

print(dict.meanings())


# def main():
#     word_dictionary = {
#         "hello": "a way of greeting",
#         "eyes": "a body part for seeing",
#         "earth": "a planet in space",
#     }

#     while True:
#         word = input("Enter a word: ")
#         if word == "":
#             break
#         if word in word_dictionary:
#             print(word, ":", word_dictionary[word])


# main()
