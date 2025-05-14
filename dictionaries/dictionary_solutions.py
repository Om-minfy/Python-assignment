# Easy Questions
# 1. Invert Dictionary
def invert_dictionary(d):
    new_dict = {}
    for key in d:
        value = d[key]
        new_dict[value] = key
    return new_dict

print("invert_dictionary:")
print(invert_dictionary({"a": 1, "b": 2, "c": 3}))


# 2. Merge Dictionaries
def merge_dictionaries(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

print("\nmerge_dictionaries:")
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(merge_dictionaries(d1, d2))


# Medium Questions
# 1. Word Frequencies
def word_frequencies(text):
    words = text.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

print("\nword_frequencies:")
text = "the quick brown fox jumps over the lazy dog"
print(word_frequencies(text))


# 2. Add Contact
def add_contact(contacts, name, **info):
    if name not in contacts:
        contacts[name] = {}
    contacts[name].update(info)

print("\nadd_contact:")
contacts = {}

add_contact(contacts, "Alice", phone="123-456-7890", email="alice@example.com")
add_contact(contacts, "Bob", phone="987-654-3210")
add_contact(contacts, "Alice", address="123 Main St")
print(contacts)