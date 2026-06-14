
import re


class PIIDetector:

    EMAIL_PATTERN = (
        r"\b[A-Za-z0-9._%+-]+"
        r"@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    )

    PHONE_PATTERN = (
        r"\b\d{10}\b"
    )

    CREDIT_CARD_PATTERN = (
        r"\b(?:\d[ -]*?){13,16}\b"
    )

    def detect(
        self,
        text: str,
    ) -> dict:

        return {

            "emails": re.findall(
                self.EMAIL_PATTERN,
                text,
            ),

            "phones": re.findall(
                self.PHONE_PATTERN,
                text,
            ),

            "credit_cards": re.findall(
                self.CREDIT_CARD_PATTERN,
                text,
            ),
        }