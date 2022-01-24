# True results
Bankrupt?
1,0,0,0,0,0,1,0

# Run streamlit app
streamlit run bankDefaultApp.py --server.port 8080

##################################

# Make docker network for containers to talk
docker network create bank_app

# Build docker image for streamlit interface
docker build -t streamlit_app_interface:latest .

# Run image for streamlit interface
docker run --network bank_app -p 8080:8080 streamlit_app_interface:latest

# tf server
docker run --network bank_app -p 8501:8501 --mount type=bind,source=/Users/rick/Desktop/Boulder/Spring2022/data_science/workspace/CUB-Data-Science-Team-2022/ml_dev_tutorial/App/tf_model,target=/models/bankmodel/ -e MODEL_NAME=bankmodel -t tensorflow/serving

# Check network
docker network inspect bank_app

docker rm $(docker ps -a -q)

docker builder prune --all
