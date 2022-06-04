import sys
import os
sys.path.insert(1, 'src')
from util import get_comment, categorize_text, get_named_entities


def test_util():
    assert isinstance(get_comment(""), list)
    assert isinstance(categorize_text('Iphone is a good brand!'), dict)
    assert isinstance(get_named_entities('I live in New York and work at Amazon.'), list)
    
    
