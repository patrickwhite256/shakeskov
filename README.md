Shakeskov
=========

I wanted to see how simple predictive text could be.
The answer: stupidly simple.

This is a 1-gram Markov Chain sentence generator that uses Hamlet's seven soliloquys as the corpus.

Usage
-----
The generator itself is written in pure Python (3) and is less than 100 lines:
`python3 sharkov.py`

There's also a web wrapper for it. It uses Flask.

    pip install -r requirements.txt
    python3 server.py

[See a live demo.](http://patrickwhite.io/shakeskov)
