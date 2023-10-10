from django.forms import ModelForm
from .models import File
from django.core.exceptions import ValidationError


class FileUpload(ModelForm):
  class Meta:
    model = File
    fields = '__all__'

  def clean_file(self):
    file = self.cleaned_data["file"]

    if not file.content_type == "application/pdf":
      
      raise ValidationError("Only PDF files are allowed.")

    return file


