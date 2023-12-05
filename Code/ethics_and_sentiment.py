import textblob
from textblob import TextBlob
import re

# Function to perform sentiment analysis
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity, analysis.sentiment.subjectivity

# Function to detect potential biases in text
def detect_bias(text):
    bias_indicators = {
        # Gender Bias
        'he': len(re.findall(r'\bhe\b', text, re.IGNORECASE)),
        'she': len(re.findall(r'\bshe\b', text, re.IGNORECASE)),
        'man': len(re.findall(r'\bman\b', text, re.IGNORECASE)),
        'woman': len(re.findall(r'\bwoman\b', text, re.IGNORECASE)),
        # Additional gender terms...

        # Racial and Ethnic Bias
        'black': len(re.findall(r'\bblack\b', text, re.IGNORECASE)),
        'white': len(re.findall(r'\bwhite\b', text, re.IGNORECASE)),
        'asian': len(re.findall(r'\basian\b', text, re.IGNORECASE)),
        'hispanic': len(re.findall(r'\bhispanic\b', text, re.IGNORECASE)),
        'latino': len(re.findall(r'\blatino\b', text, re.IGNORECASE)),
        'latina': len(re.findall(r'\blatina\b', text, re.IGNORECASE)),
        'native american': len(re.findall(r'\bnative american\b', text, re.IGNORECASE)),
        # Additional racial and ethnic terms...

        # Age Bias
        'young': len(re.findall(r'\byoung\b', text, re.IGNORECASE)),
        'old': len(re.findall(r'\bold\b', text, re.IGNORECASE)),
        'teenager': len(re.findall(r'\bteenager\b', text, re.IGNORECASE)),
        'elderly': len(re.findall(r'\belderly\b', text, re.IGNORECASE)),
        # Additional age-related terms...

        # Nationality Bias
        'american': len(re.findall(r'\bamerican\b', text, re.IGNORECASE)),
        'foreign': len(re.findall(r'\bforeign\b', text, re.IGNORECASE)),
        'immigrant': len(re.findall(r'\bimmigrant\b', text, re.IGNORECASE)),
        # Additional nationality terms...

        # Disability Bias
        'disabled': len(re.findall(r'\bdisabled\b', text, re.IGNORECASE)),
        'handicapped': len(re.findall(r'\bhandicapped\b', text, re.IGNORECASE)),
        'wheelchair': len(re.findall(r'\bwheelchair\b', text, re.IGNORECASE)),
        # Additional disability terms...

        # Socioeconomic Bias
        'poor': len(re.findall(r'\bpoor\b', text, re.IGNORECASE)),
        'wealthy': len(re.findall(r'\bwealthy\b', text, re.IGNORECASE)),
        'affluent': len(re.findall(r'\baffluent\b', text, re.IGNORECASE)),
        'low-income': len(re.findall(r'\blow-income\b', text, re.IGNORECASE)),
        # Additional socioeconomic terms...

        # Religious Bias
        'christian': len(re.findall(r'\bchristian\b', text, re.IGNORECASE)),
        'muslim': len(re.findall(r'\bmuslim\b', text, re.IGNORECASE)),
        'jewish': len(re.findall(r'\bjewish\b', text, re.IGNORECASE)),
        'hindu': len(re.findall(r'\bhindu\b', text, re.IGNORECASE)),
        'buddhist': len(re.findall(r'\bbuddhist\b', text, re.IGNORECASE)),
        'atheist': len(re.findall(r'\batheist\b', text, re.IGNORECASE)),
        'agnostic': len(re.findall(r'\bagnostic\b', text, re.IGNORECASE)),
        # Additional religious terms...

        # Sexual Orientation Bias
        'gay': len(re.findall(r'\bgay\b', text, re.IGNORECASE)),
        'lesbian': len(re.findall(r'\blesbian\b', text, re.IGNORECASE)),
        'bisexual': len(re.findall(r'\bbisexual\b', text, re.IGNORECASE)),
        'transgender': len(re.findall(r'\btransgender\b', text, re.IGNORECASE)),
        # Additional terms related to sexual orientation...
    }

    return bias_indicators

# Function to check for ethical concerns
def ethics_check(text):
    # Example: Check for derogatory terms
    derogatory_terms = ['derogatory_term1', 'derogatory_term2'] # Replace with actual terms
    for term in derogatory_terms:
        if term in text.lower():
            return False
    return True

def run():
    text = input("Enter the text for analysis: ")

    polarity, subjectivity = analyze_sentiment(text)
    print(f"Sentiment Analysis:\n Polarity: {polarity}\n Subjectivity: {subjectivity}\n")

    biases = detect_bias(text)
    print(f"Bias Detection: {biases}")

    ethical = ethics_check(text)
    if ethical:
        print("No ethical concerns detected.")
    else:
        print("Ethical concerns detected, please review the text.")

if __name__ == "__main__":
    run()
