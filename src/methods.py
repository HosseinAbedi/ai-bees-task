import os
from util import generate_comment
from database import insert_one

def generate_comment_endpoint(post):
    result = generate_comment(post)
    insert_one(os.getenv('MONGODB_DATABASE'), os.getenv('MONGODB_COLLECTION'), {"named_entities": result['named_entities'], "comment": result['comment'], "category": result["category"]})
    return result
