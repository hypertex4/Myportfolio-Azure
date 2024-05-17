from django.shortcuts import redirect, render
from .models import Contact
from . import forms
from django.contrib import messages


# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = forms.CreateContact(request.POST)
        if form.is_valid():
            newcontact = form.save(commit=False)
            newcontact.save()
            messages.add_message(request, messages.SUCCESS, "Contact message sent to Ayokunle Sucessfully, you will hear from me shortly.")
            return redirect('contacts:new-message')
    else :
        form = forms.CreateContact()
        form.as_table()
        return render(request, 'contacts/create-new.html', {'form':form})