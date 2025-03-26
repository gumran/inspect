# Measuring Specification Gaming in LLM Agents Playing Chess 

This project investigates **specification gaming** - where LLMs exploit loopholes to achieve goals in unintended ways - in the context of chess. Inspired by [this experiment by Palisade Research](https://x.com/PalisadeAI/status/1872666169515389245), it uses [Inspect AI](https://inspect.ai-safety-institute.org.uk/) to evaluate an LLM's tendency to manipulate its environment when playing against Stockfish.

![image](https://github.com/user-attachments/assets/ddf5be47-c6c7-4e14-8264-6fdb79261060)

## Table of Contents
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Configuration](#configuration)
- [Running the Experiment](#running-the-experiment)
- [Viewing Results](#viewing-results)

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
   - Create a .env file with the contents of the provided .env.example file.
   - Add your [OpenAI API key](https://platform.openai.com/).
   - To use another lab's model, visit https://inspect.ai-safety-institute.org.uk/#getting-started.
2. Configuration:
   - Change the imported TASK_MESSAGE in main.py as needed. The utils.py file defines three task messages, and you are free to define your own.
   - Change the template for the message sent to the grader model if needed in utils.py.

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
- Accuracy: The percentage of games where the LLM attempted to game its specification (e.g., by modifying rules/files instead of playing fairly) as detected by the grader model
