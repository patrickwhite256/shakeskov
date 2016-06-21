import re
import random
from collections import defaultdict

BOS = object()
EOS = object()

PUNCTUATION = ';:,'
SENTENCE_ENDERS = '.!?'


def generate_tokens(corpus):
    words = re.split(r'\s+', corpus)
    tokens = [BOS]
    for word in words:
        if not word:
            continue
        if word[-1] in PUNCTUATION:
            tokens.append(word[:-1].lower())
            tokens.append(word[-1])
        elif word[-1] in SENTENCE_ENDERS:
            tokens.append(word[:-1].lower())
            tokens.append(word[-1])
            tokens.append(EOS)
            tokens.append(BOS)
        else:
            tokens.append(word.lower())
    if tokens[-1] is BOS:
        tokens.pop()
    if tokens[-1] is not EOS:
        tokens.append(EOS)
    return tokens


def build_model(tokens):
    model = defaultdict(list)
    for i, token in enumerate(tokens):
        if i == len(tokens) - 1:
            break
        next_token = tokens[i + 1]
        model[token].append(next_token)
    return model


def format_token(token):
    if token in 'oi':
        return token.upper()
    return token


def generate_sentence(model, min_length=0):
    while True:
        sentence = ''
        token = random.choice(model[BOS])
        while token not in SENTENCE_ENDERS:
            if token not in PUNCTUATION:
                sentence += ' '
            sentence += format_token(token)
            token = random.choice(model[token])
        sentence += token
        sentence = sentence.strip()
        sentence = sentence[0].upper() + sentence[1:]
        if len(sentence) >= min_length:
            break
    return sentence


def main():
    with open('hamlet.txt') as infile:
        corpus = infile.read()
    tokens = generate_tokens(corpus)
    model = build_model(tokens)
    sentence = generate_sentence(model)
    print(sentence)


if __name__ == '__main__':
    main()
