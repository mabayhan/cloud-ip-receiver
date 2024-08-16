from flask import Flask, request, jsonify

app = Flask(__name__)
last_ip = None


@app.route('/update-ip', methods=['POST'])
def update_ip():
    global last_ip
    data = request.get_json()
    if "ip" in data:
        last_ip = data["ip"]
        return jsonify({"message": "IP updated successfully", "ip": last_ip}), 200
    return jsonify({"message": "Invalid request"}), 400


@app.route('/get-last-ip', methods=['GET'])
def get_last_ip():
    if last_ip:
        return jsonify({"last_ip": last_ip}), 200
    return jsonify({"message": "No IP received yet"}), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
