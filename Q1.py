dictionary = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dictionary)

#adding item
dictionary["color"]="red"
print("dictionary after adding item:",dictionary)

#removing item
dictionary.pop("model")
print("after removing item :",dictionary)