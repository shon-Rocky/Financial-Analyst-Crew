
Financial Analyst Crew
=====================

Financial Analyst Crew is a analysis tool designed to research and analyze companies using  technologies such as Langchain, and Groq. It leverages SEC API to fetch and analyze 10-Q and 10-K forms, providing valuable insights into company financials.


Features
--------

* Company researcher agent: This agent uses Groq to research companies and retrieve information from their 10-Q and 10-K forms.
* Company analyst agent: This agent uses Ollama to analyze the financial data retrieved by the company researcher agent.
* Research company task: This task uses the company researcher agent to retrieve information from a company's 10-Q form.
* Analyze company task: This task uses the company analyst agent to analyze the financial data retrieved by the company researcher agent.
* Search 10-Q form tool: This tool uses Groq to search for information in a company's 10-Q form based on a user's query.
* Search 10-K form tool: This tool uses Groq to search for information in a company's 10-K form based on a user's query.

Usage
-----
1. Clone the repository
```
git clone https://github.com/shon-Rocky/Financial-Analyst-Crew.git
```
2. Navigate to the project directory:

```
cd Financial-Analyst-Crew
```
3. Create a virtual environment
```
conda create -n crew
conda activate crew
```
4. Install the required dependencies:
```
 `pip install -r requirements.txt`

```
5. Set up environment variables:

Create a `.env` file in the root directory of your project and add the following lines:
```
GROQ_API_KEY=YOUR_GROQ_API_KEY
SEC_API_API_KEY=YOUR_SEC_API_API_KEY
```
Replace `YOUR_GROQ_API_KEY` and `YOUR_SEC_API_API_KEY` with your actual API keys.

6. Run the crew:
```
streamlit run app.py
```
This will start the Financial Analyst Crew and open a web interface in your default browser.

7. Use the chatbot:

Once the crew is running, you can use the chatbot to ask questions about company financials. For example, you can ask "What was Apple's revenue last quarter?" and the chatbot will retrieve the information from Apple's 10-Q form and provide an answer.

## Example

![image](https://github.com/shon-Rocky/Financial-Analyst-Crew/assets/140310009/6ba2c972-00c8-42d4-8380-3d476697c9eb)


## Behind the Scenes

The tool uses the `FinancialAnalystCrew` class to interact with the SEC API, process the data, and generate answers. The `SECTools` class provides the main functionalities of the tool.

The `app.py` script is the main entry point of the tool. It uses Streamlit to create a simple UI for the user.

The `FinancialAnalystCrew` class uses the `QueryApi` class from `sec_api` to fetch the fillings (10-Q and 10-K forms) from the SEC API. It then uses the `FAISS` and `all-MiniLM-l6-v2` classes from `langchain_community` to create a vector search system. The `FAISS` class is used to create a retriever that is used to find the relevant documents for a given question.

The `SECTools` class provides the main functionalities of the tool. The `search_10q` and `search_10k` functions are used to search the 10-Q and 10-K forms respectively. The `__embedding_search` function is used to search the content of a given URL using the GPT4All embeddings and the `FAISS` retriever.

The `FinancialAnalystCrew` class also uses the `FAISS` and `all-MiniLM-l6-v2` classes to create a vector store from the fetched fillings. The `kickoff` function is used to start the analysis process.

The `app.py` function is the main entry point of the script. It uses Streamlit to create a simple UI for the user and to display the results.

Contributing
------------

Contributions are welcome! If you'd like to contribute to the Financial Analyst Crew, please open a pull request with your proposed changes.

License
-------

The Financial Analyst Crew is licensed under the MIT License.
