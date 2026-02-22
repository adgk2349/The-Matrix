class GeminiAPIError(Exception):
    """Raised when the Gemini API returns a non-200 response or SSE error."""
    pass
