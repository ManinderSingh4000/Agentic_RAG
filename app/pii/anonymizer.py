
import re

from app.pii.detectors import (
    PIIDetector,
)


class PIIAnonymizer:

    def __init__(self):

        self.detector = (
            PIIDetector()
        )

    def anonymize(
        self,
        text: str,
    ) -> str:

        text = re.sub(
            self.detector.EMAIL_PATTERN,
            "[EMAIL]",
            text,
        )

        text = re.sub(
            self.detector.PHONE_PATTERN,
            "[PHONE]",
            text,
        )

        text = re.sub(
            self.detector.CREDIT_CARD_PATTERN,
            "[CARD]",
            text,
        )

        return text