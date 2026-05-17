from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    hcf = lcm = reversed_string = None
    factorials = {}

    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        text = request.form['text']

        hcf = math.gcd(num1, num2)
        lcm = (num1 * num2) // hcf

        reversed_string = text[::-1]

        for i in range(4, 9):
            factorials[i] = math.factorial(i)

    return render_template(
        'index.html',
        hcf=hcf,
        lcm=lcm,
        reversed_string=reversed_string,
        factorials=factorials
    )

if __name__ == '__main__':
    app.run(debug=True)
