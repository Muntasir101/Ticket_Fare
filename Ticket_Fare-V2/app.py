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
    extra_baggage = int(request.form['extra_baggage'])

    if distance < 500:
        cost = 100
        baggage_cost = 0
    elif distance >= 500 and distance <= 1000:
        if departure_date <= 7:
            cost = distance * 0.10
        elif departure_date <= 30:
            cost = distance * 0.08
        elif departure_date <= 90:
            cost = distance * 0.06
        baggage_cost = min(extra_baggage, 50) * 25
    else:
        if departure_date <= 7:
            cost = distance * 0.30
        elif departure_date <= 30:
            cost = distance * 0.25
        elif departure_date <= 90:
            cost = distance * 0.20
        baggage_cost = min(extra_baggage, 50) * 50

        if service_class == "Business":
            cost *= 2
        elif service_class == "First":
            cost *= 3

    total_cost = cost + baggage_cost

    return render_template('result.html', cost=cost, baggage_cost=baggage_cost, total_cost=total_cost)


if __name__ == '__main__':
    app.run(debug=True)
