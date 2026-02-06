from django import forms
from django.core.mail.message import EmailMessage
from django.conf import settings

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
        
        conteudo = f"Nome: {nome}\nEmail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}"
        mail = EmailMessage(
            subject='Email enviado pelo django2',
            body=conteudo,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=['arthur.resende.gomes1@gmail.com'],
            headers={'Reply-To': email}
        )
        
        mail.send()


