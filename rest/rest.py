from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample initial stock data
stocks = [
    {"name": "Apple Inc.", "symbol": "AAPL", "price": 150.0},
    {"name": "Google LLC", "symbol": "GOOGL", "price": 2700.0},
]


# Route to add a new stock
@app.route("/stocks", methods=["POST"])
def add_stock():
    data = request.get_json()
    # Check if all required fields are present
    if not all(key in data for key in ["name", "symbol", "price"]):
        return jsonify({"error": "Incomplete data"}), 400

    # Create a new stock object
    new_stock = {
        "name": data["name"],
        "symbol": data["symbol"],
        "price": data["price"],
    }

    # Add the new stock to the list of stocks
    stocks.append(new_stock)

    return jsonify({"message": "Stock added successfully"}), 201


# Route to retrieve a list of all stocks
@app.route("/stocks", methods=["GET"])
def get_stocks():
    return jsonify(stocks)


if __name__ == "__main__":
    app.run(debug=True)
