
words  = ["hello", "WORLD"]

search = "WORLD"

result = [f"{word}!" for word in words if search in word]

# result = [word.lower() for word in words]
# result = map(str.lower, words)


symbols = '$¢£¥€¤'
# beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
beyond_ascii = list(filter(lambda c: ord(c) > 127, symbols))


# result = [f"{word.lower()}" for word in words if search in word]

# words.filter {|word| search in word }
print(beyond_ascii)

