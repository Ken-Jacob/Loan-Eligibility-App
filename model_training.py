import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load and clean data
df = pd.read_csv("credit.csv")
df.dropna(inplace=True)

# Target encoding
df['Loan_Approved'] = df['Loan_Approved'].map({'Y': 1, 'N': 0})  # must be numeric

# Features
X = df.drop(['Loan_ID', 'Loan_Approved'], axis=1)
X = pd.get_dummies(X)

# Target
y = df['Loan_Approved']  # this must be a Series with 0/1

# Align features (optional, good practice if using saved model later)
X, y = X.align(y, join='left', axis=0)

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model.pkl", "wb"))
