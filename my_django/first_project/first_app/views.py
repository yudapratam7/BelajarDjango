from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
from . import  forms

# Create your views here.
def index(request):
    # Query access records and users
    webpages_list = AccessRecord.objects.order_by('date')
    persons_list = Person.objects.all()

    # Context for template
    context = {
        'access_records': webpages_list,
        'persons': persons_list 
    }
    
    # Render template with context
    return render(request, 'first_app/index.html', context=context)

def form_name_view(request):
    form = forms.FormName()  # Initialize form

    if request.method == "POST":
        form = forms.FormName(request.POST)  # Populate form with POST data

        if form.is_valid():
            # Display form data on the console
            print("VALIDATION SUCCESS!")
            print("NAME: " + form.cleaned_data["name"])
            print("EMAIL: " + form.cleaned_data["email"])
            print("TEXT: " + form.cleaned_data["text"])

    # Render form template
    return render(request, "first_app/form_page.html", {"form": form})