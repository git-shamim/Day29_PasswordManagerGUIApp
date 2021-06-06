# FileNotFoundError
with open("a_file.txt") as file:
    file.read()

# KeyError
a_dictionary = {"Key": "Value"}
value = a_dictionary["non_existent_key"]

# IndexError
fruit_list = ["apple", "orange", "banana"]
fruit = fruit_list[3]

# TypeError
text = "abc"
print(text + 3)

try:
    file = open("a_file.txt")
    a_dictionary = {"Key": "Value"}
    print(a_dictionary["non_existent_key"])
except FileNotFoundError:
    file = open("a_file.txt", 'w')
    file.write("Something")
except KeyError as error_message:
    print("That key {} does not exist".format(error_message))
else:
    content = file.read()
    print(content)
finally:
    file.close()


height = float(input())
weight = int(input())

if height > 3:
    raise ValueError("human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
