class InfoMessage:
    """
    A class to show a training information.
    ...
    Attributes
    ----------
    training_type : str
        Name to training class.
    duration : float
        Duration of the training session in hours.
    distance : float
        Training distance in kilometers.
    speed : float
        Mean speed to training.
    calories : float
        Count of calorie burned.

    Methods
    -------
    get_message()
        Return string of message.
    """

    def __init__(
            self,
            training_type: str,
            duration: float,
            distance: float,
            speed: float,
            calories=None
    ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')


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
    TRAINING_TYPE : str
        Type of training for use in child classes.

    Attributes
    ----------
    action : int
        Number of actions performed.
    duration : float
        Duration of the training session in hours.
    weight : float
        Weight of the athlete in kilograms.
    distance : float
        Training distance in kilometers.
    speed : float
        Mean speed to training.
    calories : float
        The count of kilocalories that the user burned during the workout.

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
    MIN_IN_H = 60

    def __init__(
                    self,
                    action: int,
                    duration: float,
                    weight: float,
                ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.distance = self.get_distance()
        self.speed = self.get_mean_speed()
        self.calories = None

    def get_distance(self) -> float:
        """Get distance in km."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Get mean speed."""
        return self.distance / self.duration

    def get_spent_calories(self) -> float:
        """Get spent calories."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Return training info message."""
        return InfoMessage(
            self.__class__.__name__,
            self.duration,
            self.distance,
            self.speed,
            self.calories
        )


class Running(Training):
    """Training: run."""

    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79

    def __init__(
            self,
            action: int,
            duration: float,
            weight: float
    ):
        super().__init__(action, duration, weight)
        self.calories = self.get_spent_calories()

    def get_spent_calories(self) -> float:
        """Get spent calories."""
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER *
                 self.speed + self.CALORIES_MEAN_SPEED_SHIFT) *
                self.weight / self.M_IN_KM * self.duration * self.MIN_IN_H)


class SportsWalking(Training):
    """Training: sport walking."""

    CALORIES_WEIGHT_MULTIPLIER = 0.035
    CALORIES_SPEED_HEIGHT_MULTIPLIER = 0.029
    KH_TO_MS = 0.278
    CM_IN_M = 100

    def __init__(
            self,
            action: int,
            duration: float,
            weight: float,
            height: float
    ):
        super().__init__(action, duration, weight)
        self.height = height
        self.calories = self.get_spent_calories()

    def get_spent_calories(self) -> float:
        """Get spent calories."""
        speed = self.speed * self.KH_TO_MS

        return ((self.CALORIES_WEIGHT_MULTIPLIER * self.weight
                 + (speed ** 2 / (self.height / self.CM_IN_M))
                 * self.CALORIES_SPEED_HEIGHT_MULTIPLIER * self.weight)
                * self.duration * self.MIN_IN_H)


class Swimming(Training):
    """Training: swimming."""

    LEN_STEP = 1.38
    CALORIES_MEAN_SPEED_MULTIPLIER = 1.1
    CALORIES_MEAN_SPEED_SHIFT = 2

    def __init__(
            self,
            action: int,
            duration: float,
            weight: float,
            length_pool: float,
            count_pool: int
    ):
        self.length_pool = length_pool
        self.count_pool = count_pool
        super().__init__(action, duration, weight)
        self.calories = self.get_spent_calories()

    def get_mean_speed(self) -> float:
        """Get mean speed."""
        return (self.length_pool * self.count_pool /
                self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        """Get spent calories."""
        return ((self.speed + self.CALORIES_MEAN_SPEED_MULTIPLIER)
                * self.CALORIES_MEAN_SPEED_SHIFT *
                self.weight * self.duration)


def read_package(workout_type: str, data: list) -> Training:
    """Read data received from sensors."""
    training_types = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    return training_types[workout_type](*data)


def main(training: Training) -> None:
    """Main function."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
