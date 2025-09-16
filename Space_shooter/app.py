from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# store game parameters in memory for now
game_params = {"spaceship_speed": 5}

@app.route("/")
def index():
    return render_template("index.html")  # frontend sliders page

@app.route("/get_params", methods=["GET"])
def get_params():
    return jsonify(game_params)

@app.route("/set_params", methods=["POST"])
def set_params():
    data = request.get_json()
    if "spaceship_speed" in data:
        game_params["spaceship_speed"] = float(data["spaceship_speed"])
    return jsonify(success=True, params=game_params)

if __name__ == "__main__":
    app.run(debug=True)
