#Load the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.externals import joblib

df = pd.read_csv("data/historical_loan.csv")

# Let's replace missing values with mean
# There's a fillna function
df.years = df.years.fillna(np.mean(df.years))

df_encoded = df.copy()
le_grade = LabelEncoder()
# fit label encoder
le_grade = le_grade.fit(df.grade)
df_encoded.grade = le_grade.transform(df_encoded.grade)

le_ownership = LabelEncoder()
le_ownership = le_ownership.fit(df["ownership"])
df_encoded.ownership = le_ownership.transform(df_encoded.ownership)


X = df_encoded.iloc[:,1:]
y = df_encoded.iloc[:,0]
final_model = RandomForestClassifier(n_estimators=100)
final_model = final_model.fit(X, y)

joblib.dump(final_model, "model.pkl")
joblib.dump(le_grade, "le_grade.pkl")
joblib.dump(le_ownership, "le_ownership.pkl");

print("done")
