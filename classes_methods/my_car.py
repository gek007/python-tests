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

    def __hash__(self) -> int:
        return hash((self.brand, self.model, self.year))

    def __len__(self) -> int:
        return len(self.brand) + len(self.model) + len(self.year)

    def __getitem__(self, index: int) -> str:
        return self.brand[index]


mercedes = Car("Mercedes", "C-Class", 2020)
print(repr(mercedes))
