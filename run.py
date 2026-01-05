import random

print("===================================")
print(" AI Agent Learning From Mistakes ")
print("===================================")
print("System initialized successfully.")


# ---------------- TOOL ----------------
def lookup_tool(question):
    """
    Simulated tool that fetches information.
    This tool is REQUIRED before answering.
    """
    print("[Tool] lookup_tool called")
    return f"Fetched information related to: '{question}'"


# ---------------- AGENT ----------------
class SimpleAgent:
    def __init__(self):
        self.used_tool = False
        self.tool_output = None

    def run(self, question, force_tool=False):
        print("\n[Agent] New task received:", question)

        # Decide whether to use tool
        if force_tool or random.choice([True, False]):
            self.tool_output = lookup_tool(question)
            self.used_tool = True
        else:
            print("[Agent] Skipped tool usage (mistake)")

        print("[Agent] Producing final answer...")
        if self.used_tool:
            return f"Answer based on tool output: {self.tool_output}"
        else:
            return "Answer produced without using tool"


# ---------------- EVALUATOR ----------------
def evaluate_run(agent):
    if agent.used_tool:
        print("[Evaluator] Run successful")
        return True, None
    else:
        print("[Evaluator] Run failed: Tool was not used")
        return False, "skipped_tool"


# ---------------- MEMORY ----------------
mistake_memory = {
    "skipped_tool": 0
}


def learn_from_mistake(mistake_type):
    if mistake_type:
        mistake_memory[mistake_type] += 1
        print(f"[Memory] Recorded mistake: {mistake_type} -> {mistake_memory[mistake_type]}")


# ---------------- MAIN LOOP ----------------
print("\n================ RUNNING MULTIPLE TRIALS ================\n")

for run_id in range(1, 6):
    print(f"\n----- RUN {run_id} -----")

    agent = SimpleAgent()

    # Learning rule:
    # After 2 failures, force tool usage
    force_tool_usage = mistake_memory["skipped_tool"] >= 2

    result = agent.run("What is AI?", force_tool=force_tool_usage)
    print("Final Output:", result)

    success, mistake = evaluate_run(agent)

    if not success:
        learn_from_mistake(mistake)