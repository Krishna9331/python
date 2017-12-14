import ex25

sentence = "All good things comes to those who wait."
words = ex25.break_words(sentence)
print('\n-------words--------')
print(words)
print('--------------------\n')
sorted_words = ex25.sort_words(words)
print('\n-------sorted words--------')
print(sorted_words)
print('--------------------\n')
ex25.print_first_word(words)
ex25.print_last_word(words)
# words
print('Finding first and last after sorting----')
ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
# sorted_words

sorted_words = ex25.sort_sentence(sentence)
# sorted_words
print('Finding first and last without sorting sentence----')
ex25.print_first_and_last(sentence)
print('Finding first and last after sorting sentence----')
ex25.print_first_and_last_sorted(sentence)
