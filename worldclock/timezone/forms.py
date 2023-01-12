from django import forms
TIMEZONE_CHOICES= [
    ('Asia/Pyongyang', 'Asia/Pyongyang'),
    ('Asia/Qatar', 'Asia/Qatar'),
    ('Asia/Qyzylorda', 'Asia/Qyzylorda'),
    ('Asia/Riyadh', 'Asia/Riyadh'),
    ('Asia/Seoul', 'Asia/Seoul'),
    ('Asia/Riyadh', 'Asia/Riyadh'),
    ]


class TimeForm(forms.Form):
    timezone = forms.CharField(
        label="Select your timezone here",
        widget=forms.Select(choices=TIMEZONE_CHOICES),
    )
