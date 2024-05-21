

from .models import Post, User, Stage, Logement, Event, Transport, Reaction
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields ="__all__"

class UserForm(ModelForm):
    class Meta:
        model = User
        fields ="__all__"

class StageForm(ModelForm):
    class Meta:
        model = Stage
        fields ="__all__"

class LogementForm(ModelForm):
    class Meta:
        model = Logement
        fields ="__all__"

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields ="__all__"

class TransportForm(ModelForm):
    class Meta:
        model = Transport
        fields ="__all__"


class ReactionForm(ModelForm):
    class Meta:
        model = Reaction
        fields = ['like', 'comment']