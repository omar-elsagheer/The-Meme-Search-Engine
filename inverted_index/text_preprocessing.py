from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import os

# ______________Constants__________________________
file_path = 'C:\\Users\\Omar\\Desktop\\CMPS 391\\Project\\Data\\Documents\\'
# Tokenization and Preprocessing
stemmer = SnowballStemmer('english')
wnl = WordNetLemmatizer()



# ______________Clean the Text for Single Inverted Index _____________________________
# get all files
def get_files():
    """Get the files in a directory"""
    directory = r'C:\\Users\\Omar\\Desktop\\CMPS 391\\Project\\Data\\Documents'
    return os.listdir(directory)


def get_text(file):
    s = ''
    f = open(file_path + file, 'r')
    for text in f:
        s = s + text.replace('\n', ' ')
    return s.split()


def stem_and_lem(s1):
    """Stem the text, remove numbers and stopwords and non-english characters.\n
    Returns a list\n
    s1: set, list"""
    s2 = []
    s3 = []
    # Remove non-alphabetical characters
    for i in s1:
        if i.isalnum():
            s2.append(i)
    # Normalize and Stem
    for i in s2:
        s3.append(wnl.lemmatize(i.lower())) if wnl.lemmatize(i).endswith('es') or wnl.lemmatize(i).endswith(
            'e') or wnl.lemmatize(i).endswith('y') else s3.append(stemmer.stem(i))
    # Remove Stop Words
    return s3
