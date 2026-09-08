"""Data Masking - Mask sensitive information in reports"""
import re


class DataMasker:
    """Mask sensitive data for safe display"""

    @staticmethod
    def mask_credit_card(cc_number: str) -> str:
        """Mask credit card number"""
        return f"{cc_number[:4]}****{cc_number[-4:]}"

    @staticmethod
    def mask_ssn(ssn: str) -> str:
        """Mask SSN"""
        return f"***-**-{ssn[-4:]}"

    @staticmethod
    def mask_email(email: str) -> str:
        """Mask email address"""
        parts = email.split("@")
        local = parts[0]
        domain = parts[1]
        return f"{local[:2]}***@{domain}"

    @staticmethod
    def mask_phone(phone: str) -> str:
        """Mask phone number"""
        digits = re.sub(r"\D", "", phone)
        return f"***-***-{digits[-4:]}"
