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


# st.set_option("deprecation.showfileUploaderEncoding", False)

# st.title("HIV Severity Classify")
# st.write("Explore our ANN Classification model ")

# st.sidebar.header("About App")
# st.sidebar.info("This System predicts the likelihood that the infection of an HIV patient will become less severe")


# def main():
#     def connection():
#         con = mysql.connector.connect(
#             host       = 'localhost',
#             database   = 'TCEprofile',
#             user       = 'root',
#             password   = '2wlApluS'
#             )
#         print("Connect successfully")
#         return con
#     con = connection()

#     def create_db():
#         cursor = con.cursor()
#         try:
#             query = "create table TCE (Patient VARCHAR(255),Time_Measurement VARCHAR(255), Past_Treatment_date VARCHAR(254), Past_RNA VARCHAR(254), Past_RNA_log VARCHAR(254), BaselineRNA_level VARCHAR(254), BaselineRNA_log VARCHAR(254), Nucleotide_Sequence VARCHAR(255))"
#             query2 = "create table PastTreatment(id INT AUTO_INCREMENT PRIMARY KEY, drugs VARCHAR(255), duration VARCHAR(255), Patient VARCHAR(255))"
#             query3 = "create table BaselineTreatment(id INT AUTO_INCREMENT PRIMARY KEY, drugs VARCHAR(255), duration VARCHAR(255), Patient VARCHAR(255))"

#             q = "select *from information_schema.tables where table_name = 'Client_information'"
#             c = con.cursor()
#             if c is True:
#                 print("Table already exists... you may proceed to insert element")
#             else:
#                 cursor.execute(query)
#                 cursor.execute(query2)
#                 cursor.execute(query3)
#         except Error as e:
#             print(e)
#         return cursor
#     cursor = create_db()

    
#     TCE_Profile = st.subheader("Add new TCE Profile")
#     Patient_Alias = st.text_input("Patient Alias","123")
#     Time_Measure  = st.text_input("Time Unit Measure","Weeks")
#     Past_Treatment_date = st.text_input("Past Treatment Date","+/- no of weeks")
#     Past_RNA            =     st.text_input("Past RNA log","10000")
#     Past_RNAlog_level   = st.text_input("Past RNAlog Level","5")
#     BaselineRNA_level   =   st.text_input("BaselineRNA level","1000")
#     BaselineRNA_log_level = st.text_input("BaselineRNA Log Level","5")
#     Nucleotide_Sequence   = st.text_input("Nucleotide Sequence","CGCGT...")
    
#     st.write("-------------------------------------------------------------")

#     st.subheader("Treatment Past")
#     Drugs = ['AZT','SQV','TDF','LPV']
#     # i = Drugs
#     for i in range(len(Drugs)):
#         pass
#     selected_drugs = st.multiselect("Drugs",(Drugs), key = i)
#     for b in selected_drugs:
#         s = ' '.join(selected_drugs)

#     Duration = st.text_input("Duration"," ")
#     st.write("---------------------------------------------------------------")

#     st.subheader("Treatment Baseline")
#     Baseline_Drugs = ['AZT','SQV','TDF','LPV']

#     for y in range(len(Baseline_Drugs)):
#         pass
#     sel_drugs = st.multiselect("Drugs..", (Baseline_Drugs), key = y)
#     #convert the selected drugs list to a string 
#     for c in sel_drugs:
#         # sel_drugs = c
#         f = ' '.join(sel_drugs)

#     Duration2 = st.text_input("Duration.."," ")
#     st.write("---------------------------------------------------------------")

#     if st.button("Save"):
#         query_insert1 = "INSERT INTO TCE (Patient,Time_Measurement,Past_Treatment_date,Past_RNA ,Past_RNA_log,BaselineRNA_level,BaselineRNA_log,Nucleotide_Sequence) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
#         VALUES = (Patient_Alias,Time_Measure,Past_Treatment_date,Past_RNA,Past_RNAlog_level,BaselineRNA_level,BaselineRNA_log_level,Nucleotide_Sequence)

#         query_insert2 ="INSERT INTO PastTreatment (drugs,duration,Patient) VALUES(%s, %s, %s)"
#         VALUES2 = (s,Duration,Patient_Alias)

#         query_insert3 = "INSERT INTO BaselineTreatment (drugs,duration,Patient) VALUES (%s,%s,%s)"
#         VALUES3= (f,Duration2,Patient_Alias)



#         cursor.execute(query_insert1,VALUES)
#         cursor.execute(query_insert2,VALUES2)
#         cursor.execute(query_insert3,VALUES3)
       
#         con.commit()

# if __name__ =="__main__":
#     main() 