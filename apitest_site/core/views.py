from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView


# Create your views here.
class TestView(View):
  def get(self, request):
    return HttpResponse('hello world')

class FileUploadView(APIView):
  parser_classes = (FileUploadParser,)

  def post(self, request):
    file_obj = request.FILES['file']
    upload_file(file_obj)
    return HttpResponse(content = 'OK', status = 200)

def upload_file(file_obj):
  with open('/tmp/tmpfile', 'wb+') as dest_file:
    for chunk in file_obj.chunks():
      dest_file.write(chunk)
