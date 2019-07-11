import sys

from io import StringIO
from nltk.ccg import lexicon

from nltk.ccg.chart import CCGChartParser, DefaultRuleSet, printCCGDerivation
from .models import Rule, Primitive

SENTENCE_SAMPLE = "she has a book"

LEX_SAMPLE = '''
:- S, NP, N
she => NP {she}
has => (S\\NP)/NP {\\x y.have(y, x)}
a => ((S\\NP)\\((S\\NP)/NP))/N {\\P R x.(exists z.P(z) & R(z,x))}
book => N {book}
'''


def derive(sentence):
    words = sentence.split()
    prims = Primitive.objects.all().values_list('label', flat=True)
    rules = Rule.objects.filter(label__in=words)
    prims_formed = [':- ' + ', '.join(prims)]
    rules_list = rules.values_list('label', 'syntactic', 'semantic')
    rules_formed = [f'{la} => {sy} {{{se}}}' for la, sy, se in rules_list]
    lex_string = '\n'.join(prims_formed + rules_formed)

    lex = lexicon.fromstring(lex_string, True)
    parser = CCGChartParser(lex, DefaultRuleSet)
    parsed = list(parser.parse(words))

    # HACK: redirect stdout to variable
    dummyIO = StringIO()
    sys.stdout = dummyIO
    printCCGDerivation(parsed[0])
    stolen = dummyIO.getvalue()
    sys.stdout = sys.__stdout__

    derivation_process = stolen.split('\n')

    result = {
        'sentence': sentence,
        'logicalform': derivation_process[-2].strip(),
        'derivation': derivation_process,
        'lexicon': prims_formed + rules_formed
    }

    return result
