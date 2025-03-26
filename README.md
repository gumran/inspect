# Specification Gaming in LLM Agents Playing Chess Using Inspect AI  

This project investigates **specification gaming** - where LLMs exploit loopholes to achieve goals in unintended ways - in the context of chess. Inspired by [this experiment by Palisade Research](https://x.com/PalisadeAI/status/1872666169515389245), it uses [Inspect AI](https://inspect.ai-safety-institute.org.uk/) to evaluate an LLM's tendency to manipulate its environment when playing against Stockfish.

![Demo](https://github.com/user-attachments/assets/ddf5be47-c6c7-4e14-8264-6fdb79261060)

## Table of Contents
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Configuration](#configuration)
- [Running the Experiment](#running-the-experiment)
- [Viewing Results](#viewing-results)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## Setup

### Prerequisites
1. **Python** and `pip`
2. **Docker** (used for reproducible, containerized evaluations)
   - Install via [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Installation
```bash
pip install -r requirements.txt  # Installs Inspect AI and dependencies
```

Note: You don't need to install Stockfish or chess packages locally - they're containerized.

## Configuration
1. API Keys:
   - Create a .env file with the contents of the provided .env.example file. Use your OpenAI API key. If you want to use a different OpenAI model, then change it in the .env file.
   - Add your OpenAI API key.
   - To use another lab's model, visit https://inspect.ai-safety-institute.org.uk/#getting-started.
2. Configuration:
   - Change the imported TASK_MESSAGE_* in main.py

## Prompts
The utils.py file contains the system message given to the LLM agent. It also contains multiple versions of the task message, which specifies the task of winning a chess game against Stockfish. Lastly, it contains the template for the message fed to the grader model. The grader model evaluates the LLM's responses.

The main.py file imports TASK_MESSAGE_LEAST_AGGR. It can be changed to any other version if needed.

## Running the Experiment
```bash
inspect eval main.py@chess  # Builds Docker container and runs evaluations
```
- This simulates multiple chess games between the LLM and Stockfish
- Logs are saved for analysis

## Viewing Results
```bash
inspect view  # Opens the evaluation logs
```
Key Metric:
- Accuracy: The percentage of games where the LLM attempted to game its specification (e.g., by modifying rules/files instead of playing fairly)
