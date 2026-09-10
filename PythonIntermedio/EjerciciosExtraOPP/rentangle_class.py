class Rectangle:
    def __init__(self, width : float , height : float ):
        if width < 0 or height < 0:
            raise ValueError ("El ancho y la altura no pueden ser negativos.")

        self.width = width
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return 2*(self.width + self.height)


