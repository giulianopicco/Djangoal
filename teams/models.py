from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Team(models.Model):
    name = models.CharField(max_length=255)
    couch = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    location = models.CharField(max_length=255)
    photo = models.ImageField(verbose_name='Imágen de fondo', null=True, blank=True, default='team_default.jpg')


    def get_absolute_url(self):
        return reverse('teams:detail', kwargs={'team_pk': self.pk})

    class meta:
        ordering = ['name']

    def __str__(self):
        return 'Team {}'.format(self.name)



class Player(models.Model):
    GOALKEEPER = 0
    RIGHT_FULLBACK = 1
    LEFT_FULLBACK = 2
    CENTER_BACK = 3
    SWEEPER = 4
    DEFENDING_MIDFIELDER =5
    RIGHT_MIDFIELDER = 6
    CENTRAL = 7
    STRIKER = 8
    ATTACKING_MIDFIELDER = 9
    LEFT_MIDFIELDER = 10

    POSITIONS = (
        (GOALKEEPER, 'Goalkeeper'),
        (RIGHT_FULLBACK, 'Right Fullback'),
        (LEFT_FULLBACK, 'Left Fullback'),
        (CENTER_BACK, 'Center Back'),
        (SWEEPER, 'Sweeper'),
        (DEFENDING_MIDFIELDER, 'Defending Midfielder'),
        (RIGHT_MIDFIELDER, 'Right Midfielder'),
        (CENTRAL, 'Central'),
        (STRIKER, 'Striker'),
        (ATTACKING_MIDFIELDER, 'Attacking Midfielder'),
        (LEFT_MIDFIELDER, 'Left_midfielder'),
    )

    name = models.CharField(max_length=255)
    position = models.IntegerField(default=0, choices=POSITIONS)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, default=None)

    def get_position(self):
        return self.POSITIONS[self.position][1]