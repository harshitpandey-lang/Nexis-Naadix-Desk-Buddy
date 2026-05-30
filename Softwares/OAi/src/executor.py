# This code will also have definitions and meaning of steps for better understanding
import time
from src.utils.hid_codes import get_hid_code
from src.utils.communication import send_to_nexis


class Executor:
    """Executor class to execute plans."""

    def execute_plan(self, plan):
        """Execute a plan with the given steps."""
        if not isinstance(plan, dict) or "plan" not in plan:
            print("Invalid plan format")
            return False

        for step_num, step in enumerate(plan["plan"]):
            action = step.get("action")
            parameters = step.get("parameters", {})

            print(f"\nExecuting step {step_num}: {action}")

            hid_commands = []

            if action == "open_browser":
                hid_commands.append(get_hid_code("GUI_LEFT", "press"))
                hid_commands.append(get_hid_code("r", "press"))
                hid_commands.append(get_hid_code("GUI_LEFT", "release"))
                hid_commands.append(get_hid_code("r", "release"))

                time.sleep(0.5)

                hid_commands.append(get_hid_code("enter", "press"))
                hid_commands.append(get_hid_code("enter", "release"))

                time.sleep(1)

                url = parameters.get("url", "")
                hid_commands.append(get_hid_code(url, "type"))

                hid_commands.append(get_hid_code("enter", "press"))
                hid_commands.append(get_hid_code("enter", "release"))

            elif action == "type_text":
                text = parameters.get("text", "")
                hid_commands.append(get_hid_code(text, "type"))

            elif action == "press_key":
                key = parameters.get("key")
                if key:
                    hid_commands.append(get_hid_code(key, "press"))
                    hid_commands.append(get_hid_code(key, "release"))

            elif action == "click_element":
                x = parameters.get("x", 0)
                y = parameters.get("y", 0)
                hid_commands.append(get_hid_code("mouse_left", "left", x, y))

            for cmd in hid_commands:
                send_to_nexis(cmd)

            time.sleep(0.1)

        print("\nAll steps executed successfully")
        return True

            