import cv2 as cv
import numpy as np


class HSVClassifier:
    def __init__(self, teams) -> None:
        """
        Initialize the HSVClassifier.
        Parameters:
            teams (array): Array of tuples each with name, lower_hsv and upper_hsv values.
        Returns:
            HSV classifier instance.
        """
        self.teams = teams
        self.colors = self._extract_colors()

    def _extract_colors(self):
        colors = []
        for team in self.teams:
            color = {
                "name": team["name"],
                "lower_hsv": team["colors"]["lower_hsv"],
                "upper_hsv": team["colors"]["upper_hsv"],
            }
            colors.append(color)
        return colors

    def rgb_to_grayscale(self, img):
        """
        Convert an RGB image to grayscale.

        Parameters:
            img (numpy.ndarray): Input RGB image array (height x width x 3).

        Returns:
            numpy.ndarray: Grayscale image array (height x width).
        """
        r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
        grayscale_image = 0.2989 * r + 0.5870 * g + 0.1140 * b
        return grayscale_image.astype(np.uint8)

    def apply_mask(self, img, color):
        mask = cv.inRange(img, color["lower_hsv"], color["upper_hsv"])
        filtered_img = cv.bitwise_and(img, img, mask=mask)
        return filtered_img

    def inference(self, img):
        """
        Perform inference on an image

        Parameters:
            img (numpy.ndarray): Input RGB image array (height x width x 3).

        Returns:
            numpy.ndarray: Grayscale image array (height x width).
        """
        self.img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.img = cv.cvtColor(self.img, cv.COLOR_BGR2HSV)
        results = np.array([])
        for color in self.colors:
            self.filtered_img = self.apply_mask(self.img, color)
            grayscale_filtered_image = self.rgb_to_grayscale(self.filtered_img)
            number_of_black_pix = np.sum(grayscale_filtered_image == 0)
            results = np.append(results, number_of_black_pix)
        return self.colors[results.argmin()]["name"]
