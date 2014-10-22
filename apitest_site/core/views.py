from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from rest_framework.parsers import FileUploadParser,FormParser
from rest_framework.views import APIView
import hashlib, os, logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create your views here.
class TestView(View):
  def get(self, request):
    return HttpResponse('hello world')

class FileUploadView(APIView):
  tmpdir = os.path.expanduser('~/tmp')
  parser_classes = (FileUploadParser,FormParser)

  def post(self, request):
    file_obj = request.FILES['file']
    params = request.QUERY_PARAMS

    if not self.verify_params(params):
      return HttpResponse(content = 'bad request', status = 400)
    filepath = os.path.join(self.__class__.tmpdir,params['filename'])
    success = True
    if upload_file(file_obj, filepath, placement_name = params['id'], md5 = params['md5']):
      #success
      logger.info('Successfully received file %s' % request.FILES['file'])
    else:
      #failed
      success = False
      logger.info('Fail to receive file %s' % request.FILES['file'])
    #if os.path.exists(filepath):
    #  os.remove(filepath)
    if success:
      return HttpResponse(content = 'OK', status = 200)
    else:
      return HttpResponse(content = 'FAILED', status = 409)

  def verify_params(self, params):
    if 'id' not in params:
      return False
    if 'md5' not in params:
      return False
    if 'filename' not in params:
      return False
    return True

def upload_file(file_obj, filepath, placement_name = None, md5 = None):
  md5_hasher = hashlib.md5()
  with open(filepath, 'wb+') as dest_file:
    for chunk in file_obj.chunks():
      dest_file.write(chunk)
      md5_hasher.update(chunk)
  logger.info('save received file to to %s' % filepath)
  if md5_hasher.hexdigest() != md5:
    return False

  return True
