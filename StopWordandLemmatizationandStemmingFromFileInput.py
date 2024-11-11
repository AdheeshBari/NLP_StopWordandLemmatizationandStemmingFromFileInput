import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

# Download the NLTK data files (only the first time you run this program)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_file(file_path, choice):
    # Read the content from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
    
    # Tokenize words from the file content
    word_tokens = word_tokenize(file_content)
    
    # Define stop words in English
    stop_words = set(stopwords.words('english'))
    
    # Remove stop words
    filtered_words = [word for word in word_tokens if word.lower() not in stop_words]
    
    # Initialize the lemmatizer and stemmer
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    
    # Process based on user choice
    if choice == "lemm":
        processed_words = [lemmatizer.lemmatize(word) for word in filtered_words]
        print("Lemmatized Words:\n", processed_words)
    elif choice == "stem":
        processed_words = [stemmer.stem(word) for word in filtered_words]
        print("Stemmed Words:\n", processed_words)
    elif choice == "both":
        lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
        stemmed_words = [stemmer.stem(word) for word in lemmatized_words]
        print("Lemmatized Words:\n", lemmatized_words)
        print("Stemmed Words after Lemmatization:\n", stemmed_words)
    else:
        print("Invalid choice! Please select 'lemm', 'stem', or 'both'.")
    
    # Output filtered words without stop words
    print("Filtered Words (without stop words):\n", filtered_words)

if __name__ == "__main__":
    # Prompt for file path and read file content
    file_path = input("Enter the path to the file: ")
    
    # Ask for preprocessing choice
    choice = input("Enter 'lemm' for Lemmatization, 'stem' for Stemming, or 'both' for both Lemmatization and Stemming: ").strip().lower()
    
    # Process the text from the file based on the user's choice
    preprocess_file(file_path, choice)

# OUTPUT
# Enter the path to the file: Textfile.txt
# Enter 'lemm' for Lemmatization, 'stem' for Stemming, or 'both' for both Lemmatization and Stemming: both
# Lemmatized Words:
#  ['Lorem', 'Ipsum', 'simply', 'dummy', 'text', 'printing', 'typesetting', 'industry', '.', 'Lorem', 'Ipsum', 'industry', "'s", 'standard', 'dummy', 'text', 'ever', 'since', '1500s', ',', 'unknown', 'printer', 'took', 'galley', 'type', 'scrambled', 'make', 'type', 'specimen', 'book', '.', 'survived', 'five', 'century', ',', 'also', 'leap', 'electronic', 'typesetting', ',', 'remaining', 'essentially', 'unchanged', '.', 'popularised', '1960s', 'release', 'Letraset', 'sheet', 'containing', 'Lorem', 'Ipsum', 'passage', ',', 'recently', 'desktop', 'publishing', 'software', 'like', 'Aldus', 'PageMaker', 'including', 'version', 'Lorem', 'Ipsum', '.']
# Stemmed Words after Lemmatization:
#  ['lorem', 'ipsum', 'simpli', 'dummi', 'text', 'print', 'typeset', 'industri', '.', 'lorem', 'ipsum', 'industri', "'s", 'standard', 'dummi', 'text', 'ever', 'sinc', '1500', ',', 'unknown', 'printer', 'took', 'galley', 'type', 'scrambl', 'make', 'type', 'specimen', 'book', '.', 'surviv', 'five', 'centuri', ',', 'also', 'leap', 'electron', 'typeset', ',', 'remain', 'essenti', 'unchang', '.', 'popularis', '1960', 'releas', 'letraset', 'sheet', 'contain', 'lorem', 'ipsum', 'passag', ',', 'recent', 'desktop', 'publish', 'softwar', 'like', 'aldu', 'pagemak', 'includ', 'version', 'lorem', 'ipsum', '.']
# Filtered Words (without stop words):
#  ['Lorem', 'Ipsum', 'simply', 'dummy', 'text', 'printing', 'typesetting', 'industry', '.', 'Lorem', 'Ipsum', 'industry', "'s", 'standard', 'dummy', 'text', 'ever', 'since', '1500s', ',', 'unknown', 'printer', 'took', 'galley', 'type', 'scrambled', 'make', 'type', 'specimen', 'book', '.', 'survived', 'five', 'centuries', ',', 'also', 'leap', 'electronic', 'typesetting', ',', 'remaining', 'essentially', 'unchanged', '.', 'popularised', '1960s', 'release', 'Letraset', 'sheets', 'containing', 'Lorem', 'Ipsum', 'passages', ',', 'recently', 'desktop', 'publishing', 'software', 'like', 'Aldus', 'PageMaker', 'including', 'versions', 'Lorem', 'Ipsum', '.']