#  ***Stoink***

_Stoink for Stock Price Prediction is a system that uses deep learning LSTM model to predict the price increase or decrease of one or more stocks for the next three months._

## ***Screenshots***

<img src="screenshot/screenshot1.png" width="70%" height="30%">
<img src="screenshot/screenshot2.png" width="70%" height="30%">
<img src="screenshot/screenshot3.png" width="70%" height="30%">




## ***Functionality***

_The client aims to present the option of using our model to predict what the increase or decrease in percentage is going to be of a certain stock or multiple stocks._


## ***Datasets*** 
***[AlphaVantage API](https://www.alphavantage.co/)*** : _AlphaVantage provides data from fundamental data to technical indicators. The system is not only based the learning algorithm on the listing/opening/closing prices, but to go deeper by using the fundamental data provided by AlphaVantage. 
By using the fundamental data of companies we will be able to read data such as what assets the company has and their investments, their inventory and liabilities and the cash flow of the company and the earnings etc. The free API version is limited to 5 requests per minute and 500 total per day._

## ***Libraries***

_Numpy, Matplotlib, Tensorflow , Keras , Pandas, Scikit-learn_

## ***Technologies***
 - _Python_
 - _Django_
 - _Bootstrap3_
 - _HTML_
 - _CSS_
 - _LSTM_

## ***Setup***

### ***Run app on localhost***
- _1. Install Anaconda(Recommended)_
_Install Anaconda that matches your system via [Anaconda webpage](https://www.anaconda.com/products/individual)_
_Install ML packages either use Anaconda Navigator or conda via terminal: `(base)$ conda install numpy scipy matplotlib scikit-learn pandas `_

- _2. Install Django and SQLite_
_Install pip3 via following command: `(base)$ pip3 install django `_

- _3. Run server_
_Ensure that you are in `client` directory and run the following command: `python manage.py runserver` then open it with Chrome browser: http://127.0.0.1:8000/ Or run `python manage.py runserver 8080`, then open it with Chrome browser: [http://127.0.0.1:8080/](http://127.0.0.1:8080/) if you have ` You're accessing the development server over HTTPS, but it only supports HTTP.` issue with 8000 port._

### ***Or run app Using Docker***

- _1. Build and run_
```Bash
docker build -t <repoName>/<imageName>:<tagName> . # Build image with Tag
docker run -it -p <port:port> <image>:[Tag] # Check if it works
docker tag samgun6/stoink:<Tag> samgun6/stoink:latest # Tag same image with latest
docker push --all-tags samgun6/stoink # Push all tags for selected image to docker hub
```

- _2. Open browser and head to ["http://localhost:8000/"](http://localhost:8000/)_


### ***Or run app with kubernetes and minikube***

***Prerequisites***

- _1. Kubernetes_
- _2. Minikube_
- _3. Docker_

#### ***Steps:***

-  _Start fresh with minikube_

- _1. Build and push latest docker image_
- _2. Start/ reset minikube_

```Bash
 minikube delete # Only needed when starting fresh
 minikube start
```

- _3. Apply deployments_

```Bash
cd kubernetes
kubectl apply -f stoink-job.yaml
kubectl apply -f stoink-service.yaml
kubectl apply -f stoink-deploy.yaml
```

- _4. Update deployment_

- 1. _Build and push latest docker image_
- 2. _Start minikube_
```Bash
minikube start
```
  
- _5. Reapply deployment file_
  
  ```bash
   kubectl get deployments # Shows current deployment
   kubectl get pods # Shows current pods
   # Change version in stoink-deploy.yaml
   kubectl apply -f stoink-deploy.yaml
   ```

   _Or_

   ```Bash
   kubectl set image deployment <deployment name> <container name>=<repo/image>:<new tag>
   kubectl set image deployment stoink-deploy stoink=samgun6/stoink:v1.2.0 # Example
   ```

- _6. Run service_

  ```Bash
  minikube service stoink-service
  ```

- _7. Check deployment_

  ```Bash
  minikube dashboard # In browser

  # or in terminal
  kubectl get pods
  kubectl get deployments
  ```


