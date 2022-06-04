from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification
import datefinder

ENTITIES = {'B-ORG': 'Company', 'B-LOC': 'Location', 'B-PER': 'Person'} 
LABELS = ['Sports', 'Technology', 'Medicine', "Politics", "Arts"]
TOKENIZER = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
MODEL = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
NLP = pipeline("ner", model=MODEL, tokenizer=TOKENIZER)
CLASSIFIER = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")
SUMMARIZER = pipeline("summarization", model="philschmid/distilbart-cnn-12-6-samsum")

def get_comment(text):
    return SUMMARIZER(text, max_length=min([11, len(text.split())]))['summary_text']

def categorize_text(text):
    res =  CLASSIFIER(text, LABELS, multi_label=True)
    return dict(zip(res['labels'], res['scores']))

def get_named_entities(text):
    res = NLP(text)
    temp = []
    for elem in res:
        temp.append({ENTITIES[elem['entity']]: elem['word']})
    dates = datefinder.find_dates(text)
    for date in dates:
        temp.append({"Date": str(date.date())})
    return temp

def generate_comments(post):
    named_entities = get_named_entities(post)
    categories = categorize_text(post)
    comment = get_comment(post)
    return {"categories": categories,
            "named_entities": named_entities,
            "comment": comment}


if __name__ == "__main__":
    pass
    # res = categorize_text(text='Iphone')
    # print(get_named_entities('My name is Sarah and I live in London and I work at Google I will leave on March 6th 2020'))