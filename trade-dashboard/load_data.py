import csv
from app import app, db, TradeData

# Create an application context
with app.app_context():
    # Create the database tables if they don't exist
    db.create_all()

    # Open the CSV file and read its contents
    with open('data.csv') as f:
        reader = csv.DictReader(f)
        
        # Iterate over each row in the CSV file
        for row in reader:
            # Create a TradeData object and add it to the session
            trade = TradeData(
                date=row['date'],
                trade_code=row['trade_code'],
                open=float(row['open']),
                high=float(row['high']),
                low=float(row['low']),
                close=float(row['close']),
                volume=int(row['volume'].replace(',', ''))  # Remove comma from volume string
            )
            db.session.add(trade)
        
        # Commit the changes to the database
        db.session.commit()
