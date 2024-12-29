from django.core.exceptions import ValidationError
import re


class CustomPasswordValidator:
    def validate(self, password, user=None):
        if not re.search(r"[A-Z]", password):
            raise ValidationError(
                "Password must contain at least one uppercase letter.",
                code="password_no_upper",
            )
        if not re.search(r"[a-z]", password):
            raise ValidationError(
                "Password must contain at least one lowercase letter.",
                code="password_no_lower",
            )
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError(
                "Password must contain at least one special character.",
                code="password_no_symbol",
            )

    def get_help_text(self):
        return "Your password must contain at least one uppercase letter, one lowercase letter, and one special character."
