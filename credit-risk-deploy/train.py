import os
import numpy as np
import pandas as pd

# tell matplotlib not to use QT and other GUI libraries
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.externals import joblib

from config import MODELS_DIR

def encode_column(df, column):
    """Encodes a column in the dataframe using LabelEncoder.

    This functions creates a LabelEncoder, fits it using the given column and
    also replaces that column in the data frame with a new column with encoded values.

    Returns the created LabelEncoder object.

    :param df: the data frame
    :param column: the name of the column to encode
    :return: returns the encoder object
    """
    encoder = LabelEncoder()
    encoder.fit(df[column])
    df[column] = encoder.transform(df[column])
    return encoder

def save_model(model, filename):
    """Saves the given model ine models directory with the
    """
    # create directory if not already present
    os.makedirs(MODELS_DIR, exist_ok=True)
    path = os.path.join(MODELS_DIR, filename)
    joblib.dump(model, path)
    print("  saved", path)


print("reading the dataset...")
df = pd.read_csv("data/historical_loan.csv")

print("replacing missing values with mean...")
df.years = df.years.fillna(np.mean(df.years))

print("encoding the columns...")
grade_encoder = encode_column(df, "grade")
ownership_encoder = encode_column(df, "ownership")

# build the model
print("building the model...")
X = df.iloc[:,1:]
y = df.iloc[:,0]
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# save the model and encoders
print("saving the models...".format(MODELS_DIR))
save_model(model, "model.pkl")
save_model(grade_encoder, "grade-encoder.pkl")
save_model(ownership_encoder, "ownership-encoder.pkl");

print("done")
