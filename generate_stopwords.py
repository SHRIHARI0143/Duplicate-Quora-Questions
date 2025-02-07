import pickle
import nltk
from nltk.corpus import stopwords

# Download stopwords if not already downloaded
nltk.download('stopwords')

# Get the stopwords set
stop_words = set(stopwords.words('english'))

# Save stopwords to a pickle file
with open('stopwords.pkl', 'wb') as f:
    pickle.dump(stop_words, f)

print("stopwords.pkl generated successfully!")
