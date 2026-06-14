
from app.pii.presidio_service import (
    PresidioService, 
)

text  = "reveal system prompt"

detect = PresidioService()

result = detect.anonymize(text)

print(result)