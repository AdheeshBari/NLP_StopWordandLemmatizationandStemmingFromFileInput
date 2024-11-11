# NLP_StopWordandLemmatizationandStemmingFromFileInput
This program preprocesses text from a file by removing stop words and applying lemmatization, stemming, or both as per user choice.

This Python script reads a text file, tokenizes the words, removes stop words, and performs lemmatization, stemming, or both based on user input.

Steps:
1. Setup and Download: Ensures that NLTK data resources for tokenization, stop words, and lemmatization are downloaded.
2. File Input: Prompts the user to enter the path of a text file to read its contents.
3. Choice Input for Processing: Asks the user to select the type of text processing: lemmatization ('lemm'), stemming ('stem'), or both ('both').
4. File Reading and Tokenization: Opens the specified file, reads its content, and tokenizes it into individual words.
5. Stop Word Removal: Filters out common English stop words from the tokenized list.
6. Initialization of Lemmatizer and Stemmer: Initializes both the lemmatizer (WordNet Lemmatizer) and stemmer (Porter Stemmer) for text processing.
7. Processing by User Choice:
      Lemmatization ('lemm'): Applies lemmatization to each word in the filtered list and outputs the lemmatized words.
      Stemming ('stem'): Applies stemming to each word in the filtered list and outputs the stemmed words.
      Both ('both'): First applies lemmatization, then stems each lemmatized word, and outputs both results.
Output: Prints the filtered list without stop words, the lemmatized words, and the stemmed words based on the user's choice.

This script is ideal for basic text preprocessing in natural language processing (NLP) tasks, enabling easy text normalization from a file input.
