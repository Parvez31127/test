from flask import Flask, render_template, request, jsonify
from graphqlclient import GraphQLClient

app = Flask(__name__)

# Sample stock data stored in a dictionary
stock_data = {
    "AAPL": {
        "symbol": "AAPL",
        "historical_prices": [150.0, 151.0, 152.0, 153.0, 154.0],
        "highest_price": 155.0,
        "lowest_price": 149.0,
        "trading_volume": 1000000,
    },
    "GOOGL": {
        "symbol": "GOOGL",
        "historical_prices": [2500.0, 2510.0, 2520.0, 2530.0, 2540.0],
        "highest_price": 2550.0,
        "lowest_price": 2490.0,
        "trading_volume": 500000,
    },
}

# Initialize the GraphQL client
graphql_client = GraphQLClient(
    "http://localhost:5000/graphql"
)  # Replace with your GraphQL server URL


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/query", methods=["POST"])
def query_stock():
    stock_symbol = request.form["stock_symbol"]

    # Define the GraphQL query
    query = f"""
    {{
        stock(symbol: "{stock_symbol}") {{
            symbol
            historicalPrices
            highestPrice
            lowestPrice
            tradingVolume
        }}
    }}
    """

    # Send the query to the GraphQL server
    response = graphql_client.execute(query)

    return jsonify({"data": response})


if __name__ == "__main__":
    app.run(debug=True)
