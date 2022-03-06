# Stoink

Stoink for Stock Price Prediction is a system that uses deep learning LSTM model to predict the price increase or decrease of one or more stocks for the next three months.

# Datasets used 
[AlphaVantage API](https://www.alphavantage.co/)

AlphaVantage provides data from fundamental data to technical indicators. The system is not only based the learning algorithm on the listing/opening/closing prices, but to go deeper by using the fundamental data provided by AlphaVantage. 
By using the fundamental data of companies we will be able to read data such as what assets the company has and their investments, their inventory and liabilities and the cash flow of the company and the earnings etc. 
The free API version is limited to 5 requests per minute and 500 total per day. 

# Libraries used 
 - Numpy 
 - Matplotlib
 - Tensorflow 
 - Keras 
 - Pandas
 - Scikit-learn 

# Technologies used 
 - Python
 - Django
 - Bootstrap3
 - CSS
 - LSTM

# Setup
## Install Anaconda(Recommended)
- Install Anaconda that matches your system via [Anaconda webpage](https://www.anaconda.com/products/individual)
- Install ML packages either use Anaconda Navigator or conda via terminal: 

`(base)$ conda install numpy scipy matplotlib scikit-learn pandas `

## Install Django and SQLite
- Install pip3 via following command:
`(base)$ pip3 install django `

## Run server

Ensure that you are in `client` directory and run the following command: 
`python manage.py runserver` then open it with Chrome browser: http://127.0.0.1:8000/ 

Or run `python manage.py runserver 8080`  

Open it with Chrome browser: [http://127.0.0.1:8080/](http://127.0.0.1:8080/)  

if you have ` You're accessing the development server over HTTPS, but it only supports HTTP.`

issue with 8000 port.  

## Run app Using Docker

- Build and run

    ```Bash
    docker build -t <repoName>/<imageName>:<tagName> . # Build image with Tag
    docker run -it -p <port:port> <image>:[Tag] # Check if it works
    docker tag samgun6/stoink:<Tag> samgun6/stoink:latest # Tag same image with latest
    docker push --all-tags samgun6/stoink # Push all tags for selected image to docker hub
    ```

- Open browser and head to ["http://localhost:8000/"](http://localhost:8000/)

## Run app with kubernetes and minikube

Prerequisites

- Kubernetes
- Minikube
- Docker

### Start fresh with minikube

1. Build and push latest docker image
2. Start/ reset minikube

    ```Bash
    minikube delete # Only needed when starting fresh
    minikube start
    ```

3. Apply deployments

    ```Bash
    cd kubernetes
    kubectl apply -f stoink-job.yaml
    kubectl apply -f stoink-service.yaml
    kubectl apply -f stoink-deploy.yaml
    ```

### Update deployment

1. Build and push latest docker image
2. Start minikube
  
   ```Bash
   minikube start
   ```

3. Re apply deployment file

   ```Bash
   kubectl get deployments # Shows current deployment
   kubectl get pods # Shows current pods
   # Change version in stoink-deploy.yaml
   kubectl apply -f stoink-deploy.yaml
   ```

   OR

   ```Bash
   kubectl set image deployment <deployment name> <container name>=<repo/image>:<new tag>
   kubectl set image deployment stoink-deploy stoink=samgun6/stoink:v1.2.0 # Example
   ```

### Run service

  ```Bash
  minikube service stoink-service
  ```

### Check deployment

  ```Bash
  minikube dashboard # In browser

  # or in terminal
  kubectl get pods
  kubectl get deployments
  ```

# Functionality

The client aims to present the option of using our model to predict what the increase or decrease in percentage is going to be of a certain stock or multiple stocks. This can be done in different ways, either the user inputs values manually and gets the prediction for those values or presses a button which runs all stocks in the system through the model and predicts which ones are predicted to have the most increase (the data which is ran through the model is the latest balance sheet report for each company). This is presented in a list, sorted in descending order. There will also be a list of stocks if the user just wants to make a prediction on a single stock, that is in the system. Admin can extract datasets from the API in the admin page to train the model with new data.  

# Screenshots

![screenshot1](screenshot/screenshot1.png)
![screenshot2](screenshot/screenshot2.png)
![screenshot3](screenshot/screenshot3.png)

# Project management 
[Project management](ProjectManagement.md)

