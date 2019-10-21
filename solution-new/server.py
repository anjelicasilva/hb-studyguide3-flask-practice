from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = 'blahhhhhhhh'

@app.route('/')
def show_homepage():
    """Display the homepage."""

    return render_template('homepage.html')


@app.route('/form')
def show_form():

    return render_template('form.html')


@app.route('/results')
def show_results():

    message_by_type = {
        'cheery': 'A cheery message!',
        'honest': 'An honest message!',
        'dreary': 'A dreary message!'
    }
    message_type = request.args.get('message_type')

    return render_template('results.html',
                           message=message_by_type.get(message_type, '...'))


@app.route('/save-name', methods=['POST'])
def save_name():

    name = request.form.get('name')
    session['name'] = name

    return redirect('homepage.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
