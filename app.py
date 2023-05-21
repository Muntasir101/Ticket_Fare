from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate_cost():
    distance = int(request.form['distance'])
    departure_date = int(request.form['departure_date'])
    service_class = request.form['service_class']

    if distance < 500:
        cost = 100
    elif distance >= 500 and distance <= 1000:
        if departure_date <= 7:
            cost = distance * 0.10
        elif departure_date <= 30:
            cost = distance * 0.08
        elif departure_date <= 90:
            cost = distance * 0.06
    else:
        if departure_date <= 7:
            cost = distance * 0.30
        elif departure_date <= 30:
            cost = distance * 0.25
        elif departure_date <= 90:
            cost = distance * 0.20

        if service_class == "Business":
            cost *= 2
        elif service_class == "First":
            cost *= 3

    return render_template('result.html', cost=cost)


if __name__ == '__main__':
    app.run(debug=True)
