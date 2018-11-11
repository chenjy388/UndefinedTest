def word_frequency_analysis():
    article = input("input:")
    print(article)
    article=article.lower()
    article=article.replace(',','')
    article=article.replace('.','')
    list=article.split(' ')
    print(list)
    dict={}
    for word in list:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    for word in dict:
        print(word,dict[word])
