import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px

data = pd.read_csv("../final_results.csv")


#df = data.groupby(level="Buisness Code").mean()
#df = df.sort_values(by=["Prediciton_average"], ascending=False)

image = Image.open("../assets/logo-castorama.jpeg")
st.set_page_config(layout="wide")
st.sidebar.image(image,output_format="auto")
selected_menu = st.sidebar.radio ("", ["Home","Predictions","Coming soon"])

if selected_menu == "Predictions":
    st.title("Prédiction")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None :
        col1, col2, col3 = st.columns(3)
        for i in range(0,3) :
            col1.metric("Buisness Code", data["Business Code"][i])
            col2.metric("Prediction score", data["Prediciton_average"][i])
            col3.metric("Rating ", data["Rating"][i])

        code = st.text_input("Choose your business code", key = "business_code")
        st.dataframe(data[["Content","Prediciton_average"]][data["Business Code"] == code ])
        fig = px.line(data[data["Business Code"] == code], x='Creation date', y=["Prediciton_average"])
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)



