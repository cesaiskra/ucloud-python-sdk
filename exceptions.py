class UCLOUDException(Exception):
    def __str__(self):
        return "Error"


class ConnectionRefused(Exception):
    """
    Connection refused: the server refused the connection.
    """
    def __init__(self, response=None):
        self.response = response

    def __str__(self):
        return "ConnectionRefused: %s" % repr(self.response)