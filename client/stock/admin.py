from __future__ import unicode_literals
from django.conf.urls import url
from django.contrib import admin, messages
from django.contrib.auth.models import Group
from django.forms import forms
from django.shortcuts import render, get_object_or_404
from django.urls import path, reverse
import pandas as pd
from django.db import models
from django.utils.html import format_html
from . import models
from .models import AiModel, DataSet

admin.site.site_header = "Admin page for managing training, loading, evaluating models etc."
admin.site.unregister(Group)


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class DataSetAdmin(admin.ModelAdmin):
    list_display = ("title", "created",)

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("upload-dataset/", self.upload_dataset)]
        return new_urls + urls

    def upload_dataset(self, request):
        if request.method == "POST":
            # requesting the data
            model_file = request.FILES["csv_upload"]
            # decoding to String
            file_data = model_file.read().decode("utf-8")
            # declaring model with attributes and saving it
            tempModel = models.DataSet()
            tempModel.title = model_file

            #Splitting the filedata to get column names
            column = file_data.split("\r\n", 1)
            column = str(column[0])
            column = column.split(",", 8)

            # converting the string into a dataframe to be able to save as json object (attribute of DataSet model)
            data = file_data
            df = pd.DataFrame(data=[x.split(',') for x in data.split('\r\n')])
            #deleting first row, for some realson after above function, it adds the column names as first data row....
            print(df.tail(1))
            print(df.head(1))
            df = df.iloc[1:-1, :]
            print(df.head(1))
            print(df.tail(1))
            # Assiging the right column names
            df.columns = column

            tempModel.putframe(df)
            tempModel.save()
        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/dataset_upload.html", data)


class AiModelAdmin(admin.ModelAdmin):
    list_display = ("title", "account_actions","train_dataset","evaluation_dataset","version", "deployed", "dataset", "created", "loss", "accuracy", "learningrate", "inputlayer", "dropout", "secondlayer", "thirdlayer", "epochs", "batchsize", "split")

    def account_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Train</a>&nbsp;'
            '<a class="button" href="{}">Evaluate</a>',
            reverse('admin:model-train', args=[obj.pk]),
            reverse('admin:model-evaluate', args=[obj.pk]),
        )

    account_actions.short_description = 'Account Actions'
    account_actions.allow_tags = True

    def get_urls(self):
        print("IM IN THE RIGHT FUNCTION")
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^(?P<title>.+)/train/$',
                self.admin_site.admin_view(self.train_model),
                name='model-train',
            ),
            url(
                r'^(?P<title>.+)/evaluate/$',
                self.admin_site.admin_view(self.evaluate_model),
                name='model-evaluate',
            ),
        ]
        return custom_urls + urls

    def train_model(self, request, title):
        target = get_object_or_404(AiModel, pk=title)
        print(target.train_model())
        return render(request, "admin/base.html")

    def evaluate_model(self, request, title):
        target = get_object_or_404(AiModel, pk=title)
        loss, acc = target.evaluate_model()
        message_string = "Evaluation complete, loss : " + str(loss) + " acc : " + str(acc)
        messages.success(request, message_string)
        return render(request, "admin/base.html")


admin.site.register(AiModel, AiModelAdmin)
admin.site.register(DataSet, DataSetAdmin)
