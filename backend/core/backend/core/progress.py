progress_state = {}

def update(file_id, step, percent):
    progress_state[file_id] = {"step": step, "percent": percent}

def get(file_id):
    return progress_state.get(file_id, {})
