from django.db import models
from myproj.settings import AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=8)
    email = models.EmailField()

    def __str__(self):
        return self.nom + ' ' + self.prenom + ' ' + self.telephone+' '+str(self.email)
class Post(models.Model):
    image = models.ImageField(upload_to="media")
    slug= models.SlugField(max_length=200)
    TYPE_CHOICES = [
        (0, 'Offre'),
        (1, 'Demande'),
    ]
    type = models.IntegerField(choices=TYPE_CHOICES)
    date=models.DateField()
    User= models.ForeignKey(AUTH_USER_MODEL, on_delete= models.CASCADE)

    def __str__(self):
        return str(self.type)+' '+str(self.date)

class Reaction(models.Model):
    comment = models.TextField()
    like = models.BooleanField()
    User= models.ForeignKey(User, on_delete=models.CASCADE)
    Post= models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment + ' ' + str(self.like)

class Recommandation(Post):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Transport(Post):
    depart = models.CharField(max_length=255)
    destination = models.CharField(max_length=200)
    heuredep = models.TimeField()
    nbresieges = models.IntegerField()
    contactInfo = models.CharField(max_length=200)

    def __str__(self):
        return self.depart + ' ' + self.destination + ' ' + str(self.heuredep) + ' ' + str(self.nbresieges)+' '+self.contactInfo
    

class Logement(models.Model):
    localisation = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    contactInfo = models.CharField(max_length=200)

    def __str__(self):
        return self.localisation + ' ' + self.description+' '+self.contactInfo

class Stage(models.Model):
    TYPE_CHOICES = [
        (1, 'Ouvrier'),
        (2, 'Technicien'),
        (3, 'PFE'),
    ]
    typeStg = models.IntegerField(choices=TYPE_CHOICES)
    societe = models.CharField(max_length=200)
    duree = models.TextField()
    sujet = models.CharField(max_length=200)
    contactInfo = models.CharField(max_length=200)
    specialite = models.CharField(max_length=200)

    def __str__(self):
        return str(self.typeStg) + ' ' + self.societe + ' ' + str(self.duree) + ' ' + self.sujet+' '+self.contactInfo+' '+self.specialite


class Event(Post):
    intitule = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    lieu = models.CharField(max_length=200)
    contactInfo = models.CharField(max_length=200)

    def __str__(self):
        return self.intitule + ' ' + self.description + ' ' + self.lieu + ' ' + self.contactInfo
    

class EvenClub(Event):
    club = models.CharField(max_length=200)
    

    def __str__(self):
        return self.club

class EvenSocial(Event):
    prix = models.DecimalField(max_digits=15, decimal_places=3)
    

    def __str__(self):
        return str(self.prix)
