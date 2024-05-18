from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        operator_dict = {}
        keys = ['Attack Rate', 'Decay Rate', 'Sustain Rate', 'Release Rate', 'Attack Level', 'Decay Level', 'Sustain Level', 'Release Level']
        previous_rate_value = 0

        for key in keys:
            value = float(request.form[key])
            if key.endswith("Rate"):
                value = 101 - value
            if key.endswith("Rate"):
                value += previous_rate_value
                previous_rate_value = value
            operator_dict[key] = value

        return render_template('result.html', operator_dict=operator_dict)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
