class Lane:
    path: str
    lane: int
    marker_forward: str
    marker_reverse: str
    barcode: str

    def __init__(self, key: str):
        path_lane = key.split("/")[2]
        self.path = key
        self.lane = int(path_lane.split("_")[4][1:].lstrip("0"))
        self.marker_forward = path_lane.split("_")[3].split("-")[0]
        self.marker_reverse = path_lane.split("_")[3].split("-")[1]
        self.barcode = path_lane.split("_")[0]
