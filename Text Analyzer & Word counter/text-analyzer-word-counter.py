def total_lines(text):
    sen_lines = len(text.splitlines())
    return sen_lines

def word_len(text):
    total_word = len(text.split())
    return total_word

def text_len(text):
    total_char = len(text)
    return total_char

def top_words(text):
    low_text = text.lower()
    split_sen = low_text.split()
    word_counts = {} 
    for word in split_sen:
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1         
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    top_5 = sorted_words[:5]
    return top_5

print("--------- TEXT ANALYSIS REPORT ---------\n")

with open("Text Analyzer & Word counter/sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(f"Total Lines: {total_lines(text)}")
print(f"Total Words: {word_len(text)}")
print(f"Total length of characters: {text_len(text)}")

print("\nMost used words:")
results = top_words(text)
for word, count in results:
    print(f" -> '{word}' used {count} times")
print("\n"+"-"*40)