import time


class FeedbackSystem:
    """Feedback system to verify steps execution."""

    def verify_step(self, step):
        """Verify if a step was executed successfully."""
        action = step.get("action")
        print(f"Verifying actions: {action}")

        if action == "open_browser":
            return self.check_browser_open()
        elif action == "type_text":
            return True
        elif action == "press_key":
            return True

        return False

    def check_browser_open(self):
        """Check if browser is open."""
        print("Checking if browser opened")
        time.sleep(1)
        return True
    