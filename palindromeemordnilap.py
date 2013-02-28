import os
from flask import Flask, redirect

HOST = os.environ.get('HOST', '0.0.0.0')
PORT = int(os.environ.get('PORT', 5000))

app = Flask(__name__)


def filter_word(word):
    return word.replace('+', ' ')

@app.route('/')
def index():
    return redirect('/example')

@app.route('/<word>')
def hello_world(word):
    filtered_word = filter_word(word)
    word_reversed = ''.join(reversed(filtered_word))
    if ' ' in filtered_word:
        join_word = ' '
    else:
        join_word = ''
    return join_word.join([filtered_word, word_reversed])


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
