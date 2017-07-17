from django import forms

class ParticipateForm(forms.Form):
    last_name = forms.CharField(
        label=(u'last_name'),
        widget=forms.TextInput(
            attrs={
                'id': (u'last_name'),
                'class': (u'validate'),
            }
        )
    )
    first_name = forms.CharField(
        label=(u'first_name'),
        widget=forms.TextInput(
            attrs={
                'id': (u'first_name'),
                'class': (u'validate'),
            }
        )
    )
    birthdate = forms.DateField(
        label=(u'birthdate'),
        widget=forms.DateInput(
            attrs={
                'id': (u'birthdate'),
                'class': (u'datepicker'),
            }
        )
    )
    email = forms.EmailField(
        label=(u'email'),
        widget=forms.TextInput(
            attrs={
                'id': (u'email'),
                'class': (u'validate'),
            }
        )
    )
    address = forms.CharField(
        label=(u'address'),
        widget=forms.TextInput(
            attrs={
                'id': (u'address'),
                'class': (u'validate'),
            }
        )
    )
    city = forms.CharField(
        label=(u'city'),
        widget=forms.TextInput(
            attrs={
                'id': (u'city'),
                'class': (u'validate'),
            }
        )
    )
    postal_code = forms.CharField(
        label=(u'postal_code'),
        widget=forms.NumberInput(
            attrs={
                'id': (u'postal_code'),
                'class': (u'validate'),
            }
        )
    )
    phone = forms.CharField(
        label=(u'phone'),
        required=False,
        widget=forms.NumberInput(
            attrs={
                'id': (u'phone'),
                'class': (u'validate'),
            }
        )
    )

