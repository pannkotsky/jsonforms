from django import forms

from crispy_forms.bootstrap import Tab, TabHolder, Div
from crispy_forms.helper import FormHelper
from crispy_forms import layout
from select2 import forms as select2forms

from . import fields
from .models import Posting
from core import validators


class PostingForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ('title',)

    another__title = forms.CharField(max_length=20)
    base__country = fields.ChoiceField(choices=(
        ('DE', 'Germany'),
        ('AT', 'Austria'),
        ('CH', 'Switzerland'),
    ))
    base__city = forms.CharField(max_length=100, required=False)
    base__industries = fields.MultipleChoiceField(
        choices=(
            ('1', 'Agriculture'),
            ('2', 'IT'),
            ('3', 'Tourism'),
            ('4', 'Machine building')
        ),
        validators=[
            validators.min_select(2),
            validators.max_select(3)
        ],
        widget=select2forms.SelectMultiple(
            js_options={'maximum_selection_size': 3},
            overlay="Please choose"
        )
    )
    base__description_file = forms.FileField(
        required=False,
        allow_empty_file=True
    )

    helper = FormHelper()
    helper.layout = layout.Layout(
        TabHolder(
            Tab(
                'Main',
                'title',
            ),
            Tab(
                'Base tab',
                layout.Fieldset(
                    'Address',
                    Div(
                        Div('base__country', css_class='span6'),
                        Div('base__city', css_class='span6'),
                        css_class='row-fluid'),
                ),
                layout.Fieldset(
                    'Candidate',
                    'base__industries',
                    'base__description_file'
                ),
            ),
            Tab(
                'Another tab',
                'another__title',
            )
        )
    )
    helper.form_method = 'post'
    helper.form_action = ''
    helper.add_input(layout.Submit('submit', 'Save'))

    def clean(self):
        cleaned_data = super(PostingForm, self).clean()
        if cleaned_data['base__city'] == 'Berlin' and \
                cleaned_data['base__country'] != 'DE':
            msg = "Berlin is not in {}".format(cleaned_data['base__country'])
            self.add_error('base__city', msg)
        return cleaned_data
