import subprocess
import sys

def run_command(command, step_name):
    print(f"\n{'='*50}")
    print(f" STARTING PHASE: {step_name}")
    print(f"Executing: {command}")
    print(f"{'='*50}\n")
    
    result = subprocess.run(command, shell=True)
    
    if result.returncode != 0:
        print(f"\n ERROR: {step_name} failed! Stopping execution.")
        sys.exit(result.returncode)
    else:
        print(f"\n SUCCESS: {step_name} completed successfully.")

def setup_playwright():
    """Ensures Playwright browsers are installed automatically so the reviewer doesn't have to."""
    print("Checking Playwright browser installation...")
    # Installing playwright browsers (chromium) silently, skips if already installed
    subprocess.run("playwright install chromium", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    print("Starting InsiderOne End-to-End Test Suite...")
    
    setup_playwright()

    api_cmd = "python -m pytest tests/api/ -v -s"
    run_command(api_cmd, "API Testing (Swagger Petstore)")
    
    load_cmd = "locust -f tests/load/locustfile.py --headless -u 1 -r 1 -t 30s"
    run_command(load_cmd, "Load Testing (N11 Search)")
    
    ui_cmd = "python -m pytest tests/ui/ -v"
    run_command(ui_cmd, "UI Testing (InsiderOne Web)")
    
    print("\n" + "-"*25)
    print("ALL TEST PHASES COMPLETED SUCCESSFULLY!")
    print("-"*25 + "\n")

if __name__ == "__main__":
    main()