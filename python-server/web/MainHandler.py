import pprint
from tornado.web import authenticated
from typeguard import typechecked

from web.BaseHandler import BaseHandler
from tools.JobControl import JobControll
from repository.Actuators import Actuators
from repository.Sensors import Sensors

class MainHandler(BaseHandler):
    @typechecked()
    def initialize(self, job_controll: JobControll, actuators_repo: Actuators, sensors_repo: Sensors):
        self.job_controll = job_controll
        self.__actuators_repo = actuators_repo
        self.__sensors_repo = sensors_repo

    @authenticated
    def get(self):
        actuators = self.__actuators_repo.get_actuators()
        filtered_actuators = self.__filter_actuator_by_type(actuators, 'bi')
        pprint.pprint(self.__group_actuators(actuators, 'room'))

        self.render(
            "./template/main.html",
            actuator_type_single = self.__filter_actuator_by_type(actuators, 'single'),
            actuator_type_bi = self.__group_actuators(filtered_actuators, 'device_type'),
            actuators = self.__group_actuators(actuators, 'room'),
            sensors = self.__sensors_repo.get_sensors(),
            selected_menu_item="home"
        )

    @authenticated
    def post(self, *args, **kwargs):
        actuator_name = self.get_argument("actuator_name", None, True)
        actuator_value = self.get_argument("actuator_value", None, True)
        self.job_controll.change_actuator(actuator_name, {'false' : False, 'true': True}[actuator_value])

    def __filter_actuator_by_type(self, actuators, type):
        return {key: data for key, data in list(actuators.items()) if actuators[key]['type'] == type}

    def __group_actuators(self, actuators, by):
        grouped_actuators = {}
        for actuator_name, actuator_properties in actuators.items():
            group_key = actuator_properties[by]
            if not group_key in grouped_actuators:
                grouped_actuators[group_key] = []
            actuator_data = actuators[actuator_name]
            actuator_data['name'] = actuator_name
            grouped_actuators[group_key].append(actuator_data)

        return grouped_actuators