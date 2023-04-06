# Prompt the user to enter a sentence
sentence = input('Please enter a sentence: ')

# Create an empty dictionary to store the frequency of each word
frequency = {}

# Split the sentence into words and store each word as a key in the frequency dictionary with its value as the number of occurrences
for word in sentence.split():
    # The get() method retrieves the value of a key from the dictionary. If the key does not exist, it returns a default value of 0.
    # The line below is equivalent to frequency[word] = frequency[word] + 1 if the key exists, or frequency[word] = 1 if the key does not exist.
    frequency[word] = frequency.get(word, 0) + 1

# Get the keys of the frequency dictionary
keys = frequency.keys()

# Loop over the keys and print each key and its value
for key in keys:
    print(f'{key}: {frequency[key]}')

