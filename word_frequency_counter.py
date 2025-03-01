def word_frequency(sentence):
    words = sentence.split()
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    return freq_dict
    
     

    