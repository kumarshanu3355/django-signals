class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def __iter__(self):
        """Allows iteration over the object, first returning length, then width."""
        yield {"length": self.length}
        yield {"width": self.width}

# Example usage
rect = Rectangle(10, 5)
for item in rect:
    print(item)
