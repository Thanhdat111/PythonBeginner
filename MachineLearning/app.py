import pandas as pd
from sklearn.tree import DecisionTreeClassifier
# library to split data train and test
from sklearn.model_selection import train_test_split
# calculate accuracy of predictions
from sklearn.metrics import accuracy_score
music_data = pd.read_csv('music.csv')
# import model trained to file
from sklearn.externals import joblib
# clean data not null
# split data set into two separate, one is input and one is put put
# input(age,gender) output(kind_of_music)
# run 1 time
X = music_data.drop(columns=['genre'])
Y = music_data['genre']
# split two train and test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
model = DecisionTreeClassifier()
# train model
model.fit(X, Y)
# after train model we import model to file
joblib.dump(model, 'music-recommender.joblib')
# import model from file train

model_train = joblib.load('music-recommender.joblib')
# prediction with age 21 male and age 22 female
predictions = model.predict([[21, 1], [22, 0]])
predictions2 = model.predict(X_test)

# calculate of predictions
score = accuracy_score(Y_test, predictions2)

print(predictions)

# accuracy of prediction
# split to two separate Xtrain and XTest (Train 80% and Test 20%)


