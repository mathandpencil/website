from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives 
from django.template.loader import render_to_string


def lets_crypt_verification(request):
    return render(request, 'core/https.html', {})
    
def index(request):
    return render(request, 'core/index.html', {})
    
def about(request):
    return render(request, 'core/about.html', {})
    
def branding_1(request):
    return render(request, 'core/branding_1.html', {})
    
def branding_2(request):
    return render(request, 'core/branding_2.html', {})
    
def branding_3(request):
    return render(request, 'core/branding_3.html', {})
    
def capabilities(request):
    return render(request, 'core/capabilities.html', {})
    
def clients(request):
    return render(request, 'core/clients.html', {})
    
def contact(request):
    
    if request.method == "POST":
                
        html = "<p> %s </p>" % request.REQUEST.get("name")
        html += "<p> %s </p>" % request.REQUEST.get("email")
        html += "<p> %s </p>" % request.REQUEST.get("comment")
        message = EmailMultiAlternatives("Math & Pencil Request Form", 
                                         html, 
                                         "noreply@mathandpencil.co,",
                                         to=settings.TO_EMAIL_LIST,
                                         bcc=[])
        message.attach_alternative(html , 'text/html')      
        message.send()
        
        print('sent ...')
    
    return render(request, 'core/contact.html', {})
    
def projects(request):
    return render(request, 'core/projects.html', {})
    
def projects_1(request):
    return render(request, 'core/projects_1.html', {})
    
def projects_2(request):
    return render(request, 'core/projects_2.html', {})
    
def projects_3(request):
    return render(request, 'core/projects_3.html', {})
    
def projects_4(request):
    return render(request, 'core/projects_4.html', {})
    
def team(request):
    return render(request, 'core/team.html', {})
    
def test(request):
    return render(request, 'core/test.html', {})
    
def websites_1(request):
    return render(request, 'core/websites_1.html', {})
    
def websites_2(request):
    return render(request, 'core/websites_2.html', {})
    
def websites_3(request):
    return render(request, 'core/websites_3.html', {})