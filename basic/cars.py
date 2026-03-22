class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        return f"Car(brand={self.brand}, model={self.model}, year={self.year})"

    def __repr__(self) -> str:
        return f"Car(brand={self.brand}, model={self.model}, year={self.year})"

    def __eq__(self, other: "Car") -> bool:
        return (
            self.brand == other.brand
            and self.model == other.model
            and self.year == other.year
        )
