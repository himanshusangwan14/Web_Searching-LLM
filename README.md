# Meta LLaMA 3.1 8B Web Browser

## Overview

This repository contains a web browsing interface for the Meta LLaMA 3.1 8B language model. The model can be changed by modifying the `get_out.py` file.

## Setup and Run

To run the UI, follow these steps:

1. **Create a virtual environment**: Create a new virtual environment for the project.`python -m venv myenv`
2. **Activate the environment**: Activate the virtual environment. `source myenv/bin/activate` (on Linux/macOS) or `myenv\Scripts\activate` (on Windows)
3. **Clone Repo**: Clone this repository in your directory. `git clone https://github.com/VibhuRaj01/Web_Browsing_LLM`
4. **Set up environment variables**: Create a new file named .env in the root of the repository and add your Hugging Face token `HF_TOKEN=YOUR_HF_TOKEN_HERE` Replace *YOUR_HF_TOKEN_HERE* with your actual Hugging Face token.
5. **Install dependencies**: Install the required dependencies using pip. `pip install -r requirements.txt`
6. **Run the UI**: Start the application using unicorn. `unicorn main:run --reload`

**Note**: Make sure to modify the `get_out.py` file to change the language model if desired.
