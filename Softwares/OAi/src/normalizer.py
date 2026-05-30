# this code handles normalizing user commands and adding some basic understanding
import json
import os


class Normalizer:
    """This class is used to clean and understand user input a bit better."""

    def __init__(self):
        """Load preferences and tools from config files."""

        # get current file location so paths don’t break
        base_dir = os.path.dirname(__file__)

        preferences_path = os.path.join(base_dir, "config", "preferences.json")
        tools_path = os.path.join(base_dir, "config", "tools.json")

        # load preferences
        with open(preferences_path, "r") as f:
            self.preferences = json.load(f)

        # load tools
        with open(tools_path, "r") as f:
            self.tools = json.load(f)

    def normalize_command(self, command_text):
        """Takes raw input and tries to clean + understand it."""

        # Step 1: make text simple (lowercase + remove extra spaces)
        normalized_text = command_text.lower().strip()

        # Step 2: create empty context
        context = {
            "keywords": [],
            "preferences": {}
        }

        # Step 3: check for keywords from preferences
        for keyword, prefs in self.preferences.items():
            if keyword in normalized_text:
                context["keywords"].append(keyword)
                context["preferences"].update(prefs)

        # Step 4: check for tools mentioned in command
        for tool_name, tool_info in self.tools.items():
            if tool_name.lower() in normalized_text:
                context["keywords"].append(tool_name.lower())
                context["preferences"]["tool"] = tool_name

        # Step 5: return cleaned text + context
        return normalized_text, context