"""Service to predict the probability of a person to default a loan.

How to use:

    firefly predict.predict

"""
import os
from sklearn.externals import joblib
from config import MODELS_DIR

def load_model(filename):
    path = os.path.join(MODELS_DIR, filename)
    print("reading", path)
    return joblib.load(path)

# read the encoders and the model
grade_encoder = load_model("grade-encoder.pkl")
ownership_encoder = load_model("ownership-encoder.pkl")
model = load_model("model.pkl")

def predict(amount, years, age, ownership, income, grade):
    """Returns the probablity of default for given features.
    """
    # encoders work on a vector. Wrapping in a list as we only have a single value
    ownership_code = ownership_encoder.transform([ownership])[0]
    grade_code = grade_encoder.transform([grade])[0]

    # important to pass the features in the same order as we built the model
    features = [amount, grade_code, years, ownership_code, income, age]

    # probablity for not-defaulting and defaulting
    # Again, wrapping in a list as a list of features is expected
    p0, p1 = model.predict_proba([features])[0]
    return p1
