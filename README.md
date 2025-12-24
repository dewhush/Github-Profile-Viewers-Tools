# Github Profile Views Tool

A Python-based tool to automate profile views on GitHub using Selenium. This tool allows you to increase the view count on your GitHub profile counter by simulating visits.

## Features
- **Headless Mode**: Runs in the background without opening a visible browser window.
- **Anti-Detection**: Implements various techniques to avoid detection as an automated bot.
- **Multi-Threading**: Supports concurrent visits to speed up the process.
- **Human-like Scrolling**: Simulates natural user behavior during visits.

## Prerequisites
- Python 3.x installed
- Google Chrome browser installed

## Installation

1.  **Clone or Download the Repository**
    ```bash
    git clone https://github.com/dewhush/Github-Profile-Viewers-Tools.git
    cd Github-Profile-Viewers-Tools
    ```

2.  **Install Dependencies**
    It is recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Script**
    ```bash
    python main.py
    ```

2.  **Follow the Prompts**
    - **Target Username**: Enter the GitHub username you want to target (e.g., `dewhush`).
    - **Number of Views**: Enter the desired number of views to generate.
    - **Number of Threads**: Enter the number of concurrent threads to use (default is 5). Higher numbers are faster but use more resources.

    **Example:**
    ```text
    === GitHub Profile Viewer (Fast Mode) ===
    Target Username: dewhush
    Number of Views: 100
    Number of Threads (Default 5): 10
    ```

3.  **Process**
    The script will start visitors in separate threads. You will see progress logs in the terminal.
    ```text
    [+] Visit 1/100 success
    [+] Visit 2/100 success
    ...
    Done! 100/100 successful.
    ```

## Disclaimer
This tool is for educational purposes only. Using automated scripts to artificially inflate metrics may violate GitHub's Terms of Service. Use at your own risk. The author is not responsible for any misuse or consequences.
