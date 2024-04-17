import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from crew import FinancialAnalystCrew

def run():
    st.title("Financial Analyst Crew")
    company_name = st.text_input("Enter Company Name:", "Reliance Industries Ltd")
    
    # Add an exit button
    if st.button("Exit"):
        st.stop()
    
    if st.button("Analyze"):
        inputs = {
            'company_name': company_name,
        }
        output = FinancialAnalystCrew().crew().kickoff(inputs=inputs)
        st.write(output)

if __name__ == "__main__":
    run()
