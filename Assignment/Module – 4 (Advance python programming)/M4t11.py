# Write a Python program to count the frequency of words in a file. 

def count_word_frequency(file_path):
    word_freq = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

def main():
    file_path ="C:\\Users\\sarthak saraniya\\Desktop\\python\\python23\\Assignment\\Module – 4 (Advance python programming)\\file.txt"
    word_freq = count_word_frequency(file_path)
    
    for word, frequency in word_freq.items():
        print(f'{word}: {frequency}')

if __name__ == "__main__":
    main()
