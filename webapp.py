from flask import Flask, render_template, request, redirect
from som_basic import base_func
import os
import time

app = Flask(__name__)

app.debug = True


@app.route("/")
def main_page():
   return(redirect('/entry'))


@app.route('/entry')
def entry_page() -> 'html':
    return(render_template('entry.html',
                           the_title = "Самоорганизующиеся карты"))


@app.route('/create_map')
def create_map() -> 'html':
    dataset = '/home/bakunobu/release/test_data1.xlsx'
    params = request.form['params']
    size = request.form['size']
    base_func('/home/bakunobu/release/test_data1.xlsx')
    time.sleep(120)
    return render_template('results.html',
                           the_title='Параметры модели',
                           the_dataset=dataset,
                           the_params=params,
                           the_size=size)
    

    
@app.route('/result', methods=['POST'])
def return_result() -> 'html':
    time.sleep(88)

    return render_template('image.html', the_title = "Карта построена",
                           the_dataset = '/home/bakunobu/release0.2/test_data1.xlsx',
                           the_params = 'epochs=100, alpha=0.01',
                           the_size = '(25, 25)')



if __name__ == "__main__":
    app.run()