from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def analyze(request):
    # Get the Text.
    txt = request.GET.get('text', 'default')

    # Check checkbox Button.
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')


    # Check which Checkbox is on.
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in txt:
            if char not in punctuations:
                analyzed = analyzed + char

        # Analyzed the Text.
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif fullcaps == "on":
        analyzed = ""
        for char in txt:
            analyzed = analyzed + char.upper()

        # Analyzed the Text.
        params = {'purpose': 'Change to UpperCase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremover == "on":
        analyzed = ""
        for char in txt:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char

        # Analyzed the Text.
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(txt):
            if txt[index] == " " and txt[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char

        # Analyzed the Text.
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")





