from django import forms
import cv2
import hoge
from django.core.files.storage import default_storage

class MultipleUploadForm(forms.Form):
    file = forms.FileField(
            label = "Video File",
            widget=forms.ClearableFileInput(attrs={'multiple': True})
            )
    export_dir = forms.CharField(label="export_dir")

    def save(self):
        file_paths = []
        for upload_file in self.files.getlist("file"):
            name = upload_file.name.replace(" ", "")
            file_name = default_storage.save(name, upload_file)
            file_path = default_storage.url(file_name)
            file_path = "." + file_path
            file_paths.append(file_path)
        export_dir = self.cleaned_data["export_dir"]
        hoge.video2mp3(file_paths, export_dir)
        #hoge.recreate_dir("./media")
