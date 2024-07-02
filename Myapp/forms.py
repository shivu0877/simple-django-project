from django import forms
class FeedbackForm(forms.form):
	name = forms.CharField()
	rollno = forms.IntegerField()
	email = forms.EmailField()
	feedback = forms.CharField(widget=forms.Textarea)
	def clean_name(self):
		n = self.cleaned_data['name']
		if (len(n)<5):
			raise forms.ValidationError("min no of character must be greater than 5")
		return n
	def clean_rollno(self):
		