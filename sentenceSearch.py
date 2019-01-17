#intro----------------------------
print ("""
This program will generate ammount of words, sentences, 
the longest word, average length of word used 
and the amount of words with more than 3 characters. 
Here is the paragraph and the data. \n""")

sentence = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Id donec ultrices tincidunt arcu non. Pharetra vel turpis nunc eget. Urna nec tincidunt praesent semper feugiat nibh. Ipsum faucibus vitae aliquet nec ullamcorper sit amet risus. A erat nam at lectus urna duis convallis convallis. In fermentum posuere urna nec tincidunt praesent semper. Egestas dui id ornare arcu odio ut sem nulla pharetra. Egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate sapien. Pulvinar etiam non quam lacus suspendisse faucibus interdum. Quisque egestas diam in arcu cursus euismod quis viverra nibh. Arcu bibendum at varius vel pharetra vel. Faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis. Vestibulum sed arcu non odio euismod lacinia at. Ipsum a arcu cursus vitae congue mauris rhoncus aenean vel. Senectus et netus et malesuada fames ac. Diam volutpat commodo sed egestas. Lacinia quis vel eros donec ac odio tempor. Diam sollicitudin tempor id eu nisl nunc mi ipsum. Vitae et leo duis ut diam.\n")
print (sentence)


#function-------------------------
def sentence_search(sentence):

    word_split = sentence.split()
    ammount_of_words = len(word_split)
    # #.split method splits the array string into 1 word individual strings, to finding the length of the word variable.
    print ("The ammount of words: " , ammount_of_words)


    sentence_split = sentence.split('. ')
    ammount_of_sentences = len(sentence_split)
    # #split method again splits the array string between every '. ' to create a sentence split, this splits the 20 sentences apart and then the length is push into a new variable.
    print ("The ammount of sentences: ", ammount_of_sentences)


    length = 0
    longest_word = []
    #updates everytime the function loops through the sentence array. when the longest word is found then the loop will stop.

    for long_word in word_split:
        if len(long_word) > len(longest_word):
            length = len(long_word)
            longest_word = long_word
    print ("The longest word is: ",longest_word,", with a length of " , length , "characters.")

    average_length_of_words_used = sum(len(individual_word_length) for individual_word_length in word_split)/len(word_split)
    print ("The average length of words used is: ", average_length_of_words_used)


    more_than_3_letter_words = []
    for word in word_split:
        if len(word) > 3:
            more_than_3_letter_words += [word]
    print ("The list of words with more than 3 words are: ", more_than_3_letter_words)
        

sentence_search(sentence)