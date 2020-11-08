
import nltk
from nltk.util import ngrams

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel



from collections import Counter

texts = ['රට පවත්නා කොවිඩ් තත්ත්වය හමුවේ දරුවන්ගේ ආරක්ෂාව තහවුරු කරමින්  ආරම්භ  අපොස ' 
         'පාස්කු ඉරිදා දිනයේ  මරාගෙන මැරෙන බෝම්බ ප්‍රහාර එල්ල ඊබ්‍රාහීම් ' 
         'ශ්‍රී ලංකා පොලීසිය ෂ්කර තත්වයන් රාජකාරි  රාජකාරියට බාධා පැමිණෙන අවස්ථා කිහිපයක් පූජිත් ජයසුන්දර ' 
         'මන්නාරමේ මෙහෙයුමකින් ගංජා තොගයක් සොයා'
         'කෝවිඩ්-19 වසංගතය කටුනායක වෙළෙඳ කලාපය ඇතුළු  ඇඟලුම් කම්හල්වල සේවක සේවිකාවන්  පමණ රැකියා අහිමි  වෘත්තීය සමිති '
         'දෙවෙනි රැල්ල ආරම්භ වූයේ ඉන්දියාවෙන් බ්‍රැන්ඩික්ස් සේවකයන්ගෙන් නොවන බව හමුදාපති ලුතිනන් ජනරාල් ශවේන්ද්‍ර '
         'කොවිඩ් ආසාදිතයින් '
         'මිනුවන්ගොඩ පොකුරේ  ආශ්‍රිතයින් කොරෝනා'
         'මිනුවන්ගොඩ කොරෝනා පොකුරෙන්  ආසාදිතයින්']




token = [nltk.word_tokenize(text) for text in texts]

# Create Dictionary
id2word = corpora.Dictionary(token)
corpus = [id2word.doc2bow(text) for text in token]
# print(corpus[:1])

# Build LDA model
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=4,
                                           update_every=1,
                                           chunksize=1,
                                           passes=3,
                                           alpha='auto',
                                           per_word_topics=True)

# Print the Keyword in the 10 topics
print(lda_model.print_topics(num_words=6))
doc_lda = lda_model[corpus]

