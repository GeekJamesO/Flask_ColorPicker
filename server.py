from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "ThisSoundBeSuperSpecialAndSecret123"

@app.route('/')
def root():
    return render_template("index.html")

def getColorFromForm(request, valueName):
    value = request.form[valueName]
    return max(0, value)

@app.route('/process', methods=['POST'])
def process():
    session['redValue']   = getColorFromForm(request, 'redValue')
    session['greenValue'] = getColorFromForm(request, 'greenValue')
    session['blueValue']  = getColorFromForm(request, 'blueValue')
    return redirect('/')

app.run(debug=True)
