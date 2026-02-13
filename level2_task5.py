#Task: File Manipulation

#Write a Python program that reads a text
#file and counts the occurrences of each
#word in the file. Display the results in
#alphabetical order along with their respective counts.


import string

def count_words(filename):
    word_count = {}

    try:
        with open(filename, "r") as file:
            for line in file:
                # Remove punctuation and convert to lowercase
                line = line.lower().translate(str.maketrans("", "", string.punctuation))
                words = line.split()

                for word in words:
                    word_count[word] = word_count.get(word, 0) + 1

        # Display results in alphabetical order
        print("Word counts (alphabetical order):")
        for word in sorted(word_count):
            print(f"{word}: {word_count[word]}") 

    except FileNotFoundError:
        print("File not found. Please check the filename.")

# Get filename from user
filename = input("Enter the filename: ")
count_words(filename)


