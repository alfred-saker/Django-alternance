from django import forms
from alternance.models import User,Offre


class UserRegistrationForm(forms.ModelForm):
    CHOICE_LEVEL = [
        ('GCE', 'GCE'),
        ('B', 'B'),
        ('BD', 'Bachelor Degree'),
        ('M', 'Mastere'),
    ]

    nom = forms.CharField(
        label="Nom",
        max_length=50,
        required=True,
        error_messages={'required': 'Please enter your name'},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Entrer votre nom.'})
    )
    username = forms.CharField(
        label="Username",
        max_length=50,
        required=True,
        error_messages={'required': 'Please enter your username'},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Entrer votre username.'})
    )
    level_school = forms.ChoiceField(
        choices=CHOICE_LEVEL,
        help_text="Choisissez votre niveau",
        label="Level School",
        required=True,
        error_messages={'required': 'Please enter your level choice'},
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    level_school.choices.insert(0, ("", "Select level school"))
    password = forms.CharField(
        label='Mot de passe',
        max_length=255,
        required=True,
        error_messages={'required': 'Please enter your password'},
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Entrer votre mot de passe.'})
    )
    email = forms.EmailField(
        label='Adresse e-mail',
        required=True,
        error_messages={'required': 'Please enter your email address'},
        widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Entrer votre adresse email.'})
    )

    class Meta:
        model = User
        fields = "__all__"

class UserLoginForm(forms.ModelForm):
  password = forms.CharField(
        label='Mot de passe',
        max_length=255,
        required=True,
        error_messages={'required': 'Please enter your password'},
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Entrer votre mot de passe.'})
    )
  username = forms.CharField(
        label="Username",
        max_length=50,
        required=True,
        error_messages={'required': 'Please enter your username'},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Entrer votre username.'})
    )
  class Meta():
    model = User
    fields = '__all__'

class OffreForm(forms.ModelForm):

  CHOICE_CONTRAT = [
        ('CDD', 'CONTRAT A DUREE DETERMINEE'),
        ('CDI', 'CONTRAT A DUREE INDETERMINEE'),
        ('ALTERNANCE', 'ALTERNANCE'),
        ('STAGE', 'STAGE'),
    ]
  
  poste = forms.CharField(
      label="Poste",
      max_length=50,
      required=True,
      error_messages={'required': 'Please enter poste'},
      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Entrer votre poste.'})
  )
  entreprise = forms.CharField(
      label="Entreprise",
      max_length=50,
      required=True,
      error_messages={'required': 'Please enter Entreprise'},
      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Entrer votre Entreprise.'})
  )
  localisation = forms.CharField(
      label="Localisation",
      max_length=50,
      required=True,
      error_messages={'required': 'Please enter localisation'},
      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Entrer votre localisation.'})
  )
  details = forms.CharField(
      label="Details",
      max_length=50,
      required=True,
      error_messages={'required': 'Please enter localisation'},
      widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Entrer votre localisation.', 'rows': 3})
  )
  choix_contrat = forms.ChoiceField(
      choices=CHOICE_CONTRAT,
      help_text="Choisissez le type de contrat",
      label="Contrat",
      required=True,
      error_messages={'required': 'Please enter your contrat choice'},
      widget=forms.Select(attrs={'class': 'form-control'})
  )
  choix_contrat.choices.insert(0, ("", "Select choix contrat"))
   
  user = forms.ModelChoiceField(
      queryset=User.objects.all(),
      widget=forms.HiddenInput,
      required=True
  )


  class Meta():
    model=Offre
    fields = "__all__"
