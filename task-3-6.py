def int_func(xstr):
    return xstr.capitalize();

word = input('Enter a word:\n');
Word = int_func(word);
print(Word);

word_set = list(input('Enter a set of words:\n').split());
Word_Set = [];
for w in word_set:
    Word_Set.append(int_func(w));
print(*Word_Set);