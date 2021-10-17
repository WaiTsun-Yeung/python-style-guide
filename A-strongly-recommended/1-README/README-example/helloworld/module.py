import numpy
import pyfiglet


def generate_message() -> None:
    """
    Returns a hello world message with a lucky number.
    """
    _RNG_MIN: int = 0
    _RNG_MAX: int = 10
    random_number_generator: numpy.random._generator.Generator = numpy.random.default_rng()
    lucky_number: numpy.typing.NDArray[numpy.int64] \
        = random_number_generator.integers(low=_RNG_MIN, high=_RNG_MAX, size=1)
    hello_world_message: str = "Hello, world! Your lucky number is " + str(lucky_number[0])
    _FONT: str = 'starwars'
    print(pyfiglet.figlet_format(hello_world_message, font=_FONT))
