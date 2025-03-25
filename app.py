import streamlit as st
import pandas as pd
import autocleaner

# Custom CSS styling for a prettier layout
st.markdown(
    """
    <style>
    /* Set a soft background and nice font */
    .main {
        background-color: #f9f9f9;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #333;
    }
    /* Header styling */
    h1, h2, h3 {
        color: #333;
    }
    /* Style for the buttons */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 0.5em 1em;
        margin: 0.5em 0;
    }
    /* File uploader styling */
    .stFileUploader {
        background-color: #fff;
        border: 1px solid #ddd;
        border-radius: 4px;
        padding: 1em;
    }
    </style>
    """, unsafe_allow_html=True
)

def main():
    st.title("Automated Dataset Cleaning and Visualization")
    st.markdown("""
    <p style='font-size:16px;'>
    Welcome! This application allows you to upload a CSV dataset, perform basic cleaning operations, and create visualizations.
    You can remove duplicate rows, handle missing values, inspect column data types, and generate interactive plots.
    Enjoy exploring your data!
    </p>
    """, unsafe_allow_html=True)

    # Sidebar for file upload
    st.sidebar.header("Upload Your Dataset")
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            st.error(f"Error reading CSV file: {e}")
            return
        
        st.subheader("Dataset Preview")
        st.dataframe(df.head())

        # Copy the original dataframe to perform cleaning operations
        cleaned_df = df.copy()

        st.header("Data Cleaning Options")
        # Option: Remove duplicate rows
        if st.checkbox("Remove duplicate rows"):
            cleaned_df, removed_count = autocleaner.remove_duplicates(cleaned_df)
            st.success(f"Removed {removed_count} duplicate row(s).")

        # Option: Handle missing values
        st.markdown("#### Handle Missing Values")
        missing_option = st.radio("Select a method for handling missing values:",
                                  ("None", "Remove rows with missing values", "Fill missing numeric values with mean"))
        if missing_option == "Remove rows with missing values":
            cleaned_df, message = autocleaner.handle_missing_values(cleaned_df, method="remove")
            st.success(message)
        elif missing_option == "Fill missing numeric values with mean":
            cleaned_df, message = autocleaner.handle_missing_values(cleaned_df, method="fill")
            st.success(message)
        else:
            st.info("No missing value operation selected.")

        # Allow users to download the cleaned dataset
        st.markdown("#### Download Cleaned Dataset")
        csv = cleaned_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Cleaned CSV",
            data=csv,
            file_name="cleaned_dataset.csv",
            mime="text/csv"
        )

        # Column inspection: select columns to view their data types
        st.header("Column Inspection")
        selected_columns = st.multiselect("Select columns to view their data types:", 
                                          options=cleaned_df.columns.tolist(), 
                                          default=cleaned_df.columns.tolist())
        if selected_columns:
            col_types = autocleaner.get_column_types(cleaned_df, selected_columns)
            st.write(col_types)

        # Visualization section
        st.header("Data Visualization")
        st.markdown("Create plots by selecting a plot type and specifying the x and y columns.")

        # Initialize session state for storing plot configurations
        if "plot_configs" not in st.session_state:
            st.session_state.plot_configs = []

        with st.form("plot_config_form", clear_on_submit=True):
            st.subheader("Add a Plot")
            plot_type = st.selectbox("Select plot type", ["Scatter", "Bar", "Line"])
            x_axis = st.selectbox("Select x-axis column", cleaned_df.columns.tolist(), key="x_axis")
            y_axis = st.selectbox("Select y-axis column", cleaned_df.columns.tolist(), key="y_axis")
            submitted = st.form_submit_button("Add Plot")
            if submitted:
                st.session_state.plot_configs.append({"type": plot_type, "x": x_axis, "y": y_axis})
                st.success(f"Added {plot_type} plot: {x_axis} vs {y_axis}")

        if st.session_state.plot_configs:
            st.subheader("Your Plots")
            for i, config in enumerate(st.session_state.plot_configs):
                st.markdown(f"**Plot {i+1}: {config['type']} ({config['x']} vs {config['y']})**")
                fig = autocleaner.create_plot(cleaned_df, config["type"], config["x"], config["y"])
                st.plotly_chart(fig, use_container_width=True)
            
            if st.button("Clear All Plots"):
                st.session_state.plot_configs = []
                st.experimental_rerun()
    else:
        st.info("Please upload a CSV file using the sidebar.")

if __name__ == "__main__":
    main()
