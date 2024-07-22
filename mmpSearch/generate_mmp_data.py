import subprocess

def run_script(script_path):
    subprocess.run(['python', script_path])

def main():
    script_path = 'scripts/indexa.py'
    run_script(script_path)

    script_path = 'scripts/statistics.py'
    run_script(script_path)

if __name__ == '__main__':
    main()
