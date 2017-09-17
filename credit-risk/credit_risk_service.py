"""Service to expose the credit risk model as an API.
"""
from sklearn.externals import joblib

# read the encoders and the model
grade_encoder = joblib.load("le_grade.pkl")
ownership_encoder = joblib.load("le_ownership.pkl")
model = joblib.load("model.pkl")

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
    
