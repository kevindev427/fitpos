from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import StreamingHttpResponse
from main.camera import *
from .models import  Detail, Video
import time
from django.views import View

# Create your views here.
detailid = 0

def app(request, detail_id):
	global detailid
	detailid = detail_id
	video = get_object_or_404(Video, pk=detail_id)
	return render(request, 'main/app.html',{'id':detail_id,'videos':video})




def webcam_feed(request):
	global detailid
	return StreamingHttpResponse(gen(VideoCamera(),detailid),
					content_type='multipart/x-mixed-replace; boundary=frame')


class realtime_feed(View):

	def get(self, request):
		response = StreamingHttpResponse(gene(realtime()))
		response['Content-Type'] = 'text/event-stream'
		return response
