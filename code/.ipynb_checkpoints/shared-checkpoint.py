import time
import nltk
from nltk.corpus import wordnet
from collections import defaultdict

def time_it(func, args):
    start = time.time()
    res = func(args)
    elapsed = time.time() - start
    log_line = f'Elapsed time for {func}: {elapsed}'
    return {'res': res, 'elapsed': elapsed, 'log': log_line}

def get_elapsed(start):
    return time.time() - start

def print_elapsed(start):
    elapsed = time.time() - start
    print(f'Elapsed time for operation: {elapsed}')
    
## Perform Part-Of-Speech (POS) tagging on tokens
def my_pos_tag(tok_list):
    pos_tagged = nltk.pos_tag(tok_list)
    tags = {
        'n' : wordnet.NOUN,
        'v' : wordnet.VERB,
        'j' : wordnet.ADJ,
        'r' : wordnet.ADV
    }
    tag_dict = defaultdict(lambda: wordnet.NOUN, tags)
    new_tags = [(tok, tag_dict[pos[0].lower()]) for (tok, pos) in pos_tagged]
    return new_tags
