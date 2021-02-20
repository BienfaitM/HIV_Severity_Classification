import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns

def main():
	"""Response Data Explorer """
	st.title("HIV Viral Load Viral Load Classifier")
	st.subheader("Viral Load")

	
	#select file
	def file_selector(folder_path ='/Users/mt/Downloads/Archive'):
		filenames = os.listdir(folder_path)
		seleted_filename = st.selectbox("Select A file", filenames)
		return os.path.join(folder_path, seleted_filename)
	filenames = file_selector( )
	st.info("You Picked {}".format(filenames))

	df = pd.read_csv(filenames)
	
	#show dataset
	if st.checkbox("Dataset"):
		#we can add upper and lower limit
		#n = st.number_imput("",4,20)
		number = st.number_input("Number of Rows to View",5)
		st.dataframe(df.head(number))
	#Dataset Review
	if st.checkbox("Preview Dataset"):
		if st.button("Head"):
			st.write(df.head())
		elif st.button("Tail"):
			st.write(df.tail())
		else:
			number = st.slider("Select Number of Rows",
				1, df.shape[0])
			st.write(df.head(number))
	#show columns
	if st.checkbox("columns names"):
		st.write(df.columns)
	#show shape
	if st.checkbox("Dataset Shape"):
		st.write(df.shape)
		data_dimension = st.radio("Show Dimesion By",("Rows", "Columns"))
		if data_dimension == 'Columns':
			st.text("Number of Columns")
			st.write(df.shape[0])
		else:
			st.text("Number of Rows")
			st.write(df.shape[1])
	#show dypes
	if st.checkbox("Dataset Dtypes"):
		st.write(df.dtypes)

	#show missing_values
	# if st.checkbox("Dataset missing_values"):
	# 	missing_values = list(df.columns[df.isna().any()])
	# 	columns = df.shape[1]
	# 	for col in missing_values:
	# 		missing_percentage = ((df[col].isna().sum())/columns)*100
	# 	st.text("missing percentage")
		# st.write(missing_percentage)
	#show missing_values
	if st.checkbox("Dataset missing values"):
		st.write(df.isna().sum())
	#select Columns
	if st.checkbox("Select Columns"):
		all_columns = df.columns.tolist()
		seleted_columns = st.multiselect("Select", all_columns)
		new_df = df[seleted_columns]
		st.dataframe(new_df)
	#Show Values
	if st.button("Value Counts"):
		st.text("Value Counts By Target/Class")
		st.write(df.iloc[:,-1].value_counts())
	#show Summary
	if st.checkbox("Summary"):
		st.write(df.describe().T)

	#Plotting
	st.subheader("Data Visualization")
	all_columns_names = df.columns.tolist()
	type_of_plot = st.selectbox("Select Type",["bar","area","line","hist",
		"box","pde"])
	seleted_columns_names = st.multiselect("Select Columns To Plot", all_columns_names)
	if st.button("Generate Plot"):
		st.success("Generatin Customixable Plot of {} for {}".format(type_of_plot,seleted_columns_names))

	if st.checkbox("CorrelationPlot"):
		st.write(sns.heatmap(df.corr(), annot = True))
		st.pyplot()

	# Plot By Streamlit
	if type_of_plot == 'area':
		cust_data = df[seleted_columns_names]
		st.area_chart(cust_data)
	elif type_of_plot == 'bar':
		 cust_data = df[seleted_columns_names]
		 st.bar_chart(cust_data)
	elif type_of_plot== 'line':
		cust_data = df[seleted_columns_names]
		st.line_chart(cust_data)
	elif type_of_plot :
		cust_plot = df[seleted_columns_names].plot(kind=type_of_plot)
		st.write(cust_plot)
		st.pyplot()


	#Machine Learning Algorithms 
	from sklearn.model_selection import train_test_split

	features = st.multiselect("Select Feature Columns", df.columns)
	labels   = st.multiselect("Select Target Column", df.columns)

	features = df[features].values
	labels = df[labels].values

	train_percentage = st.slider("Select % to train model",1,100)
	train_percentage = train_percentage/100

	X_train,X_test, y_train, y_text = train_test_split(features, labels, train_size = train_percentage, random_state =1)





	






if __name__ == '__main__':
	main()

