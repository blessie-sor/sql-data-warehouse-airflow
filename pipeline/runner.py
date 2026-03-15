import subprocess
import os

def run_sql_file(filepath):
    print(f"Running: {filepath}")
    
    result = subprocess.run(
        [
            "psql",
            "-h", "postgres-dwh",
            "-p", "5432",
            "-U", "dwh_user",
            "-d", "data_warehouse",
            "-f", filepath
        ],
        env={**os.environ, "PGPASSWORD": "dwh_password"},
        capture_output=True,
        text=True
    )
    
    print(result.stdout)
    
    if result.returncode != 0:
        print(result.stderr)
        raise Exception(f"SQL file failed: {result.stderr}")
    
    print(f"Done: {filepath}")