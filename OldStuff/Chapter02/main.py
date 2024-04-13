import matplotlib
matplotlib.use("TkAgg")
#here we created a script to preprocess the data. This is very instructive and can be referenced when i want to preprocess other data.
from utils import preprocess
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
from keras.layers import Input
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(16)

#this is a pretty incredible program, which learns to take as input various health metrics, and as output predicts where the patient has diabetes or not.

try:
    df = pd.read_csv('Chapter02/diabetes.csv')
except:
    print("""
      Dataset not found in your computer.
      Please follow the instructions in the link below to download the dataset:
      https://raw.githubusercontent.com/PacktPublishing/Neural-Network-Projects-with-Python/master/chapter2/how_to_download_the_dataset.txt
      """)
    quit()

# Perform preprocessing and feature engineering
df = preprocess(df)
#preprocess was able to turn every data point (which, keep in mind, was already all numbers) into floats from 0-1. this is pretty incredible. It also handles missing values.

# Split the data into a training and testing set
#X is set to be all of the input data (everything but outcome), while y is the output data
X = df.loc[:, df.columns != 'Outcome']
y = df.loc[:, 'Outcome']
#the below format is quite familiar to me in machine learning with keras
#train_test_split is an extremely useful sci-kit function for the very purpose of splitting training and testing sets for ml
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Build neural network in Keras
model = Sequential([
  Input(shape=(8,)),
  Dense(32, activation='relu'),
  Dense(16, activation='relu'),
  Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=200, verbose=False)

# Results - Accuracy
scores = model.evaluate(X_train, y_train, verbose=False)
print("Training Accuracy: %.2f%%\n" % (scores[1]*100))
scores = model.evaluate(X_test, y_test, verbose=False)
print("Testing Accuracy: %.2f%%\n" % (scores[1]*100))

# Results - Confusion Matrix
# Obtain predicted probabilities
y_test_pred_probs = model.predict(X_test)

# Convert probabilities to class labels (0 or 1)
y_test_pred = np.round(y_test_pred_probs).flatten()

# Compute confusion matrix baesed off the testing data, takes the actual outcomes followed by the predicted outcomes to generate.
c_matrix = confusion_matrix(y_test, y_test_pred)

# Visualize confusion matrix using seaborn; a heatmap is simply a way to visualize it.
ax = sns.heatmap(c_matrix, annot=True, xticklabels=['No Diabetes', 'Diabetes'], yticklabels=['No Diabetes', 'Diabetes'], cbar=False, cmap='Blues')
ax.set_xlabel("Prediction")
ax.set_ylabel("Actual")
#and matplotlib is always here to plot things when we're ready.
plt.show()
plt.clf()

# Results - ROC Curve
FPR, TPR, _ = roc_curve(y_test, y_test_pred_probs)
plt.plot(FPR, TPR)
plt.plot([0,1],[0,1],'--', color='black') #diagonal line
plt.title('ROC Curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.show()
plt.clf()
