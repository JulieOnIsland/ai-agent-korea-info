# 🤖 RAG-based AI Agent for World Population and Korea Data

Welcome to the RAG-based AI Agent project, designed to provide quick and accurate information on global population statistics and detailed insights about South Korea. 🌍🇰🇷

## 📋 Overview
This project utilizes the Retrieval-Augmented Generation (RAG) model to create an intelligent agent capable of processing both structured and unstructured data. It offers functionalities to answer queries related to world population data and extract information from Wikipedia on South Korea.

## 🛠️ RAG (Retrieval-Augmented Generation)
RAG combines retrieval-based methods with language generation, enabling the AI agent to retrieve relevant information from a large dataset and generate responses based on the retrieved data. This approach enhances the agent's ability to provide accurate and contextually relevant answers to user queries.

## 🎯 Usage
1. **Main Functionality:** The primary function of the AI agent is to answer questions regarding global population statistics and provide detailed insights into South Korea.
   
2. **Data Sources:**
   - **Population Data:** Utilizes a structured dataset (`population.csv`) containing global population information. You can download it from [here](https://www.kaggle.com/datasets/joebeachcapital/world-population-by-country-2023).
   - **South Korea Information:** Extracts data from Wikipedia (`South_Korea.pdf`) using a vector store index.
   
3. **Note-taking Feature:** The agent can also take notes based on user prompts. Simply input a prompt containing a query and a request to save a note, and the agent will generate the response and store it in a `notes.txt` file.

## 🖥️ Implementation
The project is implemented in Python, with the main functionality encapsulated in the `main.py` script. This script orchestrates the interaction between various components, including query engines, tools, and the RAG-based AI model.

## 🚀 Getting Started
1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the `main.py` script to start the AI agent.
4. Input prompts to query population data or request information about South Korea.

### 📝 Example 
**Prompt:** 
can you tell me about k-pop and save a note for me

**Result:**
K-pop is a genre of popular music that originated in South Korea and has evolved significantly since the emergence of the pop group Seo Taiji and Boys in 1992. It has incorporated elements from various musical genres and trends globally while maintaining its traditional Korean music roots. K-pop idols are well-known in Asia and have gained fame in the Western world, with notable successes like Psy's international hit "Gangnam Style" in 2012 contributing to its global recognition.

**Result will be saved in notes.txt**

## 📚 Reference
This repository was created based on the "ADVANCED Python AI Agent Tutorial - Using RAG" YouTube video by TechWithTim. You can find the tutorial [here](https://www.youtube.com/watch?v=ul0QsodYct4&ab_channel=TechWithTim).
