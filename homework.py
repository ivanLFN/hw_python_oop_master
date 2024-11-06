class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass


class Training:
    """
    A base class to training.
    ...
    Constants
    ---------
    LEN_STEP : float
        Distance covered by an athlete in one step, in meters.
    M_IN_KM : int
        Constant for converting results from meters to kilometers.

    Attributes
    ----------
    action : int
        Number of actions performed.
    duration : float
        Duration of the training session in hours.
    weight : float
        Weight of the athlete in kilograms.

    Methods
    -------
    get_distance():
        Calculates the distance covered during the training.
    get_mean_speed():
        Calculates the mean speed the training.
    get_spent_calories():
        Calculates the spent calories the training.
    show_training_info():
        Return training info message.
    """

    LEN_STEP = 0.65
    M_IN_KM = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight: weight

    def get_distance(self) -> float:
        """Get distance in km."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Get mean speed."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Get spent calories."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Return training info message."""
        return InfoMessage()
        pass


class Running(Training):
    """Тренировка: бег."""
    pass


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    pass


class Swimming(Training):
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
