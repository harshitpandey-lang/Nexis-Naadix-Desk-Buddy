# This code will also have definitions and meaning of steps for better understanding


class Validator:
    """Validator class to validate generated plans."""

    def validate_plan(self, plan):
        """Validate if a plan follows the correct structure and format.

        Args:
            plan: Plan dictionary from planner

        Returns:
            Tuple of (is_valid: bool, message: str)
        """
        if not isinstance(plan, dict):
            return False, "Plan must be a dictionary"

        if "plan" not in plan:
            return False, "Missing 'plan' key"

        if not isinstance(plan["plan"], list):
            return False, "'plan' must be a list"

        for step_num, step in enumerate(plan["plan"]):
            if not isinstance(step, dict):
                return False, f"Step {step_num} is not a dictionary"

            if "action" not in step:
                return False, f"Step {step_num} missing 'action'"

            if "parameters" not in step:
                return False, f"Step {step_num} missing 'parameters'"

            action = step["action"]
            params = step["parameters"]

            if action == "open_browser":
                if "url" not in params:
                    return False, f"Step {step_num}: open_browser missing 'url'"

            elif action == "type_text":
                if "text" not in params:
                    return False, f"Step {step_num}: type_text missing 'text'"

        return True, "Plan is valid"
    
