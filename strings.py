word = "python"
word2 = "learning"

print("word:", word)
print("slicing at index 2:", word[2])
print("slicing from 2 to 5", word[2:5])

word = word.capitalize()
print("after capitalizing: ", word)
print("word2 capitalized : ", word2.capitalize())

print("word2.count : ear: ", word2.count("ear"))
print("negative indexing: ", word[-3:])

word2 = word2.replace("learning", "coding")
print(word2)

print("replacing ing with e : ", word2.replace("ing","e"))