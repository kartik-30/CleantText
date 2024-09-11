from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext=request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineRemover=request.POST.get('newlineRemover', 'off')
    extraSpaceRemover=request.POST.get('extraSpaceRemover', 'off')
    countchar=request.POST.get('countchar', 'off')

    if removepunc == "on":
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose': 'Remove Punctuatuion', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose': 'Upper Case', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if newlineRemover=='on': 
        analyzed=""
        for char in djtext:
            if char!='\n':
                analyzed=analyzed+char
        params={'purpose': 'Remove new lines', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if extraSpaceRemover=='on':
        analyzed=""
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params={'purpose': 'Remove extra space', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if countchar=='on':
        count=0
        for char in djtext:
            if char.isalpha():
                count=count+1
        params={'purpose': 'Character count', 'analyzed_text': count}
        # return render(request, 'analyze.html', params)
    if(removepunc != "on" and fullcaps!='on' and newlineRemover!='on' and extraSpaceRemover!='on' and countchar!='on'): 
        return HttpResponse('please select the given operation')
    return render(request,'analyze.html',params)

