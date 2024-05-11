# -----------------------------------------------------------------------------
# Authors: Wayne Rasmussen
# Date:    05/10/2024
# -----------------------------------------------------------------------------

class PTGConfig:
    def __init__(self, **kwargs):
        print("PTG is running...")
        self.settings = {
            'event_count': 3,
            'global_const_count': 3,
            'func_count': 3,
            'actor_count': 3,
            'actor_item_count': 10,
            'state_item_count': 10,
            'safe_var_assign': True,
            'safe_event_calling': True,
            'max_state_depth': 7,
            'input_directory': '',
            'output_directory': '',
        }

        # Print initial settings
        self.print_settings("Initial PTG Settings:")

        # Special handling for 'hsm_options' if present
        if 'hsm_options' in kwargs:
            hsm_options = kwargs.pop('hsm_options')
            self.settings.update(hsm_options)

        # Update directories if provided values are not empty
        for dir_key in ['input_directory', 'output_directory']:
            if dir_key in kwargs and kwargs[dir_key]:
                self.settings[dir_key] = kwargs[dir_key]

        # Update remaining settings
        self.settings.update(kwargs)

        # Print final settings
        self.print_settings("Final PTG Settings:")

    def print_settings(self, message):
        print(message)
        for key, value in self.settings.items():
            print(f'{key}: {value}')

def run_ptg(**kwargs):
    PTGConfig(**kwargs)

if __name__ == '__main__':
    print("hello from ptg")
    run_ptg()
