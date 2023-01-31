import streamlit as st
from PIL import Image
import requests
import pandas as pd
import os
import json
#
image_path = "img.jpg"
image = Image.open(image_path)

st.set_page_config(page_title="Predict Next possible word App", layout="centered")
st.image(image, caption='Next Word')
#
# page header
st.title(f"Predict Next word App")
with st.form("Generate"):
   text1 = st.text_input("Enter text here")
   submit = st.form_submit_button("Next Word")
   #
   if submit:    
        print(text1)
        #
        with open("input.txt", "wb") as f:
            f.write(text1.encode("utf-8"))
        os.chmod("input.txt", 0o777)
        # Paraphrase Generation API
        url = "https://app.aimarketplace.co/api/marketplace/models/next-word-predictor-fd37a923/predict/"
        payload={'data': open('input.txt','rb')}
        headers = {'Authorization': 'Api-Key Uwxo9FdW.imQ0rBuQliuvnC7DTkvKmwXoIxeC9EQA','Cache-Control': 'no-cache'}

        response = requests.request("POST", url, headers=headers, files=payload)

        print(response.text)
        # output header
        st.header("Possible Next Word")
        # output results
        st.success(response.text.split("response")[1].replace(":","").split("}")[0].replace('"','').replace('\\',''))