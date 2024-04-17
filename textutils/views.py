from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	return render(request, 'index.html')


def analyze(request):
	# get the text
	djtext = request.POST.get('text', 'default')

	# checkbox values
	removepunc = request.POST.get('removepunc', 'off')
	fullcaps = request.POST.get('fullcaps', 'off')
	newlineremover = request.POST.get('newlineremover', 'off')

	# check which checkbox is on
	if removepunc == "on":
		# analyzed= djtext
		punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
		analyzed = ""
		for char in djtext:
			if char not in punctuation:
				analyzed = analyzed + char

		params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}

		# analyze the text
		djtext = analyzed
	# return render(request, 'analyze.html', params)

	if (fullcaps == "on"):
		analyzed = ""
		for char in djtext:
			analyzed = analyzed + char.upper()
		params = {'purpose': 'Captalized text', 'analyzed_text': analyzed}

		# analyze the text
		djtext = analyzed
	# return render(request, 'analyze.html', params)

	if (newlineremover == "on"):
		analyzed = ""
		for char in djtext:
			if char != "\n" and char != "\r":
				analyzed = analyzed + char
		params = {'purpose': 'Remove New lines', 'analyzed_text': analyzed}
		# analyze the text
		djtext = analyzed
	# return render(request, 'analyze.html', params)
	if (removepunc != "on" and newlineremover != "on" and fullcaps != "on"):
		return HttpResponse("please select any operation and try again")

	return render(request, 'analyze.html', params)
