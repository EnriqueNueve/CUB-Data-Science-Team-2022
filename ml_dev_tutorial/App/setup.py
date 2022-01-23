# True results
Bankrupt?
1,0,0,0,0,0,1,0

# Run streamlit app
streamlit run bankDefault.app

# tf server
docker run -p 8502:8501 --mount type=bind,source=/Users/rick/Desktop/Boulder/Spring2022/data_science/workspace/CUB-Data-Science-Team-2022/ml_dev_tutorial/App/tf_model,target=/models/bankmodel/ -e MODEL_NAME=bankmodel -t tensorflow/serving 
