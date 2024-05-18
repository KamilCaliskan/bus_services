from django.shortcuts import render
from .forms import SearchForm

def index(request):
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            keywords = form.cleaned_data['keywords']
            location = form.cleaned_data['location']
            date = form.cleaned_data['date']
            # Process the search query and fetch results
            # For now, just display the search criteria
            return render(request, 'bus_services/results.html', {
                'form': form,
                'keywords': keywords,
                'location': location,
                'date': date,
            })
    return render(request, 'bus_services/bus_services.html', {'form': form})
