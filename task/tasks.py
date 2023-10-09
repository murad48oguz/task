from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from App.models import File
import os


@shared_task
def delete_old_pdfs():

    thirty_days_ago = timezone.now() - timedelta(days=30)
    old_pdfs = File.objects.filter(upload_date=thirty_days_ago)
    for pdf in old_pdfs:
        if os.path.exists(pdf.file.path):
            os.remove(pdf.file.path)
        
        pdf.delete()
