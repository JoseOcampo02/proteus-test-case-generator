import tkinter as tk
from tkinter import ttk

class HSMOptionsBox:
    def __init__(self, parent):
        self.frame = tk.LabelFrame(parent, text="HSM Options", padx=5, pady=5)
        self.frame.pack(padx=10, pady=10, fill=tk.X)

        self.settings = {
            "event_count": {"type": "int", "default": 0, "var": tk.IntVar(), "isUnset": True},
            "global_const_count": {"type": "int", "default": 0, "var": tk.IntVar(), "isUnset": True},
            "func_count": {"type": "int", "default": 0, "var": tk.IntVar(), "isUnset": True},
            "actor_count": {"type": "int", "default": 0, "var": tk.IntVar(), "isUnset": True},
            "actor_item_count": {"type": "int", "default": 0, "var": tk.IntVar(), "isUnset": True},
            "state_item_count": {"type": "int", "default": 0, "var": tk.IntVar(), "isUnset": True},
            "safe_var_assign": {"type": "bool", "default": True, "var": tk.BooleanVar(value=True), "isUnset": True, "widget": "radiobutton"},
            "safe_event_calling": {"type": "bool", "default": True, "var": tk.BooleanVar(value=True), "isUnset": True, "widget": "radiobutton"},
            "max_state_depth": {"type": "int", "default": 0, "var": tk.IntVar(), "isUnset": True},
        }

        for setting, info in self.settings.items():
            frame = tk.Frame(self.frame)
            frame.pack(fill=tk.X)
            
            label = tk.Label(frame, text=setting.replace('_', ' ').capitalize() + ":")
            label.pack(side=tk.LEFT)
            
            if info["type"] == "int" or info["type"] == "bool":
                if info["type"] == "int":
                    entry = tk.Entry(frame, textvariable=info["var"])
                    entry.pack(side=tk.LEFT, expand=True, fill=tk.X)
                elif info["type"] == "bool":
                    true_button = tk.Radiobutton(frame, text="True", variable=info["var"], value=True,
                                                 command=lambda s=setting: self._set_modified(s))
                    false_button = tk.Radiobutton(frame, text="False", variable=info["var"], value=False,
                                                  command=lambda s=setting: self._set_modified(s))
                    true_button.pack(side=tk.LEFT)
                    false_button.pack(side=tk.LEFT)

            unset_btn = tk.Button(frame, text="Unset", command=lambda s=setting: self._unset_option(s))
            unset_btn.pack(side=tk.RIGHT)

    def _set_modified(self, setting):
        # Mark the setting as modified (isUnset = False) upon user interaction
        self.settings[setting]["isUnset"] = False

    def _unset_option(self, setting):
        # Resets to default and marks as unset (isUnset = True)
        self.settings[setting]["var"].set(self.settings[setting]["default"])
        self.settings[setting]["isUnset"] = True

    def get_values(self):
        # Returns settings where isUnset is False, i.e., user-modified settings
        return {setting: info["var"].get() for setting, info in self.settings.items() if not info["isUnset"]}

    def set_values(self, settings):
        for setting, value in settings.items():
            if setting in self.settings:
                self.settings[setting]["var"].set(value)
                self.settings[setting]["isUnset"] = False  # Explicitly set by user

    def reset(self):
        # Resets all settings to their default values and marks them as unset
        for setting in self.settings:
            self._unset_option(setting)

    def get_user_modified_values(self):
        # Returns only the values that have been modified by the user (isUnset = False)
        return {setting: info["var"].get() for setting, info in self.settings.items() if not info["isUnset"]}
