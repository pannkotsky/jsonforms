from select2 import forms as select2forms


class ChoiceField(select2forms.ChoiceField):
    """Fix issue in select2 forms with adding choices to widget"""
    def _set_choices(self, value):
        self._choices = self.widget.choices = value


class MultipleChoiceField(select2forms.MultipleChoiceField):
    """Fix issue in select2 forms with adding choices to widget"""
    def _set_choices(self, value):
        self._choices = self.widget.choices = value
