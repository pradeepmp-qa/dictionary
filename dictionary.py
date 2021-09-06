from flask import Flask, render_template, request
from textblob import Word

# initialse the application
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('form.html')

@app.route('/submit' , methods = ["POST"])
def form_data():
   input_text = request.form.get('input_text')
   word_meaning = Word(input_text).definitions

   
   return render_template('predict.html' , meaning_data = f' {word_meaning}')
#    return render_template('predict.html' , sentence_data = f'Number of sentences are {sentence_length}')
if __name__ == '__main__':
    app.run(debug = True)

