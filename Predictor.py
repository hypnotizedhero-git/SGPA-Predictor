import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

data=pd.read_csv("final.csv")

X=data.drop(['SGPA','ID','NAME'],axis=1).values
Y=data['SGPA'].values.astype('float32')

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=125,random_state=None,shuffle=False)

ml=LinearRegression()
ml.fit(x_train,y_train)

y_pred=ml.predict(x_test)

# plt.figure(figsize=(15,10))
# plt.scatter(y_test,y_pred)
# plt.xlabel('Actual')
# plt.ylabel('Predicted')
# plt.title('Actual vs Predicted')

# y_pred=y_pred.round(2)

result=pd.DataFrame({'Actual':y_test,'Predicted':y_pred,'Diff.':y_pred-y_test})
result.to_csv('Difference1.csv')

# pickle.dump(ml,open('model.pkl','wb'))
# model=pickle.load(open('model.pkl','rb'))
