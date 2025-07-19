# blog_website/weird_blog/forms.py

from django import forms
from .models import Topic, Entry # Ensure Topic and Entry are imported

# Form for adding a new Topic
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text'] # THIS LINE IS ABSOLUTELY ESSENTIAL AND MUST BE PRESENT
        labels = {'text': ''} # Optional: remove the default label

# Form for adding a new Entry to a Topic
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text'] # This line is also essential for EntryForm
        labels = {'text': 'Entry:'} # Optional: customize the label
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} # Optional: make textarea wider
