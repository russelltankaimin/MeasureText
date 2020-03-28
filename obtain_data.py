def clean_text(essay):
    sentences=0
    avg_len_of_sentences=0
    avg_len_of_word=0
    words=0
    letters=0
    word_len=0
    common_words=['to','with','from','but','in','upon','and','or']
    standard_freq=6
    sample=essay.replace(" ",'')
    for char in sample:
        if char=='.' or char=='!' or char=='?':
            sentences+=1
    #print("There are",sentences,'sentences')
    sen_list=split_into_sentences(essay)
    for line in sen_list:
        i=line.split()
        #i is a list of words
        words+=len(i)
        t=0
        for word in i:
            t+=1
        #print("There are",t,"words in this sentence")
    #print("There are a total of",words,"words in the text")       
    avg_len_of_sentences=words/sentences
    #print("There are an average of",avg_len_of_sentences,"words in a sentence")
    alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for indiv in sample:
        if indiv in alphabet:
            word_len+=1
        else:
            pass
    #print("The average length of words is",word_len/words)
    score_cw=[0,0,0,0,0,0,0,0]
    for line in sen_list:
        line=line.split()
        for w in line:
            w=w.lower()
            if w in common_words:
                score_cw[common_words.index(w)]+=1
            else:
                pass
    #print(common_words,'=',score_cw)
    return [sentences,words,avg_len_of_sentences,word_len/words]+[score_cw[i] for i in range(len(score_cw))]
