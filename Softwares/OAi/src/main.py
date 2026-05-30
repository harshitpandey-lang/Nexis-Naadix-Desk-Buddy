from fastapi import FastAPI
from src.normalizer import Normalizer
from src.planner import Planner
from src.validator import Validator
from src.executor import Executor

app = FastAPI()

# Initialize components (load once, not per request)
normalizer = Normalizer()
planner = Planner()
validator = Validator()
executor = Executor()


@app.get("/")
def home():
    return {"message": "OAI Cloud Backend is running 🚀"}


@app.post("/plan")
def generate_plan(data: dict):
    """
    Step 1: Receive task from user/hardware
    Step 2: Normalize
    Step 3: Plan
    Step 4: Validate
    Step 5: Return plan (not executing yet)
    """
    user_input = data.get("task", "")

    # Normalize
    normalized_text, context = normalizer.normalize_command(user_input)

    # Plan
    plan = planner.generate_plan(normalized_text, context)

    # Validate
    is_valid, message = validator.validate_plan(plan)

    return {
        "normalized": normalized_text,
        "context": context,
        "plan": plan,
        "valid": is_valid,
        "message": message
    }


@app.post("/execute")
def execute_plan(data: dict):
    """
    Optional: execute plan from hardware side
    """
    plan = data.get("plan", {})

    success = executor.execute_plan(plan)

    return {
        "success": success
    }