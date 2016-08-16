from django import forms
from .models import User


# class LoginForm(forms.Form):
# 	username = forms.CharField(label='Username',max_length=100)
# 	password = forms.CharField(label="Password",max_length=100,widget=forms.PasswordInput())


# class RegistrationForm(forms.Form):
# 	username = forms.CharField(label='Username',max_length=100)
# 	password = forms.CharField(label="Password",max_length=100,widget=forms.PasswordInput())


class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('email', 'password')
		labels = {
			'email': 'Email',
			'password': 'Password'
		}
		widgets = {
			'email': forms.TextInput(
				attrs = {
					'placeholder': 'Enter email',
					'autofocus': 'autofocus'
				}
			),
			'password': forms.PasswordInput(
				attrs = {
					'placeholder': 'Enter password'
				}
			)
		}

	def clean(self):
		data = self.cleaned_data
		email = data.get('email')
		if email is None:
			raise forms.ValidationError('Invalid email!')
		password = data.get('password')
		if password is None:
			raise forms.ValidationError('Invalid password')
		return data


class RegistrationForm(forms.ModelForm):

	confirm_password =  forms.CharField(
		label="Password again",
		max_length=100,
		required=True,
		widget=forms.PasswordInput()
	)
	# captcha = CaptchaField()
	class Meta:
		model = User
		fields = (
			'full_name', 'user_type', 'dept', 'email', 'password'
		)
		labels = {
			'full_name': 'Full Name',
			'user_type': 'User Type',
			'dept': 'Department',
			'email': 'Email',
			'password': 'Password'
		}
		widgets = {
			'email': forms.TextInput(
				attrs = {
					'placeholder': 'Enter email',
					'autofocus': 'autofocus'
				}
			),
			'password': forms.PasswordInput(
				attrs = {
					'placeholder': 'Enter password'
				}
			)
		}

	def clean(self):
		data = self.cleaned_data
		dept = data.get('dept')
		if dept is None:
			raise forms.ValidationError('Invalid department!')
		email = data.get('email')
		if email is None:
			raise forms.ValidationError('Invalid Email')
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('User already exists')
		password = data.get('password')
		if password is None:
			raise forms.ValidationError('Invalid password')

		return data