#render is key component in generating dynamic web pages in Django 
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meetup,Participant
from .forms import RegistrationForm


def home(request):
    meetup = Meetup.objects.all()
    
    # meetups = [{
    #     'title': 'A First Meetup',
    #     'location':'Islamabad',
    #     'slug':'a-first-meetup'
    # },
    # {
    #     'title': 'A Second Meetup',
    #     'location':'Lahore',
    #     'slug':'a-Second-meetup'
    # }]
    
    context = {
        'meetups': meetup
    }

    return render(request, 'meetups/index.html',context)

def meetup_details(request,meetup_slug):
    try:
      selected_meetup = Meetup.objects.get(slug=meetup_slug)
      if request.method == 'GET':
         registration_form = RegistrationForm()
      else:
         registration_form = RegistrationForm(request.POST)
         if registration_form.is_valid():
            user_email = registration_form.cleaned_data['email']
            participant, _ = Participant.objects.get_or_create(email=user_email)
            selected_meetup.participant.add(participant)

            # participant = Participant.objects.create(email=email)
            # participant = registration_form.save()
            return redirect('confirmation-registration',meetup_slug=meetup_slug)
            
    
      selected_meetup = {
          'meetup_found':True,
          'meetup':selected_meetup,
          'form':registration_form
         }
      return render(request, 'meetups/meetup_details.html', selected_meetup)
    
    except Exception as exc:
      print(exc)
      selected_meetup = {
          'meetup_found':False,
        #   'selected_meetup':meetup_item,
      }
      return render(request, 'meetups/meetup_details.html', selected_meetup)
       

def confirmation_registration(request,meetup_slug):
   meetup = Meetup.objects.get(slug=meetup_slug)
   meetup = {
      'organizer_email':meetup.organizer_email
   }
   return render(request, 'meetups/registration-sucess.html',meetup)