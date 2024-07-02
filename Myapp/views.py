from django.shortcuts import render
from Myapp.forms import FeedBackForm



# Create your views here.
def feedbackView(request):
	f=FeedBackForm()
	if request.method=="POST":
		f=FeedBackForm(request.POST)
		if f.is_valid():
			name=f.cleaned_data['name']
			rollno=f.cleaned_data['rollno']
			email=f.cleaned_data['email']
			feedback=f.cleaned_data['feedback']
			d={'name':name,'rollno':rollno,'email':email,'feedback':feedback}
			return render(request,'Myapp/output.html',d)
		
	d={'form':f}
	return render(request,'Myapp/feedback.html',d)

# Create your views here.
