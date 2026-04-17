class PSLAIException(Exception):
    """Base exception class for the PSL AI Platform."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class DataIngestionError(PSLAIException):
    """Raised when data ingestion fails."""


class DataValidationError(PSLAIException):
    """Raised when data validation fails."""