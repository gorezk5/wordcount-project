from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    text_written = request.GET['thething']

    words_list = text_written.split()

    worddictionary = {}

    for word in words_list:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'thething':text_written, 'count':len(words_list), 'worddictionary':sortedwords})

def about(request):
    return render(request, 'about.html')
