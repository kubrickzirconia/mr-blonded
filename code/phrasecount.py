text = str(input("Copy and paste text here:"))
key_phrase = str(input("Key phrase to search for:"))
text = text.lower()
counter = text.count(key_phrase)
print("Number of occurences: ")
print(counter)
