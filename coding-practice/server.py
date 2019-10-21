from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    """Show user form"""

    return render_template('form.html')

@app.route('/results', methods=['GET'])
def show_results():
    """Show user results"""

    message = request.args.get("message_type")

    return render_template('results.html',
                            messagetype=message)

@app.route('/save-name')
def save_name():

    session['name'] = request.args.get('firstname')

    return redirect('/form')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
