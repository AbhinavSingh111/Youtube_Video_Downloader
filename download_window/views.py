from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from moviepy.editor import VideoFileClip
import youtube_dl
import os
import zipfile

def index(request):
    # return HttpResponse("This is HOME page")
    context = {
        "variable1" : "This is the variable sent via context from views",
        "variable2" : "This is the second variable coming from template which has been rendered via view"
    }
    return render(request, 'index.html', context)

def services(request):
    # return HttpResponse("This is SERVICES page")
    if request.method == 'POST':
        url = request.POST.get('url')

        try:
            # Set the options for youtube_dl
            ydl_opts = {
                'outtmpl': os.path.join(os.path.expanduser('~'), 'Downloads', '%(title)s.%(ext)s'),  # Output file path and name
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                # Download the video
                info_dict = ydl.extract_info(url, download=True)

            # Get the video filename
            video_filename = ydl.prepare_filename(info_dict)

            # Set the download success message
            download_message = f"Video '{info_dict['title']}' has been downloaded successfully."

            return render(request, 'result.html', {'download_message': download_message})
        except Exception as e:
            error_message = str(e)
            return render(request, 'result.html', {'error_message': error_message})



    return render(request, 'index.html')
