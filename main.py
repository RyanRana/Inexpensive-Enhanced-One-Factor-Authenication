import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Load your data
data = pd.read_csv('login_data.csv')

# Extract features and labels
X = data[['User ID', 'Login Time', 'Input Destination', 'End Destination', 'Device Type', 'Browser Type',
          'Previous Login Success', 'Failed Attempts', 'Account Age', 'Session Duration', 'Typical Login Time',
          'IP Reputation', 'Geo-location Change', 'Unusual Activity']]
y = data['Malicious']

# Convert categorical features to category dtype
categorical_features = ['Input Destination', 'End Destination', 'Device Type', 'Browser Type', 
                        'Previous Login Success', 'Typical Login Time', 'IP Reputation', 
                        'Geo-location Change', 'Unusual Activity']
for col in categorical_features:
    X[col] = X[col].astype('category')

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['User ID', 'Login Time', 'Failed Attempts', 'Account Age', 'Session Duration']),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Create a pipeline that first preprocesses the data and then applies logistic regression
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=1000))
])

# Train the model
pipeline.fit(X_train, y_train)

# Predict on the test set
y_pred = pipeline.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_pred))
