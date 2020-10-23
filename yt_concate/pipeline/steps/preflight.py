from .step import Step


class PreFlight(Step):
    def process(self, data, inputs, utils):
        print('in PreFlight')
        utils.create_dirs()

