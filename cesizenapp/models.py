import uuid
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Information(models.Model):
    CATEGORY = [
        ('SANTE-MENTAL', 'Comprendre la santé mentale'),
        ('RECONNAITRE-LE-STRESS', 'Reconnaître le stress'),
        ('GESTION-DU-STRESS', 'Techniques de gestion du stress'),
        ('COMPTRENDRE-EMOTIONS', 'Comprendre ses émotions'),
        ('HABITUDES', 'Habitude de vie et auto-soin'),
        ('ACTIVITES', 'Activités de détente'),
        ('DEMANDER-L-AIDE', 'Quand demander de l`aide'),
        ('SOUTENIR', 'Soutenir un proche'),
        ('DRAFT', 'Unavailable to the public')
    ]
    idInformation = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, null=False)
    caption = models.CharField(max_length=100)
    content = models.CharField(max_length=5000, null=False)
    image = models.ImageField(upload_to="images", null=True)
    alt = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=200, null=False, choices=CATEGORY, default='DRAFT')
    publicationDate = models.DateTimeField(auto_now_add=True, null=False)

class Diagnostic(models.Model):
    score = models.IntegerField(editable=False, null=False)
    result = models.TextField(editable=False, null=False)
    diagnosticDate = models.DateTimeField(auto_now_add=True, null=False)
    diagnosticUser = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=False)

class StressEvent(models.Model):
    description = models.CharField(max_length=255)
    score = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.description} ({self.score})"