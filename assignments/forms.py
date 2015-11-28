from django import forms

from assignments.models import AssignmentUpload


class AssignmentUploadForm(forms.ModelForm):
    class Meta:
        model = AssignmentUpload
        fields = ('file',)


    def __init__(self, *args, **kwargs):
        self.assignment = kwargs.pop('assignment')
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.instance.assignment = self.assignment
        self.instance.user = self.user



