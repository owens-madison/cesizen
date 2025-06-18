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
    content = models.CharField(max_length=1000, null=False)
    image = models.ImageField(upload_to="images", null=True)
    alt = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=200, null=False, choices=CATEGORY, default='DRAFT')
    publicationDate = models.DateTimeField(auto_now_add=True, null=False)

class Comment(models.Model):
    idComment = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.CharField(max_length=150, null=False)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=False)
    commentDate = models.DateTimeField(null=False)

class Diagnostic(models.Model):
    RESULTS = [
        (300, 'vos risques de présenter dans un avenir proche, une maladie somatique, sont très élevés. '
              'Un score de 300 et plus suppose que vous avez eu à traverser une série de situations particulièrement pénibles et éprouvantes. '
              'Ne craignez donc pas de vous faire aider si c’est votre cas.'),
        (100, 'Les risques que se déclenche une éventuelle maladie somatique demeure statistiquement significatif. '
              'Prenez soin de vous. Ce n’est pas la peine d’en rajouter.'),
        (0, 'Le risque se révèle peu important. '
            'La somme des stress rencontrés en une année est trop peu importante pour ouvrir la voie à une maladie somatique.'),
    ]
    score = models.IntegerField(editable=False, null=False)
    result = models.CharField(max_length=350, choices=RESULTS, editable=False, null=False)
    diagnosticDate = models.DateTimeField(null=False)
    diagnosticUser = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=False)