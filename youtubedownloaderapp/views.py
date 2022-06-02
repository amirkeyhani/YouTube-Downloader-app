# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# import youtube_dl
# from django.contrib import messages
# # Create your views here.


# def home(request):
#     return render(request, 'home.html')


# def download_video(request):
#     if request.method == 'POST':
#         video_url = request.POST['url']
#         if video_url:
#             ydl_opts = {'outtmp1': 'D:/'}
#             with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#                 ydl.download([video_url])
#             messages.success(request, 'Video Downloaded.')
#             return redirect('home')
#         else:
#             messages.warning(request, 'Please Enter Video URL')
#             return redirect('home')
#     return redirect('home')

from django.shortcuts import render
from django.contrib import messages
from pytube import *
# Create your views here.


def index(request):
    if request.method == 'POST':
        url = request.POST['url']
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download()
        messages.info(request, 'Video Downloaded..')
        return render(request, 'home.html')
    return render(request, 'home.html')


# from django.views.generic import View
# from pytube import YouTube
# from django.shortcuts import render, redirect

# class home(View):
#     def __init__(self, url=None):
#         self.url = url
        
#     def get(self, request):
#             return render(request, 'home.html')
        
#     def post(self, request):
#         if request.POST.get('fetch-vid'):
#             self.url = request.POST.get('given_url')
#             video = YouTube(self.url)
#             vidTitle, vidThumbnail = video.title, video.thumbnail_url
#             qual, stream = [], []
#             for vid in video.streams.filter(progressive=True):
#                 qual.append(vid.resolution)
#                 stream.append(vid)
#             context = {'vidTitle': vidTitle, 'vidThumbnail': vidThumbnail, 
#                        'qual': qual, 'stream': stream, 
#                        'url': self.url}
#             return render(request, 'home.html', context)
        
#         elif request.POST.get('download-vid'):
#             self.url = request.POST.get('given_url')
#             video = YouTube(self.url)
#             stream = [x for x in video.streams.filter(progressive=True)]
#             video_qual = video.streams[int(request.POST.get('download-vid')) - 1]
#             video_qual.download(output_path='../../Downloads')
#             return redirect('home')
        
#         return render(request, 'home.html')

