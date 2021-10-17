import streamlit as st
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

activities = ["EDA", "Visuals"]
choice = st.sidebar.selectbox("Select Activities", activities)
if choice == 'EDA':
    st.subheader("Automating Exploratory Data Analysis Process")
    data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])
    if data is not None:
        df = pd.read_csv(data)
        try:
            #  EDA Logic
            if st.checkbox("Preview Dataset"):
                if st.button("Show Top 5 Values"):
                    st.dataframe(df.head())
                if st.button("Show Bottom 5 Values"):
                    st.dataframe(df.tail())
            if st.checkbox("Show Summary"):
                st.write(df.describe())
            if st.checkbox("Show Shape"):
                st.write(df.shape)
            if st.checkbox("Show Size"):
                st.write(df.size)
            if st.checkbox("Show Index"):
                st.write(df.index)
            if st.checkbox("Show Columns"):
                st.write(df.columns)
            if st.checkbox("Show Total Null Values In Dataset"):
                st.write(df.isnull().sum().sum())
            if st.checkbox("Show Null Values In Each Columns"):
                st.write(df.isnull().sum())
            if st.checkbox("Show Percentage of Null Values in each Column"):
                st.write(df.isnull().sum() * 100 / len(df))
            if st.checkbox("Show Duplicate Records"):
                st.dataframe(df[df.duplicated()])
            #  Statistics Logic Starting
            all_columns_name = df.columns
            type_of_Statistics = st.selectbox("Select Type of Statistics",
                                              ["Mean", "Median", "Mode", "Standard Deviation", "Variance"])
            selected_columns_name = st.multiselect("Select Columns For Statistics", all_columns_name)
            if st.button(f"Generate {type_of_Statistics}"):
                st.success(
                    "Generating {} for {}".format(type_of_Statistics, selected_columns_name))
                if type_of_Statistics == "Mean":
                    st.write(df[selected_columns_name].mean())
                if type_of_Statistics == "Median":
                    st.write(df[selected_columns_name].median())
                if type_of_Statistics == "Mode":
                    st.write(df[selected_columns_name].mode())
                if type_of_Statistics == "Standard Deviation":
                    st.write(df[selected_columns_name].std())
                if type_of_Statistics == "Variance":
                    st.write(df[selected_columns_name].var())

        except:
            st.write("Something Went Wrong!!")
#  Plotting Start
elif choice == 'Visuals':
    st.subheader("Data Visualization")
    data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])
    if data is not None:
        df = pd.read_csv(data)
        st.dataframe(df.head())
        if st.checkbox("Show Null Values in Dataset"):
            if st.button("Click Button To see Null Values"):
                st.text("Loading plz wait")
                style.use("ggplot")
                plt.figure(figsize=(12, 9))
                sns.heatmap(df.isnull())
                st.pyplot()
        if st.checkbox("Show Correlation in Dataset"):
            if st.button("Click Button To see Correlation"):
                st.text("Loading plz wait")
                style.use("ggplot")
                plt.figure(figsize=(12, 9))
                sns.heatmap(df.corr(), annot=True)
                st.pyplot()

        st.text("Wants More Plot Then You Can select Below")

        all_columns_names = df.columns.to_list()
        type_of_plot = st.selectbox("Select Type of Plot", ["histplot", "boxplot", "Countplot"])
        selected_columns_names = st.multiselect("Select Column To Plot", all_columns_names)

        if st.button("Generate Plot"):
            st.success("Generating Customizable Plot of {} for {}".format(type_of_plot, selected_columns_names))

            #  Plot By Streamlit
            try:
                if type_of_plot == 'histplot':
                    style.use("ggplot")
                    plt.figure(figsize=(12, 9))
                    sns.distplot(df[selected_columns_names], kde=True)
                    st.pyplot()
                    st.success(f"Now You can see Distribution of data in {selected_columns_names} column")


                elif type_of_plot == "boxplot":
                    style.use("ggplot")
                    plt.figure(figsize=(12, 9))
                    for i in selected_columns_names:
                        sns.boxplot(df[i]).set_title(i)
                        st.pyplot()
                        st.success(f"Now You can see Outliers in {selected_columns_names} Column")


                elif type_of_plot == "Countplot":
                    style.use("ggplot")
                    plt.figure(figsize=(12, 9))
                    for i in selected_columns_names:
                        sns.countplot(df[i]).set_title(i)
                        st.pyplot()
            except:
                st.error("Something wrong with this Attribute ,plz try another")
