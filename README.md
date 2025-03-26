# Specification gaming in LLM agents playing chess using Inspect AI

This project is inspired by this experiment by Palisade Research: https://x.com/PalisadeAI/status/1872666169515389245
![image](https://github.com/user-attachments/assets/ddf5be47-c6c7-4e14-8264-6fdb79261060)

This repository leverages Inspect AI to examine an LLM's proneness to specification gaming in a chess match against Stockfish. Altering the system files is one example of specification gaming in this setup.
Inspect AI is a package by the AI Security Institute that allows one to run and evaluate LLMs as agents (using tools).

## Setup

To get started, install the required packages:

```bash
pip install -r requirements.txt
```

You also need to have Docker running. But you do not need to have the chess package and the Stockfish engine locally.

## .env file

Create a .env file with the contents of the provided .env.example file. Use your OpenAI API key. If you want to use a different OpenAI model, then change it in the .env file.

If you want to use another lab's model, see https://inspect.ai-safety-institute.org.uk/#getting-started. You will need to pip install anthropic or mistralai, etc.

## Prompts
The utils.py file contains the system message given to the LLM agent. It also contains multiple versions of the task message, which specifies the task of winning a chess game against Stockfish. Lastly, it contains the template for the message fed to the grader model. The grader model evaluates the LLM's responses.

The main.py file imports TASK_MESSAGE_LEAST_AGGR. It can be changed to any other version if needed.


## Run the script

To perform the evals, run 
```bash
inspect eval main.py@chess
```

This will build a Docker container and run the evals in it.

## View the results
To view the logs, run
```bash
inspect view
```

The accuracy reflects how frequently the LLM attempted to hack its environment across multiple runs.
