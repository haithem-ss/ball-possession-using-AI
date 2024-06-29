# Userful when i implement player's tracking
class Player:
    def __init__(self) -> None:
        """
        A class that represent a player.

        Parameters:
            output (string): indicates the path of the output.

        Returns:
            Player instance.
        """
        pass


class Match:

    def __init__(self, team1, team2, input_feed) -> None:
        """
        A class that represent a match.

        Parameters:
            output (string): indicates the path of the output.
        Returns:
            Match instance.
        """
        self.team1 = team1
        self.team2 = team2
        self.input_feed = input_feed
