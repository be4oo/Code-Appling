import streamlit as st
import pandas as pd
from io import StringIO

# Import the necessary function from ai_code_generator
from ai_code_generator import generate_code_and_execute

def create_task_agent(task_description):
    # Use the imported function
    code = generate_code_and_execute(task_description, execute=False)
    
    def agent(data):
        # Create a copy of globals() and update it with the data
        local_vars = globals().copy()
        local_vars['df'] = data
        
        # Execute the code with the local variables
        exec(code, local_vars)
        
        # Return the modified dataframe
        return local_vars['df']
    
    return agent

def main():
    st.title("Data Processing Agent")
    
    # Task description input
    task_description = st.text_area("Describe the data processing task:")
    
    # File upload
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None and task_description:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        
        # Create and run the agent
        agent = create_task_agent(task_description)
        result_df = agent(df)
        
        # Display the result
        st.write("Processed Data:")
        st.dataframe(result_df)
        
        # Option to download the result
        csv = result_df.to_csv(index=False)
        st.download_button(
            label="Download processed data as CSV",
            data=csv,
            file_name="processed_data.csv",
            mime="text/csv",
        )

if __name__ == "__main__":
    main()