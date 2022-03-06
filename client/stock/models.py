from __future__ import unicode_literals
import pandas as pd
from django.contrib.postgres.fields import JSONField
from django.db import models, transaction
from tensorflow.keras.models import load_model
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import tensorflow as tf


class DataSet(models.Model):
    title = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    data = JSONField(default='This is empty')

    def putframe(self, dataframe):
        self.data = dataframe.to_json(orient='split')

    def loadframe(self):
        return pd.read_json(self.data, orient='split')

    def __str__(self):
        return self.title

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title


class AiModel(models.Model):
    # Title is also the name of the file that holds the model, which we load from the repo as a .h5 file
    title = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    loss = models.FloatField(default=0.0)
    accuracy = models.FloatField(default=0.0)
    learningrate = models.FloatField(default=0.005)
    dropout = models.FloatField(default=0.2)
    inputlayer = models.IntegerField(default=10)
    secondlayer = models.IntegerField(default=100)
    thirdlayer = models.IntegerField(default=51)
    epochs = models.IntegerField(default=100)
    batchsize = models.IntegerField(default=16)
    split = models.FloatField(default=0.3727)
    version = models.IntegerField(default=0)
    deployed = models.BooleanField(default=False)
    dataset = models.ForeignKey(DataSet, related_name='dataset', null=True, on_delete=models.SET_NULL)
    evaluation_dataset = models.ForeignKey(DataSet,related_name='evaluation_dataset', null=True, on_delete=models.SET_NULL)
    train_dataset = models.CharField(max_length=30, default= "Untrained")


    def save(self, *args, **kwargs):
        if not self.deployed:
            return super(AiModel, self).save(*args, **kwargs)
        with transaction.atomic():
            AiModel.objects.filter(
                deployed=True).update(deployed=False)
            return super(AiModel, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

    def get_title(self):
        temp = self.title
        return temp

    def get_titleversion(self):
        temp = str(self.title + "_v" + str(self.version))
        return temp

    def set_title(self, title):
        self.title = title

    def set_version(self, new):
        self.version = new

    def set_train_dataset(self, new):
        self.train_dataset = new

    def train_model(self):

        df = self.dataset.loadframe()
        print(df)
        # Randomly shuffles the rows, better for training the model later
        # Also resetting the Index for the dataframe
        df = df.sample(frac=1).reset_index(drop=True)

        # Initiating a Sequential model with keras
        model = tf.keras.models.Sequential()

        # Adding layers to the model
        model.add(tf.keras.layers.Dense(units=self.inputlayer, input_dim=5))
        model.add(tf.keras.layers.Dropout(self.dropout))
        model.add(tf.keras.layers.Dense(self.secondlayer, activation='relu'))
        model.add(tf.keras.layers.Dense(self.thirdlayer, activation='relu'))
        model.add(tf.keras.layers.Dense(units=1, activation='linear'))

        # Compiling the model
        opt = tf.keras.optimizers.Adam(lr=self.learningrate)
        model.compile(loss='mean_squared_error', optimizer=opt, metrics=['accuracy'])

        # Declaring the label and features np.array
        column_features = []
        for col in df.columns:
            if col != "1m":
                if col != "symbol":
                    if col != "timestamp":
                        column_features.append(col)

        # Slicing the dataset to features and labels
        y = df["1m"].to_numpy()
        X = df[column_features].to_numpy()

        # Normalizing
        X = preprocessing.normalize(X)

        # Splitting the dataset
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.split)

        # Fitting the model
        model.fit(X_train, y_train, epochs=self.epochs, batch_size=self.batchsize)

        # Updating the version of the model
        temp = self.version + 1
        self.version = temp

        # Evaluation
        train_loss, train_acc = model.evaluate(X_train, y_train)
        self.loss = train_loss
        self.accuracy = train_acc

        # save model
        model.save(str(self.get_titleversion()) + ".h5")
        self.train_dataset = self.dataset.get_title()

        # return statement and saving the update varaible to .self
        self.save()
        return str("Trained model successfully with " + self.dataset.get_title() + " dataset , named : " + self.get_titleversion())

    def evaluate_model(self):
        # Loading model
        model = load_model(self.get_titleversion() + ".h5")

        # Loading dataset, evaluation_dataset
        df = self.evaluation_dataset.loadframe()
        print(df)

        # Declaring the label and features np.array
        column_features = []
        for col in df.columns:
            if col != "1m":
                if col != "symbol":
                    if col != "timestamp":
                        column_features.append(col)

        # Splitting dataset and normalizing
        X = df[column_features].to_numpy()
        y = df["1m"].to_numpy()

        # Normalizing
        X = preprocessing.normalize(X)

        # Model evaluation
        test_loss, test_acc = model.evaluate(X, y)

        return test_loss, test_acc


class Prediction:
    price: float

    def __init__(self, price):
        self.price = price


