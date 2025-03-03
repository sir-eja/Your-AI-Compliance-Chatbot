from flask import Flask, request, jsonify

app = Flask(__name__)

ORDER_DB = {
    "12345": "Your order is being prepared.",
    "67890": "Your order has been shipped."
}

@app.route('/track-order', methods=['POST'])
def track_order():
    data = request.get_json()
    order_id = data.get("order_id")
    response = ORDER_DB.get(order_id, "Order not found.")
    return jsonify({"status": response})

if __name__ == "__main__":
    app.run(port=5000, debug=True)

