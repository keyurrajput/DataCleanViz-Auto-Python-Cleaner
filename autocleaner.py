import pandas as pd
import numpy as np
import plotly.express as px

def remove_duplicates(df):
    """
    Removes duplicate rows from the DataFrame.
    Returns the cleaned DataFrame and the number of rows removed.
    """
    initial_len = len(df)
    cleaned_df = df.drop_duplicates()
    removed = initial_len - len(cleaned_df)
    return cleaned_df, removed

def handle_missing_values(df, method="none"):
    """
    Handles missing values in the DataFrame.
    
    Parameters:
        df (pd.DataFrame): The input DataFrame.
        method (str): The method to handle missing values:
            - "none": Do nothing.
            - "remove": Remove rows with any missing values.
            - "fill": Fill missing numeric values with the column mean.
    
    Returns:
        cleaned_df (pd.DataFrame): The DataFrame after handling missing values.
        message (str): A message summarizing the operation.
    """
    cleaned_df = df.copy()
    if method == "remove":
        before = len(cleaned_df)
        cleaned_df = cleaned_df.dropna()
        removed_rows = before - len(cleaned_df)
        return cleaned_df, f"Removed {removed_rows} row(s) with missing values."
    elif method == "fill":
        numeric_cols = cleaned_df.select_dtypes(include=[np.number]).columns.tolist()
        cleaned_df[numeric_cols] = cleaned_df[numeric_cols].fillna(cleaned_df[numeric_cols].mean())
        return cleaned_df, "Filled missing numeric values with their mean."
    else:
        return cleaned_df, "No missing value operation performed."

def get_column_types(df, columns):
    """
    Returns the data types of the selected columns.
    """
    return df[columns].dtypes

def create_plot(df, plot_type, x, y):
    """
    Creates a Plotly figure based on the selected plot type and columns.
    
    Parameters:
        df (pd.DataFrame): The DataFrame to plot.
        plot_type (str): Type of plot ("Scatter", "Bar", "Line").
        x (str): Column name for the x-axis.
        y (str): Column name for the y-axis.
    
    Returns:
        fig (plotly.graph_objs._figure.Figure): The generated plot.
    """
    if plot_type == "Scatter":
        fig = px.scatter(df, x=x, y=y, title=f"Scatter Plot: {x} vs {y}")
    elif plot_type == "Bar":
        fig = px.bar(df, x=x, y=y, title=f"Bar Chart: {x} vs {y}")
    elif plot_type == "Line":
        fig = px.line(df, x=x, y=y, title=f"Line Chart: {x} vs {y}")
    else:
        fig = None
    return fig
