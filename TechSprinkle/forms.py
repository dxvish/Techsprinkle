# from django import forms
# from .models import Projects
# import uuid
#
# class addProjectForm(forms.ModelForm):
#     projectname = forms.CharField(required=True,widget=forms.TextInput(attrs={'data-validate':'required,regex(^[a-zA-Z0-9 _-]*$,Invalid Project Name),size(3,30),projectNameCheck','class':'form-control'}))
#     description = forms.CharField(required=True,widget=forms.Textarea(attrs={'rows':3, 'cols':30,'class':'form-control'}))
#     class Meta:
#         model = Projects
#         fields = ('projectname', 'description','hashedprojectsid')
#
# class  editProjectForm(forms.ModelForm):
#     projectname = forms.CharField(required=True,widget=forms.TextInput(attrs={'data-validate':'required,regex(^[a-zA-Z0-9 _-]*$,Invalid Project Name),size(3,30),projectNameCheck','class':'form-control'}))
#     description = forms.CharField(required=True,widget=forms.Textarea(attrs={'rows':3, 'cols':30,'class':'form-control'}))
#     class Meta:
#         model = Projects
#         fields = ('projectname', 'description','hashedprojectsid')
#
# def validate_file_extension(value):
#         if not value.name.endswith('.csv'):
#             raise forms.ValidationError("Only CSV file is accepted")
#
# class UploadFileForm(forms.Form):
#     file = forms.FileField(label='Select a file',validators=[validate_file_extension])
#     projectsId = forms.CharField(required=True)
#
# class ValidatingPostVariables(forms.Form):
#     filePath =  forms.CharField(required=True)
#     projectsId = forms.CharField(required=True)
#
