#!/usr/bin/env python

from flask import Flask, render_template

import sharkov

app = Flask(__name__)


@app.route('/')
def main():
    with open('hamlet.txt') as infile:
        corpus = infile.read()
    tokens = sharkov.generate_tokens(corpus)
    model = sharkov.build_model(tokens)
    sentence = sharkov.generate_sentence(model)
    return render_template('main.html', sentence=sentence)


if __name__ == '__main__':
    app.run(debug=True)
