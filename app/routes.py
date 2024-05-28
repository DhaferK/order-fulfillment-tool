from flask import Blueprint, render_template, request
import pandas as pd
from data_processing import analyze_orders
from optimization import economic_order_quantity

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            data = pd.read_csv(file)
            order_analysis = analyze_orders(data)
            eoq = economic_order_quantity(order_analysis['TotalVolume'], 5, 100)
            return render_template('results.html', analysis=order_analysis, eoq=eoq)
    return render_template('index.html')

