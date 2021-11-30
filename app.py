from flask import Flask, render_template, request
import pandas as pd
import model



app = Flask(__name__, template_folder='template')


@app.route("/", methods = ["GET", "POST"])
def func():

    if request.method == "POST":

        movement_reaction = request.form["movement_reaction"]
        mentality_composure = request.form["mentality_composure"]
        potential = request.form["potential"]
        passing = request.form["passing"]
        dribbling = request.form["dribbling"]
        power_shot_power = request.form["power_shot_power"]
        mentality_vision = request.form["mentality_vision"]
        attacking_short_passing = request.form["attacking_short_passing"]

        array = [movement_reaction, mentality_composure, potential, passing, dribbling, power_shot_power, mentality_vision, attacking_short_passing]
        array = pd.to_numeric(array)
        prediction = model.dct.predict([array])
        print(prediction)

    return render_template("index.html", output = prediction)

if __name__ == "__main__":
    app.run(debug=True)