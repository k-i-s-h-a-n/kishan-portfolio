from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from kishan.models import contact

# Create your views here.


def profile(request):
    return render(request,"website/index.html")





def send_msg(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        instances=contact(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        instances.save()

        print(f"\nname = {name},email = {email},subject= {subject},message=  {message}")
         # Validate the form data here (you may want to add more validation logic)
        if name and email and subject and message:
            # If the form is valid, set success message
            messages.success(request, 'Your message has been submitted successfully!')
            return redirect("send_msg")
    return render(request,"website/contact.html")