from flask import Flask, render_template, jsonify
import re
import urllib.parse

app = Flask(__name__)
vowel_list = ['A', 'E', 'I', 'O', 'U']
suffix = 'ay'


def arrangeConsonantWord(word):
    '''
    Using given word find where to re-arrange for Pig Latin.
    '''
    for i, letter in enumerate(word[1:], start=1):
        if letter.upper() in vowel_list:
            first_letter = word[i].upper() if word[0].isupper() else word[i]
            return first_letter + word[i + 1:] + word[0:i].lower() + suffix
    return word[1].upper() + word[2:].lower() + word[0].lower() + suffix


def convertToPigLatin(word):
    '''
    Check if given word start with a vowel otherwise pass it on.
    '''
    if word[0].upper() in vowel_list:
        return word + suffix

    return arrangeConsonantWord(word)


# API Routes


@app.route('/')
def index():
    '''
    Render index page which allows users to make Ajax calls to API.
    '''
    return render_template('index.html')


@app.route('/api/plq/<plq_str>/')
def convertPLQ(plq_str):
    '''
    Clean and prepare given query string for Pig Latin conversion.
    '''
    query_str = urllib.parse.unquote_plus(plq_str)

    word_list = re.findall(r'\w+', query_str)
    pig_latin_list = []
    for word in word_list:
        pig_latin_list.append(convertToPigLatin(word))

    template = re.sub(r'\w+', '{}', query_str)
    return jsonify(data={
        'plq': query_str,
        'result': template.format(*pig_latin_list)
    })
