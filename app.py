import dash
from dash import html, dcc
import plotly.express as px
from sqlalchemy import create_engine
import pandas as pd
from models import Patient

# Initialize the Dash app
app = dash.Dash(__name__)

# Create database connection
engine = create_engine('sqlite:///patients.db')

# Get data from database
query = "SELECT * FROM patients"
df = pd.read_sql(query, engine)

# Print available columns to debug
print("Available columns:", df.columns.tolist())

# Create visualizations with available columns
age_histogram = px.histogram(df, x='age', title='Age Distribution')
waiting_scatter = px.scatter(df, x='age', y='waiting_time', 
                           title='Age vs Waiting Time')

# Define the layout
app.layout = html.Div([
    html.H1('Heart Transplant Dashboard'),
    
    html.Div([
        html.H2('Patient Statistics'),
        html.P(f'Total Patients: {len(df)}'),
        html.P(f'Average Age: {df["age"].mean():.1f}'),
        html.P(f'Average Waiting Time (days): {df["waiting_time"].mean():.1f}')
    ]),
    
    html.Div([
        dcc.Graph(figure=age_histogram),
        dcc.Graph(figure=waiting_scatter)
    ])
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)