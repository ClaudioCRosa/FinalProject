from flask import Flask, render_template, request
import math
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

constant = 5.6065

@app.route('/calculate', methods=['POST'])
def calculate():
    beds = float(request.form['number1'])
    baths = float(request.form['number2'])
    housing_type = float(request.form["housing_type"])
    neighbourhood = float(request.form["neighbourhood"])
    
    checkbox_values = request.form.getlist('checkbox_value')
    additional_from_checkboxes = sum(map(float, checkbox_values))

    bed_price = beds * 0.181943
    bath_price = baths * 0.078980
    total_rooms = bed_price + bath_price

    avg_price_2019 = 946.40
    avg_price_2023 = 1795.31

    price_increase = (1799.64 / 946.4)


    all_sum = (total_rooms + housing_type + neighbourhood + additional_from_checkboxes + constant)
    price = math.exp(all_sum) * price_increase
    return render_template('result.html', bed_price=bed_price, bath_price=bath_price, total_rooms=total_rooms, all_sum=all_sum, price=price)

if __name__ == '__main__':
    app.run(debug=True)