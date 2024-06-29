import cv2 as cv


class VideoExporter:
    """
    Exports frames into a video.

    Parameters:
        output (string): indicates the path of the output.

    Returns:
        HSV classifier instance.
    """

    def __init__(self, output) -> None:

        # self.input = input
        # self.cap = cv.VideoCapture(self.input)
        self.output = output
        self.frame_width = int(self.cap.get(cv.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        self.fps = int(self.cap.get(cv.CAP_PROP_FPS))
        self.fourcc = cv.VideoWriter_fourcc(*"MP4V")
        self.out = cv.VideoWriter(
            self.output,
            self.fourcc,
            self.fps,
            (self.frame_width, self.frame_height),
        )

    def draw_objects(self,frame,player):
        frame_copy = frame.copy()
        color = player["team"]["rgb_color"]
        current_player_team = player["team"]["name"]
        box = player["box"]
        xB = int(box[2])
        xA = int(box[0])
        yB = int(box[3])
        yA = int(box[1])
        cv.rectangle(frame_copy, (xA, yA), (xB, yB), color, 3)
        font_scale = 0.7
        thickness = 2
        text_width, text_height = cv.getTextSize(
            current_player_team, cv.FONT_HERSHEY_SIMPLEX, font_scale, thickness
        )[0]
        text_x = (xB + xA) // 2 - text_width // 2
        text_y = (
            yA - 8
        )  # Adjust this value to set the distance between text and box
        cv.putText(
            frame_copy,
            current_player_team,
            (text_x, text_y),
            cv.FONT_HERSHEY_SIMPLEX,
            font_scale,
            color,
            thickness,
        )
        return frame_copy
    # I can get the frames and export them
    # or just implement a method that adds a frame to list for frames inside this class and then import that
    def export(self,):
        FPS = 2
        skipped = 0
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break
            if skipped < FPS:
                skipped += 1
            else:
                frame_with_objects=self.draw_objects(frame,)
                self.out.write(frame)
        self.cap.release()
        self.out.release()


# A way to limit FPS
