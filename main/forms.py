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
        names = []
        for i, upload_file in enumerate(self.files.getlist("file")):
            name = upload_file.name.replace(" ", "")
            name = name.replace(".", "")
            origin_name = name.replace("mp4", "")

            name = "%d.mp4"%(i)
            file_name = default_storage.save(name, upload_file)
            file_path = default_storage.url(file_name)
            file_path = "." + file_path
            #file_path = file_path.split("/")[1:]
            #tmp = ""
            #for i, path in enumerate(file_path):
            #    tmp += path
            #    if i != len(file_path)-1:
            #        tmp += "/"
            #file_path = tmp
            file_paths.append(file_path)
            names.append(origin_name)
        export_dir = self.cleaned_data["export_dir"]
        hoge.video2mp3(names, file_paths, export_dir)
        hoge.recreate_dir(["./media"])
