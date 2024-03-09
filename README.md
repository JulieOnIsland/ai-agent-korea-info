# RAG-based AI Agent for World Population and Korea Data

Welcome to the RAG-based AI Agent project, designed to provide quick and accurate information on global population statistics and detailed information about South Korea. 🌍🇰🇷

## Overview
This project utilizes the Retrieval-Augmented Generation (RAG) model to create an intelligent agent capable of processing both structured and unstructured data. It offers functionalities to answer queries related to world population data and extract information from Wikipedia on South Korea.

## RAG (Retrieval-Augmented Generation)
RAG combines retrieval-based methods with language generation, enabling the AI agent to retrieve relevant information from a large dataset and generate responses based on the retrieved data. This approach enhances the agent's ability to provide accurate and contextually relevant answers to user queries.

## Usage
1. **Main Functionality:** The primary function of the AI agent is to answer questions regarding global population statistics and provide detailed insights into South Korea.
   
2. **Data Sources:**
   - **Population Data:** Utilizes a structured dataset (`population.csv`) containing global population information. You can download it from [here](https://www.kaggle.com/datasets/joebeachcapital/world-population-by-country-2023).
   - **South Korea Information:** Extracts data from Wikipedia (`South_Korea.pdf`) using a vector store index.
   
3. **Note-taking Feature:** The agent can also take notes based on user prompts. Simply input a prompt containing a query and a request to save a note, and the agent will generate the response and store it in a `notes.txt` file.

## Implementation
The project is implemented in Python, with the main functionality encapsulated in the `main.py` script. This script orchestrates the interaction between various components, including query engines, tools, and the RAG-based AI model.
