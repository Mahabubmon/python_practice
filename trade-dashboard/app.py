from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
CORS(app)

class TradeData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50))
    trade_code = db.Column(db.String(50))
    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    close = db.Column(db.Float)
    volume = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'trade_code': self.trade_code,
            'open': self.open,
            'high': self.high,
            'low': self.low,
            'close': self.close,
            'volume': self.volume
        }

@app.route('/trades', methods=['GET'])
def get_trades():
    trades = TradeData.query.all()
    return jsonify([trade.to_dict() for trade in trades])

@app.route('/trades/<int:id>', methods=['PUT'])
def update_trade(id):
    trade = TradeData.query.get(id)
    if trade is None:
        return jsonify({'error': 'not found'}), 404

    data = request.get_json()
    trade.date = data.get('date', trade.date)
    trade.trade_code = data.get('trade_code', trade.trade_code)
    trade.open = data.get('open', trade.open)
    trade.high = data.get('high', trade.high)
    trade.low = data.get('low', trade.low)
    trade.close = data.get('close', trade.close)
    trade.volume = data.get('volume', trade.volume)
    db.session.commit()
    return jsonify(trade.to_dict())

if __name__ == '__main__':
    # Create all database tables within the Flask application context
    with app.app_context():
        db.create_all()

    # Run the Flask application
    app.run(debug=True)
