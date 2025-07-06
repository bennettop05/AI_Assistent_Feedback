import json
from datetime import datetime

def log_trace(question, thought, tool_used, tool_output, final_answer):
    log_entry = {
        "timestamp": str(datetime.now()),
        "question": question,
        "thought": thought,
        "tool_used": tool_used,
        "tool_output": tool_output,
        "final_answer": final_answer
    }

    try:
        with open("trace_log.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(log_entry)

    with open("trace_log.json", "w") as f:
        json.dump(data, f, indent=4)

def load_trace_logs():
    try:
        with open("trace_log.json", "r") as f:
            return json.load(f)
    except:
        return []
