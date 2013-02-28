from flask import Flask

app = Flask(__name__)


def filter_word(word):
    return word.replace('+', ' ')

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
    app.run()
