import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache
def load_data():
    data = {
        'id': np.arange(1, 10001),
        'age': np.random.randint(18, 80, 10000),
        'income': np.random.normal(50000, 15000, 10000),
        'city': np.random.choice(['CityA', 'CityB', 'CityC', 'CityD'], 10000),
        'gender': np.random.choice(['Male', 'Female'], 10000)
    }
    df = pd.DataFrame(data)
    return df

df = load_data()

# Title and Description
st.title("Population Data Dashboard")
st.markdown("Explore the population data using various filters and visualizations.")

# Sidebar Filters
st.sidebar.header("Filters")

# Filter by Age
age_filter = st.sidebar.slider("Select Age Range", min_value=int(df['age'].min()), max_value=int(df['age'].max()), value=(18, 80))
filtered_df = df[(df['age'] >= age_filter[0]) & (df['age'] <= age_filter[1])]

# Filter by City
city_filter = st.sidebar.multiselect("Select Cities", options=df['city'].unique(), default=df['city'].unique())
filtered_df = filtered_df[filtered_df['city'].isin(city_filter)]

# Filter by Gender
gender_filter = st.sidebar.multiselect("Select Gender", options=df['gender'].unique(), default=df['gender'].unique())
filtered_df = filtered_df[filtered_df['gender'].isin(gender_filter)]

# Show Filtered Data
st.dataframe(filtered_df)

# Plot Age Distribution
st.subheader("Age Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_df['age'], bins=30, kde=True, ax=ax)
st.pyplot(fig)

# Plot Income Distribution
st.subheader("Income Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_df['income'], bins=30, kde=True, ax=ax)
st.pyplot(fig)

# Plot City Distribution
st.subheader("City Distribution")
fig, ax = plt.subplots()
sns.countplot(x='city', data=filtered_df, ax=ax)
st.pyplot(fig)

# Show Summary Statistics
st.subheader("Summary Statistics")
st.write(filtered_df.describe())
