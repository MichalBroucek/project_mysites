from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone

from messages.models import Message

# Create your views here.

def messages(request):
    """List of messages which were stored by visitors."""
    messages = Message.objects.all().order_by("-date")
    count_messages = len(messages)
    # List of messages only for displaying History on the right-side panel - last 7 comments only
    message_history = messages[:7]
    content = {'messages': messages, 'count_messages': count_messages, 'message_history': message_history}
    return render(request, 'messages/messages.html', content)


def new_message(request):
    """Add new message via form page"""
    messages = Message.objects.all().order_by("-date")
    count_messages = len(messages)
    # List of messages only for displaying History on the right-side panel - last 7 comments only
    message_history = messages[:7]
    content = {'messages': messages, 'count_messages': count_messages, 'message_history': message_history} 
    return render(request, 'messages/new_message.html', content)


def receive_message(request):
    """Receive message from FORM which add new message."""

    # Just for data inside right panel = History
    messages = Message.objects.all().order_by("-date")
    count_messages = len(messages)
    # List of messages only for displaying History on the right-side panel - last 7 comments only
    message_history = messages[:7]
    content = {'messages': messages, 'count_messages': count_messages, 'message_history': message_history} 

    # Values receive from Form
    title_value = ""
    text_value = ""
    author_value = ""
    mail_value = ""
    # These values has to be sent from form and needs to be not empty string
    mandatory_form_values = {'title': False, 'text': False}

    # TITLE:
    # Get 'title' from the form data or set flag (mandatory_form_values) for sending data again if title is empty string
    try:
        # Get title from sent Form
        title_value = request.POST['title']
	# Check if title isn't empty string and if yes then redirect to form again - should be pre-prepared form from preview values
	if len(title_value) == 0:
            mandatory_form_values['title'] = False
        else:
            mandatory_form_values['title'] = True
    except (KeyError):
        # Error: missing value 'title' from Form data
        content['error_message'] = "Chybi interni polozka 'Nadpis' z odeslaneho formulare !"
        return render(request, 'messages/new_message.html', content)

    # TEXT:
    # Get 'text' from the Form data or set flag (mandatory_from_values) for sending data again if text is empty string
    try:
        # Get text from sent form
        text_value = request.POST['text']
        # Check if text isn't empty string and if yes then redirect to form again - should be pre-prepared form from preview values
        if len(text_value) == 0:
            mandatory_form_values['text'] = False
        else:
            mandatory_form_values['text'] = True
    except (KeyError):
        # Error: missing value 'text' from Form data
        content['error_message'] = "Chybi interni polozka 'Text' z odelsaneho formulare !"
        return render(request, 'messages/new_message.html', content)

    # AUTHOR:
    # Get 'author' from the Form data or redirect to clear form again if there is a error
    try:
        # Get mail from sent form
        author_value = request.POST['author']
    except (KeyError):
        # Error: missing value 'mail' from Form data
        content['error_message'] = "Chybi interni polozka 'Autor' z odeslaneho formulare !"
        return render(request, 'messages/new_message.html', content)

    # MAIL:
    # Get 'mail' from the Form data or redirect to the clear form again if there is a error
    try:
        # Get mail from sent form
        mail_value = request.POST['mail']
    except (KeyError):
        # Error: missing value 'mail' from Form data
        content['error_message'] = "Chybi interni polozka 'Mail' z odeslaneho formulare !"
        return render(request, 'messages/new_message.html', content)

    content['title_value'] = title_value 
    content['author_value'] = author_value
    content['mail_value'] = mail_value
    content['text_value'] = text_value
    # Test if mandatory values (title and text) were receive correctly if not then redirect to form again
    if ((mandatory_form_values['title'] == False) and (mandatory_form_values['text'] == False)):
        # Mistake - Both 'title' and 'text' content are missing
        content['error_message'] = "Chybi povinne polozky 'Nadpis' a 'Text' ve formulari !"
        return render(request, 'messages/new_message.html', content)
    elif mandatory_form_values['title'] == False:
        # Mistake - item 'title' is missting (empty)
        content['error_message'] = "Zapomel jsi vyplnit 'Nadpis' ve formulari !'"
        return render(request, 'messages/new_message.html', content)
    elif mandatory_form_values['text'] == False:
        # Mistake - item 'text' is missing (empty)
        content['error_message'] = "Zapomel jsi vyplnit 'Text' ve formulari !"
        return render(request, 'messages/new_message.html', content)
    else:
        # Zpracovat formular
	# Vytvorit novou message a ulozit ji do DB
	# return HttpResponseRedirect
        comment = Message(title=title_value, author=author_value, mail=mail_value, text=text_value, date=timezone.now())
        comment.save()
        #return render(request, 'messages/receive_message.html', content)
        # Redirect to the list of existing messages
        return HttpResponseRedirect(reverse('messages:messages'))


