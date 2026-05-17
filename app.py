from flask import Flask, render_template, request

app = Flask(__name__)

expenses = []

@app.route('/', methods=['GET', 'POST'])
def home():
    total = 0

    if request.method == 'POST':
        title = request.form['title']
        amount = float(request.form['amount'])

        expenses.append({
            'title': title,
            'amount': amount
        })

    total = sum(item['amount'] for item in expenses)

    return render_template(
        'index.html',
        expenses=expenses,
        total=total
    )

if __name__ == '__main__':
    app.run(debug=True)