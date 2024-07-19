import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import traceback

from ai_code_generator import generate_code_and_execute

def create_visualization_agent(task_description, df_columns):
    task_with_columns = f"""
    The DataFrame has the following columns: {', '.join(df_columns)}. 
    {task_description}
    Use matplotlib or seaborn to create the visualization.
    After creating the plot, make sure to call 'plt.tight_layout()' to adjust the layout.
    """
    
    code = generate_code_and_execute(task_with_columns, execute=False)
    
    if code is None:
        return lambda data: (None, "Failed to generate visualization code")
    
    def agent(data):
        local_vars = globals().copy()
        local_vars.update({
            'df': data,
            'plt': plt,
            'sns': sns
        })
        
        try:
            # Clear any existing plots
            plt.clf()
            
            # Execute the code
            exec(code, local_vars)
            
            # Adjust the layout
            plt.tight_layout()
            
            # Capture the plot in a buffer
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            
            return buf, None
        except Exception as e:
            error_message = f"Error executing the generated code: {str(e)}\n{traceback.format_exc()}"
            return None, error_message
    
    return agent

def main():
    st.title("Data Visualization Agent")
    
    task_description = st.text_area("Describe the visualization you want to create:")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None and task_description:
        df = pd.read_csv(uploaded_file)
        
        st.write("Sample of the uploaded data:")
        st.dataframe(df.head())
        
        agent = create_visualization_agent(task_description, df.columns.tolist())
        plot_buffer, error = agent(df)
        
        if error:
            st.error(f"An error occurred: {error}")
        elif plot_buffer is not None:
            st.write("Generated Visualization:")
            st.image(plot_buffer)
            
            st.download_button(
                label="Download visualization as PNG",
                data=plot_buffer,
                file_name="visualization.png",
                mime="image/png",
            )
        else:
            st.warning("No visualization was generated. Please try a different description.")

if __name__ == "__main__":
    main()


    