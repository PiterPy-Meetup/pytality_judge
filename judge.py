import functools
import json
import os
import subprocess
import sys

CODE_USER = "user.py"
CODE_SAMPLE = "sample.py"
INPUT_SCHEMA_ARG = 1
RUNS_NUMBER = 10


def generate_data(input_schema: dict) -> dict:
    """Generate random test data from JSON Schema"""
    return (1, 2)  # TODO implement me


if __name__ == "__main__":
    input_schema = json.loads(sys.argv[INPUT_SCHEMA_ARG])

    runs_results = []
    for _ in range(RUNS_NUMBER):
        args = " ".join(map(str, generate_data(input_schema)))

        run = functools.partial(
            subprocess.run,
            input=args,
            text=True,
            check=True,
            timeout=0.5,
            stdout=subprocess.PIPE,
        )

        result = run(("python", CODE_USER))
        user_result = result.stdout

        result = run(("python", CODE_SAMPLE))
        sample_result = result.stdout

        runs_results.append(user_result == sample_result)

    if not all(runs_results):
        sys.exit(1)
