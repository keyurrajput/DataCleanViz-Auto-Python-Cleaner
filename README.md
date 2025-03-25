# DataCleanViz

**Automated dataset cleaning and visualization with intuitive interface**

## Overview
DataCleanViz is a powerful web application built with Streamlit that simplifies the data cleaning and visualization process. This tool enables users to upload CSV datasets, perform essential cleaning operations, and generate interactive visualizations without writing a single line of code. Designed for data analysts, researchers, and business professionals, DataCleanViz streamlines the initial exploratory data analysis (EDA) phase of the data science workflow.

## Features

### Data Cleaning Capabilities
- **Duplicate Row Removal**: Instantly identify and remove duplicate entries from your dataset
- **Missing Value Handling**: Choose between removing rows with missing values or filling numeric fields with column means
- **Data Type Inspection**: Examine the data types of selected columns to better understand your dataset
- **One-Click Download**: Export your cleaned dataset with a simple button click

### Interactive Visualization
- **Multiple Plot Types**: Create scatter plots, bar charts, and line graphs
- **Dynamic Configuration**: Easily select columns for x and y axes
- **Plot Management**: Add multiple plots and clear them as needed
- **Responsive Design**: Visualizations adapt to your screen size for optimal viewing

## How It Works
The application consists of two main components:

1. **app.py**: The Streamlit interface that handles user interactions, file uploads, and displaying results
2. **autocleaner.py**: A utility module containing functions for data cleaning and visualization

The workflow is straightforward:
1. Upload your CSV file through the sidebar
2. Preview your data in a tabular format
3. Select and apply cleaning operations as needed
4. Inspect column data types
5. Create visualizations by selecting plot types and columns
6. Download your cleaned dataset

## Technical Implementation
DataCleanViz leverages several powerful Python libraries:
- **Streamlit**: Provides the web application framework and interactive widgets
- **Pandas**: Handles data manipulation and processing
- **NumPy**: Supports numerical operations
- **Plotly Express**: Creates interactive, publication-quality visualizations

The application employs a modular design with separate functions for different cleaning operations, making the codebase maintainable and extensible. Custom CSS styling enhances the user interface for a more professional appearance.

## Use Cases
- **Data Scientists**: Quickly clean datasets before implementing machine learning models
- **Business Analysts**: Generate visualizations for presentations and reports
- **Researchers**: Prepare data for statistical analysis
- **Students**: Learn data cleaning concepts with hands-on experience
- **Small Teams**: Share a common tool for consistent data preprocessing

## Future Enhancements
- Advanced data type conversion tools
- Outlier detection and handling
- More visualization options (histograms, box plots, heatmaps)
- Custom color schemes for plots
- Data profiling reports
- Export visualizations as static images

## Getting Started
To run DataCleanViz locally:

```bash
# Install requirements
pip install streamlit pandas numpy plotly

# Run the application
streamlit run app.py
```

DataCleanViz demonstrates how powerful data tools can be made accessible through thoughtful interface design, enabling users of all technical backgrounds to explore and clean their datasets with confidence.
