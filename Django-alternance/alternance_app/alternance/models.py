from django.db import models

# Create your models here.
class User(models.Model):
  id_user = models.BigAutoField(primary_key=True)
  nom = models.CharField(max_length=50)
  username = models.CharField(max_length=50, unique=True)
  email = models.EmailField(unique=True)
  level_school = models.CharField(max_length=50) 
  password = models.CharField(max_length=255)

  def __str__(self):
    return self.nom
  

class Offre(models.Model):
  id_offre = models.BigAutoField(primary_key=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  poste = models.CharField(max_length=50, unique=True)
  choix_contrat = models.CharField(max_length=50)
  entreprise = models.CharField(max_length=50)
  localisation = models.CharField(max_length=50)
  details = models.TextField()

  def __str__(self):
    return self.poste
  




