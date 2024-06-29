from HSVClassifier import HSVClassifier


class PlayerDetector:

    def __init__(self, model, teams) -> None:
        """
        Initialize the PlayerDetector.
        Parameters:
            model : model used to do inference.
        Returns:
            detected player.
        """
        self.model = model
        self.teams = teams
        self.team_classifier = HSVClassifier(self.teams)

    def inference(self, frame):
        """
        Does inference on a frame (image).
        Parameters:
            frame (image)
        Returns:
            Standard yolov5 output.
        """
        results = self.model(frame)
        objects = results.crop(save=False)
        return objects
        res = []
        for object in objects:
            label = " ".join(object["label"].split(" ")[:-1])
            if label != "person":
                continue
            # x is used to only show the top part of the image
            x = int(3 * object["im"].shape[0] / 5)
            player_img = object["im"][0:x, :]
            current_player_team = self.team_classifier.inference(player_img)
            if current_player_team == self.teams[0]["name"]:
                color = self.teams[0]["bgr_color"]
            else:
                color = self.teams[1]["bgr_color"]
            res.append(
                {"box": object["box"], "team": current_player_team, "bgr_color": color}
            )
        return res
