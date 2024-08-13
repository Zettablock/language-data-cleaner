class ValueFormatError(Exception):
    """Exception raised for errors in the input or output format.

    Attributes:
        format -- input or output format which caused the error
        message -- explanation of the error
    """

    def __init__(self, format, message="Unsupported format provided"):
        self.format = format
        self.message = f"{message}: {format}"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'