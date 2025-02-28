#Khoa Duong
#assignment 7
#Write a program that allow user to enter a paragraph, then display each sentences in sequences.

import re

#Split sentences and print it in number sequnces.
def split_sentence(paragraph):
    #This pattern only detect sentences started with a uppercase letters.
    sentence_pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'
    sentences = re.findall(sentence_pattern, paragraph, flags=re.DOTALL | re.MULTILINE)

    print("Extracted Sentences:")
    for i, sentence in enumerate(sentences, 1):
        print(f'{i}. {sentence}')
        
    print(f"\nTotal number of sentences: {len(sentences)}")

def main():
    paragraph = input("Please enter your texts: ")
    split_sentence(paragraph)


if __name__ == "__main__":
    main()
