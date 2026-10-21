# JEV Experiment

Testing and evaluation with Vercel AI Gateway against **Jev** (`typesafe-ai/jev`).

## Features
- Evaluates customer inquiries with structured boolean, choice, and score questions.
- Communicates with Vercel AI Gateway evaluation API (`https://ai-gateway.vercel.sh/v1/evaluate`).

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shahzeb5136/JEV_Experiment.git
   cd JEV_Experiment
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Vercel AI Gateway API key:**
   - **Linux / macOS:**
     ```bash
     export AI_GATEWAY_API_KEY="your-api-key-here"
     ```
   - **Windows (Command Prompt / PowerShell):**
     ```powershell
     $env:AI_GATEWAY_API_KEY="your-api-key-here"
     ```
     Or persistently with:
     ```cmd
     setx AI_GATEWAY_API_KEY "your-api-key-here"
     ```

## Usage

Run the evaluation script:
```bash
python main.py
```
