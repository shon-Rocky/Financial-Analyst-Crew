import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from crew import FinancialAnalystCrew

def run():
    st.title("Financial Analyst ")
    company_name = st.text_input("Enter Company Name:", "Reliance Industries Ltd")
    
    
    
    if st.button("Analyze"):
        inputs = {
            'company_name': company_name,
        }
        output = FinancialAnalystCrew().crew().kickoff(inputs=inputs)
        st.write(output)
    if st.button("Clear"):
        # Clear the output area
        st.empty()

if __name__ == "__main__":
    run()
