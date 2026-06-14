
from app.pii.anonymizer import (
    PIIAnonymizer,
)

anonymizer = (
    PIIAnonymizer()
)

text = """
Email:
maninder@gmail.com

Email:
saab3141@yahoo.com


Phone:
9876543210

Email:
Luca.261@gmail.com

"""

print(
    anonymizer.anonymize(
        text
    )
)