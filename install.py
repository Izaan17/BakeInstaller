import os
import subprocess
import sys
import shutil


def download_and_clone_repo(repo_url, save_dir, overwrite=False):
    """Download and clone the GitHub repository files."""
    if os.path.exists(save_dir):
        if overwrite:
            print(f"Directory {save_dir} exists. Overwriting...")
            shutil.rmtree(save_dir)  # Delete existing directory if overwrite is enabled
        else:
            print(f"Directory {save_dir} already exists. Skipping cloning.")
            return  # Skip cloning if directory exists and overwrite is not allowed

    try:
        clone_repo(repo_url, save_dir)
    except Exception as e:
        print(f"Error cloning repository: {e}")


def clone_repo(repo_url, save_dir):
    """Clone the repository, including .git data."""
    print(f"Cloning repository {repo_url} into {save_dir}...")
    try:
        subprocess.check_call(['git', 'clone', repo_url, save_dir], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Repository cloned successfully into {save_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error while cloning the repository: {e}")
        raise  # Re-raise to propagate error


def install_requirements(requirements_path):
    """Install dependencies from the requirements.txt file."""
    if os.path.exists(requirements_path):
        print(f"Installing dependencies from {requirements_path}...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_path, '--break-system-packages'],
                                  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("Dependencies installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing dependencies: {e}")
    else:
        print(f"No 'requirements.txt' found at {requirements_path}")


def run_script(script_path):
    """Run the specified Python script."""
    print(f"Running script: {script_path}...")
    try:
        subprocess.check_call([sys.executable, script_path, '--install'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Script {script_path} executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running script {script_path}: {e}")


def checkout_branch(branch_name):
    """Checkout the specified branch."""
    print(f"Switching to branch '{branch_name}'...")
    try:
        subprocess.check_call(['git', 'checkout', branch_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Successfully switched to branch '{branch_name}'")
    except subprocess.CalledProcessError as e:
        print(f"Error switching to branch '{branch_name}': {e}")


if __name__ == '__main__':
    repo_url = 'https://github.com/Izaan17/Bake'
    save_dir = os.path.join(os.path.expanduser('~'), '.bake')  # Directory where repo will be saved
    overwrite = True

    # Step 1: Download and clone the repository
    download_and_clone_repo(repo_url, save_dir, overwrite)

    # Step 2: Change working directory to the cloned repo
    os.chdir(save_dir)

    # Step 3: Checkout the specific branch
    # checkout_branch('bake-2.0')

    # Step 4: Install dependencies from requirements.txt
    requirements_path = os.path.join(save_dir, 'requirements.txt')
    install_requirements(requirements_path)

    # Step 5: Run the main Python script
    script_path = os.path.join(save_dir, 'main.py')
    run_script(script_path)