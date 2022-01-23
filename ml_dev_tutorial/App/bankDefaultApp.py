import streamlit as st
import pandas as pd
import json
import requests
import numpy as np

##########

# Present title
st.title('Company Default Estimator')

##########

st.header('1. Load csv report')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     df = pd.read_csv(uploaded_file)
     st.table(df)

##########
st.header('2. Run analysis')

if st.button('Press to run data through model'):
    #Create JSON Object
    data = df.to_numpy()
    data = json.dumps({"signature_name": "serving_default", "instances": data.tolist()})

    # Call tf server
    headers = {"content-type": "application/json"}
    json_response = requests.post('http://localhost:8502/v1/models/bankmodel:predict', data=data, headers=headers)
    predictions = json.loads(json_response.text)['predictions']

    # show results
    pred_round = [round(pred,3) for pred in sum(predictions, [])]
    st.write("0 ~ prediction no default and 1 ~ prediction will deault ")
    st.write(pred_round)
