import csv
from app import db, TradeData

db.create_all()

with open('stock_market_data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        trade = TradeData(
            date=row['date'],
            trade_code=row['trade_code'],
            open=float(row['open']),
            high=float(row['high']),
            low=float(row['low']),
            close=float(row['close']),
            volume=int(row['volume'])
        )
        db.session.add(trade)
    db.session.commit()
