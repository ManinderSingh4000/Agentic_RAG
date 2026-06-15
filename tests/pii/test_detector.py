
from app.pii.detectors import (
    PIIDetector,
)

detector = PIIDetector()

text = """
Email:
maninder@gmail.com

Email:
saab3141@yahoo.com


Phone:
9876543210

Email:
Luca.261@gmail.com

Credit:
1234-1234-1234-q234

"""

print(
    detector.detect(text)
)