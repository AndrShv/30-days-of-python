from flask import Flask, request, jsonify

app = Flask(__name__)

pumps_status = {
    1: "stopped",
    2: "stopped"
}


# GET: Получить статус всех насосов
@app.route("/api/v1/pumps", methods=["GET"])
def get_pumps():
    # Во Flask нужно явно оборачивать словари в jsonify() для отправки JSON
    return jsonify({"pumps": pumps_status})


# POST: Переключить состояние насоса
@app.route("/api/v1/pumps/<int:pump_id>", methods=["POST"])
def toggle_pump(pump_id):
    if pump_id not in pumps_status:
        return jsonify({"error": "Pump not found"}), 404

    # Вручную забираем JSON-тело запроса
    data = request.get_json() or {}
    action = data.get("action")  # Ожидаем "start" или "stop"

    if action not in ["start", "stop"]:
        return jsonify({"error": "Invalid action. Use 'start' or 'stop'"}), 400

    pumps_status[pump_id] = "running" if action == "start" else "stopped"

    return jsonify({
        "pump_id": pump_id,
        "current_status": pumps_status[pump_id],
        "message": f"Pump successfully {pumps_status[pump_id]}"
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True)