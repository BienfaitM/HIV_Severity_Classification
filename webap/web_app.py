import streamlit as st
import pandas as pd 
import matplotlib as plt
import  seaborn as sns
import os
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from keras.models import model_from_yaml
from keras.models import  load_model
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
import mysql.connector
from mysql.connector import Error



st.set_option("deprecation.showfileUploaderEncoding", False)

st.title("HIV Severity Classifier")
st.write("Explore our ANN Classification model ")

st.sidebar.header("About App")
st.sidebar.info("This System predicts the likelihood that the infection of an HIV patient will become less severe")





pickle_in = open('model.pkl','rb')
classifier = pickle.load(pickle_in)

def main():



    def file_selector(folder_path='/Users/mt/Documents/TCEproject/data'):
        filenames = os.listdir(folder_path)
        selected_filename = st.sidebar.selectbox("Select A file", filenames)
        return os.path.join(folder_path,selected_filename)
    filename = file_selector()
    st.info("You Selected {}".format(filename))

    def connection():
        con = mysql.connector.connect(
            host       = 'localhost',
            database   = 'TCEprofile',
            user       = 'root',
            password   = '*******'
        )
        print("Connect successfully ")
        return con 
    con = connection()

    def create_db():
        cursor = con.cursor()
        try:
            query = "create table TCE (Patient VARCHAR(255),Time_Measurement VARCHAR(255), Past_Treatment_date VARCHAR(254), Past_RNA VARCHAR(254), Past_RNA_log VARCHAR(254), BaselineRNA_level VARCHAR(254), BaselineRNA_log VARCHAR(254), Nucleotide_Sequence VARCHAR(255))"
            query2 = "create table PastTreatment(id INT AUTO_INCREMENT PRIMARY KEY, drugs VARCHAR(255), duration VARCHAR(255), Patient VARCHAR(255))"
            query3 = "create table BaselineTreatment(id INT AUTO_INCREMENT PRIMARY KEY, drugs VARCHAR(255), duration VARCHAR(255), Patient VARCHAR(255))"

            q = "select *from information_schema.tables where table_name = 'Client_information'"
            c = con.cursor()
            if c is True:
                print("Table already exists... you may proceed to insert element")
            else:
                cursor.execute(query)
                cursor.execute(query2)
                cursor.execute(query3)
        except Error as e:
            print(e)
        return cursor
    cursor = create_db()
    
    with st.beta_expander("Click to add new TCE"):

        TCE_Profile = st.subheader("Add new TCE Profile")
        Patient_Alias = st.text_input("Patient Alias","123")
        Time_Measure  = st.text_input("Time Unit Measure","Weeks")
        Past_Treatment_date = st.text_input("Past Treatment Date","+/- no of weeks")
        Past_RNA            =     st.text_input("Past RNA log","10000")
        Past_RNAlog_level   = st.text_input("Past RNAlog Level","5")
        BaselineRNA_level   =   st.text_input("BaselineRNA level","1000")
        BaselineRNA_log_level = st.text_input("BaselineRNA Log Level","5")
        Nucleotide_Sequence   = st.text_input("Nucleotide Sequence","CGCGT...")
        
        st.write("-------------------------------------------------------------")

        st.subheader("Treatment Past")
        Drugs = ['AZT','SQV','TDF','LPV']
        # i = Drugs
        for i in range(len(Drugs)):
            pass
        selected_drugs = st.multiselect("Drugs",(Drugs), key = i)
        for b in selected_drugs:
            s = ' '.join(selected_drugs)

        Duration = st.text_input("Duration"," ")
        st.write("---------------------------------------------------------------")

        st.subheader("Treatment Baseline")
        Baseline_Drugs = ['AZT','SQV','TDF','LPV']

        for y in range(len(Baseline_Drugs)):
            pass
        sel_drugs = st.multiselect("Drugs..", (Baseline_Drugs), key = y)
        #convert the selected drugs list to a string 
        for c in sel_drugs:
            # sel_drugs = c
            f = ' '.join(sel_drugs)

        Duration2 = st.text_input("Duration.."," ")
        st.write("---------------------------------------------------------------")

        if st.button("Save"):
            query_insert1 = "INSERT INTO TCE (Patient,Time_Measurement,Past_Treatment_date,Past_RNA ,Past_RNA_log,BaselineRNA_level,BaselineRNA_log,Nucleotide_Sequence) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            VALUES = (Patient_Alias,Time_Measure,Past_Treatment_date,Past_RNA,Past_RNAlog_level,BaselineRNA_level,BaselineRNA_log_level,Nucleotide_Sequence)

            query_insert2 ="INSERT INTO PastTreatment (drugs,duration,Patient) VALUES(%s, %s, %s)"
            VALUES2 = (s,Duration,Patient_Alias)

            query_insert3 = "INSERT INTO BaselineTreatment (drugs,duration,Patient) VALUES (%s,%s,%s)"
            VALUES3= (f,Duration2,Patient_Alias)



            cursor.execute(query_insert1,VALUES)
            cursor.execute(query_insert2,VALUES2)
            cursor.execute(query_insert3,VALUES3)
        
            con.commit()

	
    data = pd.read_csv(filename)
    
    if st.checkbox("Show Dataset"):
        number = st.number_input("Number of Rows to View",1,60)
        st.dataframe(data.head(number))
    

    if st.checkbox("Please choose the features including target variable that go into the model"):
        all_columns = data.columns.tolist()
        selected_columns = st.multiselect("Select", all_columns)
        new_data = data[selected_columns]
        st.dataframe(new_data)
    #set target Column
    target_options = data.columns
    chosen_target = st.sidebar.selectbox("Target column", (target_options))

    X = data.loc[:,data.columns != chosen_target]
    scaler = StandardScaler()
    scaler.fit(X)
    X = (scaler.transform(X))

    y = data[chosen_target].values
    encoder = LabelEncoder()
    encoder.fit(y)
    y= encoder.transform(y)

    X_train,X_test,y_train,y_test = train_test_split(X,y, random_state = 42)
    

    model = load_model('model.h5')


    if st.sidebar.button("Predict"):
        Test_score = model.evaluate(X_test,y_test, verbose=0)
        Train_score = model.evaluate(X_train,y_train, verbose = 0)
        prediction = model.predict_classes(X_test)
        accuracy = accuracy_score(y_test, prediction)

   
        st.success("The accuracy is, {}".format(accuracy*100))
        # st.success("The Test accuracy is,{}".format(Test_score[1]*100))
        # st.success("The Validation accuracy is,{}".format(Train_score[1]*100))
        # st.success("The prediction is {}".format(prediction))
        for i in prediction:break
        st.success("The predicted value is {}".format(i))

        if i == 0:
            st.write("Low Baseline RNA log")
            st.write("A low viral load indicates that the treatment is working and is effective")
        else:
            st.write("High Baseline RNA Log")
            st.write("The Patient has not yet received HIV treatment, or that their treatment is not effective a change in the ARV drug may be important the virus is becoming resistant to therapy or that the treatment is not being followed rigorously.")

 






   

    
    

    
    st.sidebar.text("Built with Streamlit")

if __name__ =="__main__":
    main()    





    







