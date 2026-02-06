from django import forms
from django.core.mail.message import EmailMessage
from django.conf import settings
from dotenv import load_dotenv
import os
load_dotenv()

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email')
    assunto = forms.CharField(label='Assunto')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())
    
    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']
        
        TO_PERSONS = os.environ.get('TO_EMAIL')
        mail = EmailMessage(
            subject=assunto,
            body=f'{nome} te enviou a seguinte mensagem:\n{mensagem}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[TO_PERSONS],
            headers={'Reply-To': email}
        )
        
        mail.send()


