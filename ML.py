import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report

# Assuming 'md' is your DataFrame
# Convert categorical features to numerical using one-hot encoding
md = pd.get_dummies(md, columns=['sex', 'smoker', 'region'])

# Define features (X) and target variable (y)
X = md.drop('charges', axis=1)
y = (md['charges'] > 50000).astype(int)  # 1 if charges > 50000, else 0

# Split data into training and testing sets
X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a logistic regression model
model = LogisticRegression(max_iter=1000)  # Increased max_iter to ensure convergence

# Train the model
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Print the evaluation metrics
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)
