
from presidio_analyzer import (
    AnalyzerEngine,
)

from presidio_anonymizer import (
    AnonymizerEngine,
)


class PresidioService:

    def __init__(self):

        self.analyzer = (
            AnalyzerEngine()
        )

        self.anonymizer = (
            AnonymizerEngine()
        )

    def analyze(
        self,
        text: str,
    ):

        return self.analyzer.analyze(
            text=text,
            language="en",
        )

    def anonymize(
        self,
        text: str,
    ):

        results = (
            self.analyze(text)
        )

        anonymized = (
            self.anonymizer.anonymize(
                text=text,
                analyzer_results=results,
            )
        )

        return anonymized.text