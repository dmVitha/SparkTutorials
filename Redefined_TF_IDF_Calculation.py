
# return  Calculate Calculate_Redefined_TF_IDF_Score for each N-gram

def cluatering_redefines_TF_IDF_score():
    tf_idf = dict.fromkeys(tf.keys(), 0)
    for word, v in tf.items():
        tf_idf[word] = v * idf[word]
    return tf_idf

    tf_idf_A : compute_tf_idf(tf_A, idf)
    tf_idf_B : compute_tf_idf(tf_B, idf)
    tf_idf_C : compute_tf_idf(tf_C, idf)

tfidf_vectorizer = TfidfVectorizer(preprocessor=preprocessing)
tfidf = tfidf_vectorizer.fit_transform(all_text)
kmeans = KMeans(n_clusters=2).fit(tfidf)

Dict_2020_10_30 = {
    "ජනාධිපතිතුමා": 65.7,"COVID කොරෝනා ව්‍යාප්තිය": 86.7,"සිදුව සෞඛ්‍ය": 86,"හමුදාව": 59,"කතුන් දෙකක් මරුට": 42,"කෝවිඩ් වෛරස": 85,"ගර්භණී": 86,"අධ්‍යක්ෂ ජනරාල්වරයා": 86,"මවුනිදෙව්ලොව": 86,"බස්නාහිර පළාතේ ඇඳිරිනීතිය": 86,"Airbus ගුවන්යානාව": 86,"ඖෂධ": 86,"නාරාහේන්පිට ප‍්‍රදේශයේ පදිංචිකරු": 56
    }