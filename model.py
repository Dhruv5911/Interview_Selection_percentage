print("MODEL TRAINING STARTED")

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import matplotlib.pyplot as plt
import os

df = pd.read_csv("student_data.csv")

df["mcat_marks"] = df["mcat_marks"].fillna(df["mcat_marks"].median())
df["cgpa"] = df["cgpa"].fillna(df["cgpa"].median())

df.loc[df["mcat_marks"] > 150, "mcat_marks"] = 150
df.loc[df["mcat_marks"] < 0, "mcat_marks"] = 0

df["Selection"] = (df["mcat_marks"] / 150) * 60 + (df["cgpa"] / 10) * 40

X = df[["mcat_marks", "cgpa"]]
y = df["Selection"]
z=df['mcat_marks']
plt.plot(X,y)
plt.show()

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("MODEL SAVED")
print("FILE SIZE:", os.path.getsize("model.pkl"))
