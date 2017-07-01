conf = {
    'door': {
        'state': False,
        'type': 'single',
        'room' : 'holway',
        'device_type': 'door',
        'strategy' : 'send',
        'communicator': 'bluetooth',
        'send_to_device': 'holway',
        'command': {True: 'O'}
    },
    'homeAlarm': {
        'state': False,
        'type': 'bi',
        'device_type': 'action',
        'room' : 'general',
        'strategy' : False,
        'communicator': False,
        'send_to_device': False,
        'command': False
    },
    'livingCourtainsDwn': {
        'state': False,
        'type': 'single',
        'device_type': 'courtains',
        'room' : 'living',
        'strategy': 'send',
        'communicator': 'bluetooth',
        'send_to_device': 'balcony',
        'command': {True: 'C3;'}
    },
    'livingCourtainsUp': {
        'state': False,
        'type': 'single',
        'device_type': 'courtains',
        'room' : 'living',
        'strategy': 'send',
        'communicator': 'bluetooth',
        'send_to_device': 'balcony',
        'command': {True: 'O3;'}
    },
    'closeAllLights': {
        'state': False,
        'type': 'single',
        'device_type': 'action',
        'room' : 'general',
        'strategy': 'group',
        'futureState': False,
        'actuators' : ['livingLight', 'bedroomLight', 'kitchenLight', 'holwayLight', 'closetLight', 'balconyLight'],
        'communicator': False,
        'send_to_device': False,
        'command': False
    },
    'livingCourtains': {
        'state': False,
        'type': 'bi',
        'device_type': 'courtains',
        'room' : 'living',
        'strategy': 'send',
        'communicator': 'bluetooth',
        'send_to_device': 'balcony',
        'command': {False: 'O50;', True: 'C50;'}
    },
    'livingLight': {
        'state': False,
        'type': 'bi',
        'device_type': 'light',
        'room' : 'living',
        'strategy': 'send',
        'communicator': 'serial',
        'encription': 'aes',
        'send_to_device': 'L1',
        'command': {False: '1C|', True: '1O|'}
    },
    'bedroomLight': {
        'state': False,
        'type': 'bi',
        'device_type': 'light',
        'room' : 'bedroom',
        'strategy': 'send',
        'communicator': 'serial',
        'encription': 'aes',
        'send_to_device': 'L1',
        'command': {False: '2C|', True: '2O|'}
    },
    'kitchenLight': {
        'state': False,
        'type': 'bi',
        'device_type': 'light',
        'room' : 'kitchen',
        'strategy': 'send',
        'communicator': 'serial',
        'encription': 'aes',
        'send_to_device': 'L1',
        'command': {False: '4C|', True: '4O|'}
    },
    'holwayLight': {
        'state': False,
        'type': 'bi',
        'device_type': 'light',
        'room': 'holway',
        'strategy': 'send',
        'communicator': 'serial',
        'encription': 'aes',
        'send_to_device': 'L1',
        'command': {False: '3C|', True: '3O|'}
    },
    'closetLight': {
        'state': False,
        'type': 'bi',
        'device_type': 'light',
        'room': 'closet',
        'strategy': 'send',
        'communicator': 'serial',
        'encription': 'aes',
        'send_to_device': 'L1',
        'command': {False: '5C|', True: '5O|'}
    },
    'balconyLight': {
        'state': False,
        'type': 'bi',
        'device_type': 'light',
        'room': 'balcony',
        'strategy': 'send',
        'communicator': 'serial',
        'encription': 'aes',
        'send_to_device': 'L1',
        'command': {False: '6C|', True: '6O|'}
    },
    'powerSocket1': {
        'state': False,
        'type': 'bi',
        'device_type': 'powerSocket',
        'room': 'living',
        'strategy': 'send',
        'communicator': 'serial',
        'encription': 'aes',
        'send_to_device': 'L1',
        'command': {False: '8C|', True: '8O|'}
    },
    'wemoSwitch1': {
        'state': False,
        'type': 'bi',
        'device_type': 'powerSocket',
        'room': 'holway',
        'strategy': 'wemo-switch',
        'communicator': 'wemoSwitch',
        'send_to_device': 'DanSwitch1',
    }
}