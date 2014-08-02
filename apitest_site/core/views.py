from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
import hashlib, os


# Create your views here.
class TestView(View):
  def get(self, request):
    return HttpResponse('hello world')

class FileUploadView(APIView):
  parser_classes = (FileUploadParser,)

  def post(self, request):
    file_obj = request.FILES['file']
    if not verify_params(self, request):
      return HttpResponse(content = 'bad request', status = 400)
    upload_file(file_obj, filename = request.POST['filename'], placement_name = request.POST['id'], md5 = request.POST['md5'])
    return HttpResponse(content = 'OK', status = 200)

  def verify_params(self, request):
    if 'id' not in request.POST:
      return False
    if 'md5' not in request.POST:
      return False
    if 'filename' not in request.POST:
      return False
    return True

def upload_file(file_obj, filename = None, placement_name = None, md5 = None):
  md5_hasher = hashlib.md5()
  with open(os.path.join('/tmp/',filename), 'wb+') as dest_file:
    for chunk in file_obj.chunks():
      dest_file.write(chunk)
      md5_hasher.update(chunk)
  if md5_hasher.hexdigest != md5:
    return False

  return True
