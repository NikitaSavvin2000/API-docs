import subprocess
import os


# to_run_path = os.path.abspath("src/ui/pages/main_page.py")

to_run_path = os.path.abspath("src/ui/pages/streamlit_app.py")


def streamlit_run():
    subprocess.run(["streamlit", "run", to_run_path])


if __name__ == "__main__":
    streamlit_run()
