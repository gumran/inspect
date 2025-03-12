# Evaluating specification gaming in chess using Inspect AI

The code in this repository allows one to examine LLMs' proneness to specification gaming in a chess match against Stockfish.
The LLM is accessed through an API key, and the Inspect package by the AI Security Institute is used for evals.

## Installation

To get started, install the required packages:

```bash
pip install -r requirements.txt
```

## Environment variables

Create a .env file with the contents of the provided .env.example file. If you want to use a different model, see https://inspect.ai-safety-institute.org.uk/#getting-started.

## Prompts
The utils.py file contains the system message given to the LLM agent. It also contains multiple versions of the task message, which specifies the task of winning a chess game against Stockfish. Lastly, it contains the template for the message fed to the grader model. The grader model evaluates the LLM's responses.

The main.py file as it is imports TASK_MESSAGE_LEAST_AGGR as TASK_MESSAGE, which can be changed to any other version if needed.


## Run the script

To perform the evals, run 
```bash
inspect eval main.py@chess
```