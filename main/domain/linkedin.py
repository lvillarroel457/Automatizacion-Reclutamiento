class LinkedinFilter:
    def __init__(self, filter_name, description, possible_values):
        self.filter_name = filter_name
        self.description = description
        self.possible_values = possible_values

    @classmethod
    def from_json(cls, json_data):
        return cls(
            json_data['filter_name'],
            json_data['description'],
            json_data['possible_values']
        )

    def to_json(self):
        return {
            "filter_name": self.filter_name,
            "description": self.description,
            "possible_values": self.possible_values
        }

    def __str__(self):
        return f"LinkedinFilter(filter_name={self.filter_name}, description={self.description}, possible_values={self.possible_values})"
