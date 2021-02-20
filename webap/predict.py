# import streamlit as st
# import pandas as pd 
# import matplotlib as plt
# import  seaborn as sns
# import os
# import pickle
# from sklearn.preprocessing import StandardScaler
# from sklearn.impute import SimpleImputer
# import pandas as pd
# import numpy as np
# from sklearn.preprocessing import LabelEncoder,OneHotEncoder
# from sklearn.model_selection import train_test_split
# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers
# from sklearn.model_selection import train_test_split
# from keras.models import model_from_yaml
# from keras.models import  load_model
# from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
# import mysql.connector
# from mysql.connector import Error



# pickle_in = open('model.pkl','rb')
# classifier = pickle.load(pickle_in)
# def file_selector(folder_path='/Users/mt/Documents/TCEproject/data'):
#         filenames = os.listdir(folder_path)
#         selected_filename = st.sidebar.selectbox("Select A file", filenames)
#         return os.path.join(folder_path,selected_filename)
# filename = file_selector()
# st.info("You Selected {}".format(filename))

# data = pd.read_csv(filename)

# if st.checkbox("Show Dataset"):
#     number = st.number_input("Number of Rows to View",1,60)
#     st.dataframe(data.head(number))
    

# if st.checkbox("Please choose the features including target variable that go into the model"):
#     all_columns = data.columns.tolist()
#     selected_columns = st.multiselect("Select", all_columns)
#     new_data = data[selected_columns]
#     st.dataframe(new_data)
#     #set target Column
# target_options = data.columns
# chosen_target = st.sidebar.selectbox("Target column", (target_options))
  
# X = data.loc[:,data.columns != chosen_target]
# scaler = StandardScaler()
# scaler.fit(X)
# X = (scaler.transform(X))

# y = data[chosen_target].values
# encoder = LabelEncoder()
# encoder.fit(y)
# y= encoder.transform(y)

# X_train,X_test,y_train,y_test = train_test_split(X,y, random_state = 42)
    

# model = load_model('model.h5')


# if st.sidebar.button("Predict"):
#     Test_score = model.evaluate(X_test,y_test, verbose=0)
#     Train_score = model.evaluate(X_train,y_train, verbose = 0)
#     prediction = model.predict_classes(X_test)
#     accuracy = accuracy_score(y_test, prediction)

   
#     st.success("The accuracy is, {}".format(accuracy*100))
#     st.success("The Test accuracy is,{}".format(Test_score[1]*100))
#     st.success("The Validation accuracy is,{}".format(Train_score[1]*100))
#     st.success("The prediction is {}".format(prediction))
#     for i in range(len(prediction)):break
#     if prediction[i] == 0:
#         st.write("Low Baseline RNA log")
#     else:
#         st.write("High Baseline RNA Log")
 

 






   

    
    

    
# #     st.sidebar.text("Built with Streamlit")

# # if __name__ =="__main__":
# #     main() 