class Metadata:
    sample_id: str
    case_id: str
    sample_label: str
    data_type: str
    lanes: list

    def __init__(self, key: str, lanes: list):
        self.sample_id = key.split("/")[0]
        self.case_id = self.sample_id.split("-")[0]
        self.sample_label = self.sample_id.split("-")[1]
        self.data_type = key.split("/")[1]
        self.lanes = lanes
