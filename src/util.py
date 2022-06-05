import os
import numpy as np
import datefinder
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification

STARTER_ENTITIES = ['I-ORG', 'I-LOC', 'I-PER', "I-MISC", "O", "B-MISC"]
ENTITIES = {'B-ORG': 'Company', 'B-LOC': 'Location', 'B-PER': 'Person'} 
LABELS = ['Sports', 'Technology', 'Medicine', "Politics", "Arts"]
TOKENIZER = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
MODEL = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
NLP = pipeline("ner", model=MODEL, tokenizer=TOKENIZER)
CLASSIFIER = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")
SUMMARIZER = pipeline("summarization", model="philschmid/distilbart-cnn-12-6-samsum")

def get_comment(text):
    return SUMMARIZER(text)

def categorize_text(text):
    res =  CLASSIFIER(text, LABELS, multi_label=True)
    return res['labels'][np.argmax(res['scores'])] 

def get_named_entities(text):
    res = NLP(text)
    temp = []
    for elem in res:
        if elem['entity'] not in STARTER_ENTITIES:
            temp.append({ENTITIES[elem['entity']]: elem['word']})
    dates = datefinder.find_dates(text)
    for date in dates:
        temp.append({"Date": str(date.date())})
    return temp

def generate_comment(post):
    named_entities = get_named_entities(post)
    category = categorize_text(post)
    comment = get_comment(post)
    if comment:
        comment = comment[0]['summary_text']
    else:
        comment = ''
    result = {"category": category,
              "named_entities": named_entities,
              "comment": comment}
    return result
