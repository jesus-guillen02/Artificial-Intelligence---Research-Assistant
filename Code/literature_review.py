import PyPDF2 # Used for reading and extracting information from PDF Files
import nltk
import re
import json
from PyPDF2 import PdfReader
from nltk.corpus import stopwords
from transformers import pipeline
from gensim import corpora,  models

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)  # Using PdfReader instead of PdfFileReader
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return None

summarizer = pipeline("summarization")

def summarize_text(text, max_chunk=1024):
    # Split the text into chunks
    chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
    summary = ""

    for chunk in chunks:
        try:
            # Summarize each chunk
            part_summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
            summary += part_summary[0]['summary_text'] + " "
        except Exception as e:
            print(f"Error in summarizing text chunk: {e}")

    return summary.strip()

def perform_topic_modeling(text): # Performs topic modeling on the given text
    stop_words = stopwords.words('english')

    # Tokens and stopwords removal from the text
    words = [word for word in text.lower().split() if word not in stop_words]

    # Building the term dictionary
    dictionary = corpora.Dictionary([words])
    corpus = [dictionary.doc2bow(words)]

    # Applying the LDA Model
    lda_model = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)
    topics = lda_model.print_topics(num_words=4)

    for topic in topics:
        print(f"Topic: {topic}")

def extract_citations(text):
    # APA citation pattern (e.g., (Smith, 2020))
    citation_pattern = re.compile(r'\([A-Za-z]+, \d{4}\)')
    citations = citation_pattern.findall(text)
    return citations

def store_citations(citations, file_path = 'citations.json'):
    with open(file_path, 'w') as file:
        json.dump(citations, file, indent=4)
    print(f"Citations stored in {file_path}")

def format_citations(citations): # Formats the list of citations.
    # Basic formatter for APA style
    formatted = "\n".join(sorted(set(citations)))
    return formatted

def run():  # Compiles, used to run the functions in a seperate block from the if __NAME__ call
    print("Welcome to the Literature Review Assistant!")
    pdf_path = input("Enter the path of your PDF file: ")

    # Extracting text from PDF
    text = extract_text_from_pdf(pdf_path)

    # Summarizing text
    print("\nSummary of the Document:")
    print(summarize_text(text))

    # Extracting and managing citations
    citations = extract_citations(text)
    if citations:
        print("\nExtracted Citations:")
        print(format_citations(citations))
        store_citations(citations)
    else:
        print("\nNo citations found.")

    # Topic Modeling
    print("\nIdentified Topics:")
    perform_topic_modeling(text)

if __name__ == "__main__":
    run()