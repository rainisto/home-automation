from typeguard import typechecked

from repository.SensorsRepository import SensorsRepository
from ifttt.parser.TokenConverter import TokenConverter
from ifttt.parser.Token import Token


class SensorTokenConverter(TokenConverter):
    @typechecked()
    def __init__(self, sensors_repository: SensorsRepository) -> None:
        self.__sensors_repository = sensors_repository

    @typechecked()
    def get_value(self, token_raw_value: str):
        sensor = self.__sensors_repository.get_sensor(token_raw_value)
        if None is not sensor:
            return sensor.value

    def get_supported_token(self) -> str:
        return Token.TYPE_SENSOR