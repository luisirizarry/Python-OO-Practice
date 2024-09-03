"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = start
        self.next = start  

    def generate(self):
        """Make the next number."""
        current = self.next
        self.next += 1
        return current

    def reset(self):
        """Reset the number to the start number"""
        self.next = self.start

