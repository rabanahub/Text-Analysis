# Text-Analysis
Text analysis, also known as text mining, focuses on extracting meaningful information and insights from structured and unstructured text data. It is crucial in various domains, including marketing, customer service, social media monitoring, content recommendation, and fraud detection.

**Tokenization**
Tokenization is the process breaking complex data like paragraphs into simple units called tokens.

**Sentence tokenization **: split a paragraph into list of sentences using sent_tokenize() method
**Word tokenization** : split a sentence into list of words using word_tokenize() method

Some other important terms related to word Tokenization are:

**Bigrams**: Tokens consist of two consecutive words known as bigrams.

**Trigrams**: Tokens consist of three consecutive words known as trigrams.

**Ngrams**: Tokens consist of ’N’ number of consecutive words known as ngrams

**Stopwords** : refers to the most common words in a language (such as “the”, “a”, “an”, “in”) which helps in formation of sentence to make sense, but these words does not provide any significance in language processing so remove it

**Stemming**
Stemming is a normalization technique where list of tokenized words are converted into shorten root words to remove redundancy. Stemming is the process of reducing inflected (or sometimes derived) words to their word stem, base or root form.

**Lemmatization**
Major drawback of stemming is it produces Intermediate representation of word. Stemmer may or may not return meaningful word.

To overcome this problem Lemmatization comes into picture.

Stemming algorithm works by cutting suffix or prefix from the word.On the contrary Lemmatization consider morphological analysis of the words and returns meaningful word in proper form.

**Bag of Words (BoW)**:
The bag-of-words model is method of feature extraction which preprocess the text by converting it into numeric format also known as vectors .BoW keeps count of the total occurrences of most frequently used words.
Bag of Words just creates a set of vectors containing the count of word occurrences in the document , while the TF-IDF model contains information on the more important words and the less important ones as well.

Bag of Words vectors are easy to interpret. However, TF-IDF usually performs better in machine learning models.Hence TF-IDF is preferred.

**TF-IDF**
TF-IDF stands for Term Frequency-Inverse Document Frequency

“Term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus.”

**Term Frequency**: is a scoring of the frequency of the word in the current document.
**Inverse Document Frequency**: is a scoring of how rare the word is across documents.

