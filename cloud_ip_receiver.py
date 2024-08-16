from flask import Flask, request, jsonify

app = Flask(__name__)
IP_FILE = "last_ip.txt"


def load_last_ip():
    try:
        with open(IP_FILE, "r") as file:
            ips = file.readlines()
            return ips[-1].strip() if ips else None
    except FileNotFoundError:
        return None


def save_last_ip(ip):
    with open(IP_FILE, "a") as file:
        file.write(ip + "\n")


@app.route('/update-ip', methods=['POST'])
def update_ip():
    data = request.get_json()
    if "ip" in data:
        ip = data["ip"]
        save_last_ip(ip)
        return jsonify({"message": "IP updated successfully", "ip": ip}), 200
    return jsonify({"message": "Invalid request"}), 400


@app.route('/', methods=['GET'])
def show_last_ip():
    last_ip = load_last_ip()
    if last_ip:
        # return jsonify({"last_ip": last_ip}), 200
        return last_ip
    return jsonify({"message": "No IP received yet"}), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
