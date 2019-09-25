from flask import Flask, escape, request, render_template, jsonify
import re, string
import urllib.parse

app = Flask(__name__)
vowel_list = ['A', 'E', 'I', 'O', 'U']
suffix = 'ay'


def arrangeConsonantWord(word):
    for i, letter in enumerate(word[1:], start=1):
        if letter.upper() in vowel_list:
            first_letter = word[i].upper() if word[0].isupper() else word[i]
            return first_letter + word[i + 1:] + word[0:i].lower() + suffix
    return word[1:] + word[0] + suffix


def convertToPigLatin(word):
    if word[0].upper() in vowel_list:
        return word + suffix

    return arrangeConsonantWord(word)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/plq/<plq_str>/')
def convertPLQ(plq_str):
    # query_str = request.args.get('q', 'Hello, my name is Alice.')
    query_str = urllib.parse.unquote_plus(plq_str)
    query_str = escape(query_str)

    query_str = re.sub(r'[^\w\s]', '', query_str)
    word_list = re.split(r'\s', query_str)

    pig_latin_list = []

    for word in word_list:
        pig_latin_list.append(convertToPigLatin(word))

    return jsonify(data={'plq': query_str, 'result': ' '.join(pig_latin_list)})
