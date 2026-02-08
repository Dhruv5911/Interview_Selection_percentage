from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

print("RUNNING FROM:", BASE_DIR)
print("FILES HERE:", os.listdir(BASE_DIR))

model = joblib.load(MODEL_PATH)

@app.route("/", methods=["GET", "POST"])
def index():
    percentage = None
    decision = None

    if request.method == "POST":
        mcat = float(request.form["mcat"])
        cgpa = float(request.form["cgpa"])

        input_df = pd.DataFrame(
            [[mcat, cgpa]],
            columns=["mcat_marks", "cgpa"]
        )

        percentage = round(model.predict(input_df)[0], 2)
        decision = "LIKELY SELECTED" if percentage >= 60 else "LOW CHANCE"

    return render_template(
        "index.html",
        percentage=percentage,
        decision=decision
    )

if __name__ == "__main__":
    app.run(debug=True)
