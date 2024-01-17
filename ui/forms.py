from django import forms
from .models import *

class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact
		fields = '__all__'

	full_name = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={
			'type':'text',
			'class':'input-contact rounded px-4 border-0 mb-3',
			'placeholder': 'Họ và tên *' 
			}
			)
		)

	phone = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={
			'type':'text',
			'class':'input-contact rounded px-4 border-0 mb-3',
			'placeholder': 'Số điện thoại *' 
			}
			)
		)

	email = forms.CharField(
		required=False,
		widget=forms.TextInput(
			attrs={
			'type':'text',
			'class':'input-contact rounded px-4 border-0 mb-3',
			'placeholder': 'Email' 
			}
			)
		)

	note = forms.CharField(
		required=True,
		widget=forms.Textarea(
			attrs={
			'type':'text',
			'class':'w-100 h-100 note-contact rounded p-3 border-0',
			'placeholder': 'Ghi chú *' 
			}
			)
		)