# import streamlit as st
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# import toml
# import json

# # Load the secrets from the .secrets.toml file
# secrets = toml.load('.streamlit/secrets.toml')

# # Extract Google API credentials
# google_api_credentials = json.loads(secrets['google_api']['credentials'])
# print("");
# # Define scope for Google Sheets API
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# # Authenticate with Google API credentials
# credentials = ServiceAccountCredentials.from_json_keyfile_dict(google_api_credentials, scope)
# client = gspread.authorize(credentials)

# # Open a Google Sheet by name or URL
# sheet = client.open("StreamLit Form").sheet1

# # Get data from a specific range or all values
# existing_data = sheet.get_all_records()

# def submit_record(data):
#     sheet.append_row(data)

# # Display data in Streamlit
# st.dataframe(existing_data)

# # List of Business Types and Products
# BUSINESS_TYPES = [
#     "Manufacturer",
#     "Distributor",
#     "Wholesaler",
#     "Retailer",
#     "Service Provider",
# ]
# PRODUCTS = [
#     "Electronics",
#     "Apparel",
#     "Groceries",
#     "Software",
#     "Other",
# ]

# # Onboarding New Vendor Form
# with st.form(key="vendor_form"):
#     company_name = st.text_input(label="Company Name*")
#     business_type = st.selectbox("Business Type*", options=BUSINESS_TYPES, index=None)
#     products = st.multiselect("Products Offered", options=PRODUCTS)
#     years_in_business = st.slider("Years in Business", 0, 50, 5)
#     onboarding_date = st.date_input(label="Onboarding Date")
#     additional_info = st.text_area(label="Additional Notes")

#     # Mark mandatory fields
#     st.markdown("**required*")

#     submit_button = st.form_submit_button(label="Submit Vendor Details")

#     # If the submit button is pressed
#     if submit_button:
#         submit_record([company_name, business_type, ", ".join(products), years_in_business, onboarding_date.strftime("%Y-%m-%d"), additional_info])
#         existing_data = sheet.get_all_records()
#         st.dataframe(existing_data)
#         st.success("Vendor details successfully submitted!")






#############


# import streamlit as st
# import requests
# import pandas as pd

# def fetch_random_user():
#     response = requests.get('https://randomuser.me/api/')
#     return response.json()['results'][0]

# def main():
#     st.title('Random User Generator')
#     st.write('Click the button below to fetch a random user from the API.')

#     if st.button('Fetch Random User'):
#         user = fetch_random_user()
        
#         st.subheader('User Information')
#         st.image(user['picture']['large'], width=150)
#         st.write(f"Name: {user['name']['first']} {user['name']['last']}")
#         st.write(f"Email: {user['email']}")
#         st.write(f"Phone: {user['phone']}")
#         st.write(f"Location: {user['location']['city']}, {user['location']['country']}")

#         # Display user details in a DataFrame
#         user_df = pd.DataFrame({
#             'Field': ['Gender', 'Age', 'Username', 'Registered Date'],
#             'Value': [
#                 user['gender'],
#                 user['dob']['age'],
#                 user['login']['username'],
#                 user['registered']['date']
#             ]
#         })
#         st.dataframe(user_df)

# if __name__ == '__main__':
#     main()
    

###########

# import streamlit as st
# import requests
# import pandas as pd
# import plotly.express as px

# API_URL = "https://staging.api.crp22.yhh.ae/items/invoices?limit=1000"
# API_TOKEN = "r3XYt4SgbI61JWUraxtD3aTzMcy4nc9X"

# def fetch_invoice_data():
#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }
#     response = requests.get(API_URL, headers=headers)
#     if response.status_code == 200:
#         return response.json()['data']
#     else:
#         st.error(f"Failed to fetch data: {response.status_code}")
#         return None

# def main():
#     st.title('Invoice Data Visualization')
#     st.write('Fetching and visualizing invoice data from the API.')

#     data = fetch_invoice_data()
    
#     if data:
#         df = pd.DataFrame(data)
        
#         st.subheader('Invoice Data Overview')
#         st.dataframe(df.head())
#     # Convert date strings to datetime
#     df['date_created'] = pd.to_datetime(df['date_created'])

#     # Display basic statistics
#     st.subheader('Basic Statistics')
#     st.write(f"Total Invoices: {len(df)}")
#     st.write(f"Total Revenue (USD): ${df['Amount_In_USD'].sum():.2f}")
#     st.write(f"Average Invoice Amount (USD): ${df['Amount_In_USD'].mean():.2f}")

#     # Chart 1: Invoice Amounts Over Time
#     st.subheader('Invoice Amounts Over Time')
#     fig1 = px.scatter(df, x='date_created', y='Amount_In_USD', 
#                       hover_data=['currency', 'amount', 'buyer_email'],
#                       title='Invoice Amounts Over Time')
#     st.plotly_chart(fig1)

#     # Chart 2: Distribution of Invoice Amounts
#     st.subheader('Distribution of Invoice Amounts')
#     fig2 = px.histogram(df, x='Amount_In_USD', nbins=20,
#                         title='Distribution of Invoice Amounts (USD)')
#     st.plotly_chart(fig2)

#     # Chart 3: Invoice Status Distribution
#     st.subheader('Invoice Status Distribution')
#     status_counts = df['status'].value_counts()
#     fig3 = px.pie(values=status_counts.values, names=status_counts.index, 
#                   title='Invoice Status Distribution')
#     st.plotly_chart(fig3)

#     # Chart 4: Top 10 Countries by Invoice Count
#     st.subheader('Top 10 Countries by Invoice Count')
#     country_counts = df['country_code'].value_counts().head(10)
#     fig4 = px.bar(x=country_counts.index, y=country_counts.values,
#                   title='Top 10 Countries by Invoice Count')
#     fig4.update_xaxes(title='Country Code')
#     fig4.update_yaxes(title='Number of Invoices')
#     st.plotly_chart(fig4)

#     # Chart 5: Revenue by Product Plan
#     st.subheader('Revenue by Product Plan')
#     plan_revenue = df.groupby('product_plan_id')['Amount_In_USD'].sum().sort_values(ascending=False)
#     fig5 = px.bar(x=plan_revenue.index, y=plan_revenue.values,
#                   title='Revenue by Product Plan ID')
#     fig5.update_xaxes(title='Product Plan ID')
#     fig5.update_yaxes(title='Total Revenue (USD)')
#     st.plotly_chart(fig5)

# if __name__ == '__main__':
#     main()


#########


# import streamlit as st
# import pandas as pd
# import plotly.express as px
# from datetime import datetime, timedelta
# import numpy as np

# def main():
#     # Set page config
#     st.set_page_config(page_title="Date Selection and Charts", layout="wide")

#     # Add custom CSS
#     st.markdown("""
#     <style>
#         .reportview-container {
#             background: #f0f2f6;
#         }
#         .main {
#             background: #ffffff;
#             padding: 2rem;
#             border-radius: 10px;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#         }
#         h1 {
#             color: #1f2937;
#         }
#     </style>
#     """, unsafe_allow_html=True)

#     # Title
#     st.title("Date Selection and Charts")

#     # Date selection
#     col1, col2 = st.columns(2)
#     with col1:
#         start_date = st.date_input("Start Date", datetime.now() - timedelta(days=30))
#     with col2:
#         end_date = st.date_input("End Date", datetime.now())

#     # Generate sample data
#     date_range = pd.date_range(start=start_date, end=end_date)
#     data = pd.DataFrame({
#         'Date': date_range,
#         'Value': np.random.randn(len(date_range)).cumsum()
#     })

#     # Line chart
#     st.subheader("Line Chart")
#     fig_line = px.line(data, x='Date', y='Value', title='Time Series Data')
#     st.plotly_chart(fig_line, use_container_width=True)

#     # Bar chart
#     st.subheader("Bar Chart")
#     weekly_data = data.resample('W', on='Date').mean().reset_index()
#     fig_bar = px.bar(weekly_data, x='Date', y='Value', title='Weekly Average')
#     st.plotly_chart(fig_bar, use_container_width=True)

#     # Scatter plot
#     st.subheader("Scatter Plot")
#     fig_scatter = px.scatter(data, x='Date', y='Value', title='Data Points')
#     st.plotly_chart(fig_scatter, use_container_width=True)

#     # Data table
#     st.subheader("Data Table")
#     st.dataframe(data)

# if __name__ == '__main__':
#     main()


#########


# import streamlit as st
# import pandas as pd
# import plotly.express as px
# from datetime import datetime, timedelta
# import requests

# # Set page config
# st.set_page_config(page_title="Invoice Data Charts", layout="wide")

# # Add custom CSS
# st.markdown("""
# <style>
#     .reportview-container {
#         background: #f0f2f6;
#     }
#     .main {
#         background: #ffffff;
#         padding: 2rem;
#         border-radius: 10px;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#     }
#     h1 {
#         color: #1f2937;
#     }
# </style>
# """, unsafe_allow_html=True)

# # Title
# st.title("Invoice Data Charts")

# # Date selection
# col1, col2 = st.columns(2)
# with col1:
#     start_date = st.date_input("Start Date", datetime.now() - timedelta(days=45))
# with col2:
#     end_date = st.date_input("End Date", datetime.now())

# # Fetch data from API
# @st.cache_data(ttl=3600)
# def fetch_invoice_data(start_date, end_date):
#     url = "https://staging.api.crp22.yhh.ae/items/invoices"
#     headers = {
#         "Authorization": "Bearer r3XYt4SgbI61JWUraxtD3aTzMcy4nc9X"    
#     }
#     params = {
#         "limit": 3000,
#         "filter[date_created][_between]": f"{start_date},{end_date}",
#     }
#     response = requests.get(url, params=params, headers=headers)
#     if response.status_code == 200:
#         print(response.json()['data'])
#         return response.json()['data']
#     else:
#         st.error(f"Failed to fetch data: {response.status_code}")
#         return None

# data = fetch_invoice_data(start_date, end_date)

# if data:
#     # Convert to DataFrame
#     df = pd.DataFrame(data)
#     df['date_created'] = pd.to_datetime(df['date_created'])
#     df['Amount_In_USD'] = pd.to_numeric(df['Amount_In_USD'], errors='coerce')

#     # Filter data based on selected date range
#     mask = (df['date_created'].dt.date >= start_date) & (df['date_created'].dt.date <= end_date)
#     df_filtered = df.loc[mask]

#     if df_filtered.empty:
#         st.warning("No data available for the selected date range.")
#     else:
#         # Line chart
#         st.subheader("Daily Invoice Totals (USD)")
#         daily_totals = df_filtered.groupby(df_filtered['date_created'].dt.date)['Amount_In_USD'].sum().reset_index()
#         fig_line = px.line(daily_totals, x='date_created', y='Amount_In_USD', title='Daily Invoice Totals (USD)')
#         st.plotly_chart(fig_line, use_container_width=True)

#         # Bar chart
#         st.subheader("Weekly Invoice Totals (USD)")
#         weekly_totals = df_filtered.resample('W', on='date_created')['Amount_In_USD'].sum().reset_index()
#         fig_bar = px.bar(weekly_totals, x='date_created', y='Amount_In_USD', title='Weekly Invoice Totals (USD)')
#         st.plotly_chart(fig_bar, use_container_width=True)

#         # Scatter plot
#         st.subheader("Individual Invoice Amounts (USD)")
#         fig_scatter = px.scatter(df_filtered, x='date_created', y='Amount_In_USD', title='Individual Invoice Amounts (USD)')
#         st.plotly_chart(fig_scatter, use_container_width=True)

#         # Data table
#         st.subheader("Invoice Data Table")
#         st.dataframe(df_filtered[['buyer_email', 'date_created', 'Amount_In_USD', 'status', 'currency']])

#         # Summary statistics
#         st.subheader("Summary Statistics")
#         total_invoices = len(df_filtered)
#         total_amount = df_filtered['Amount_In_USD'].sum()
#         avg_amount = df_filtered['Amount_In_USD'].mean()

#         col1, col2, col3 = st.columns(3)
#         col1.metric("Total Invoices", f"{total_invoices:,}")
#         col2.metric("Total Amount (USD)", f"${total_amount:,.2f}")
#         col3.metric("Average Amount (USD)", f"${avg_amount:.2f}")

# else:
#     st.warning("No data available for the selected date range.")


#### 


import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import requests

# Set page config
st.set_page_config(page_title="Invoice Analytics Dashboard", layout="wide")

# Custom CSS for a more professional look
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6;
    }
    .main {
        background: #ffffff;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    h1, h2, h3 {
        color: #1f2937;
    }
    .stPlotlyChart {
        background: #ffffff;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .stMetric {
        background: #f3f4f6;
        padding: 1rem;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
</style>
""", unsafe_allow_html=True)

# Function to convert color to RGBA
def color_to_rgba(color, alpha=0.2):
    if color.startswith("#"):
        r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
    else:
        # Assume it's an RGB string like "rgb(255, 0, 0)"
        r, g, b = map(int, color.strip("rgb()").split(","))
    return f"rgba({r}, {g}, {b}, {alpha})"

# Title and description
st.title("Invoice Analytics Dashboard")
st.markdown("Analyze invoice data trends and patterns over time.")

# Date selection
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date", datetime.now() - timedelta(days=180))
with col2:
    end_date = st.date_input("End Date", datetime.now())

# Fetch data from API
@st.cache_data(ttl=3600)
def fetch_invoice_data(start_date, end_date):
    url = "https://staging.api.crp22.yhh.ae/items/invoices"
    params = {
        "limit": 3000,
        "filter[date_created][_between]": f"{start_date},{end_date}"
    }
    headers = {
        "Authorization": "Bearer r3XYt4SgbI61JWUraxtD3aTzMcy4nc9X"    
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()['data']
    else:
        st.error(f"Failed to fetch data: {response.status_code}")
        return None

data = fetch_invoice_data(start_date, end_date)

if data:
    # Convert to DataFrame
    df = pd.DataFrame(data)
    df['date_created'] = pd.to_datetime(df['date_created'])
    df['Amount_In_USD'] = pd.to_numeric(df['Amount_In_USD'], errors='coerce')

    # Filter data based on selected date range
    mask = (df['date_created'].dt.date >= start_date) & (df['date_created'].dt.date <= end_date)
    df_filtered = df.loc[mask]

    if df_filtered.empty:
        st.warning("No data available for the selected date range.")
    else:
        # Color scheme
        color_scheme = px.colors.qualitative.Safe

        # Summary statistics
        st.header("Summary Statistics")
        total_invoices = len(df_filtered)
        total_amount = df_filtered['Amount_In_USD'].sum()
        avg_amount = df_filtered['Amount_In_USD'].mean()

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Invoices", f"{total_invoices:,}")
        col2.metric("Total Amount (USD)", f"${total_amount:,.2f}")
        col3.metric("Average Amount (USD)", f"${avg_amount:.2f}")

        # Line chart with area and moving average
        st.header("Daily Invoice Trends")
        daily_totals = df_filtered.groupby(df_filtered['date_created'].dt.date)['Amount_In_USD'].agg(['sum', 'count']).reset_index()
        daily_totals['moving_avg'] = daily_totals['sum'].rolling(window=7).mean()

        fig_line = go.Figure()
        fig_line.add_trace(go.Scatter(x=daily_totals['date_created'], y=daily_totals['sum'],
                                      fill='tozeroy', fillcolor=color_to_rgba(color_scheme[0]),
                                      line=dict(color=color_scheme[0]), name='Daily Total'))
        fig_line.add_trace(go.Scatter(x=daily_totals['date_created'], y=daily_totals['moving_avg'],
                                      line=dict(color=color_scheme[1], dash='dash'), name='7-day Moving Average'))
        fig_line.update_layout(title='Daily Invoice Totals and 7-day Moving Average',
                               xaxis_title='Date', yaxis_title='Amount (USD)',
                               legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))
        st.plotly_chart(fig_line, use_container_width=True)

        # Bar chart with line overlay
        st.header("Weekly Invoice Analysis")
        weekly_totals = df_filtered.resample('W', on='date_created')['Amount_In_USD'].agg(['sum', 'count']).reset_index()
        fig_bar = go.Figure()
        fig_bar.add_trace(go.Bar(x=weekly_totals['date_created'], y=weekly_totals['sum'],
                                 marker_color=color_scheme[2], name='Weekly Total'))
        fig_bar.add_trace(go.Scatter(x=weekly_totals['date_created'], y=weekly_totals['count'],
                                     line=dict(color=color_scheme[3]), name='Invoice Count', yaxis='y2'))
        fig_bar.update_layout(title='Weekly Invoice Totals and Count',
                              xaxis_title='Week', yaxis_title='Amount (USD)',
                              yaxis2=dict(title='Invoice Count', overlaying='y', side='right'),
                              legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))
        st.plotly_chart(fig_bar, use_container_width=True)

        # Scatter plot with size and color (handling NaN values)
        st.header("Invoice Distribution")
        df_scatter = df_filtered.dropna(subset=['Amount_In_USD'])
        fig_scatter = px.scatter(df_scatter, x='date_created', y='Amount_In_USD',
                                 color='status', size='Amount_In_USD',
                                 hover_data=['currency', 'buyer_email'],
                                 title='Invoice Distribution by Amount and Status',
                                 color_discrete_sequence=color_scheme)
        fig_scatter.update_layout(xaxis_title='Date', yaxis_title='Amount (USD)',
                                  legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))
        st.plotly_chart(fig_scatter, use_container_width=True)

        # Status distribution pie chart
        st.header("Invoice Status Distribution")
        status_counts = df_filtered['status'].value_counts()
        fig_pie = px.pie(values=status_counts.values, names=status_counts.index,
                         title='Invoice Status Distribution',
                         color_discrete_sequence=color_scheme)
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_pie, use_container_width=True)

        # Top buyers
        st.header("Top Buyers")
        top_buyers = df_filtered.groupby('buyer_email')['Amount_In_USD'].sum().sort_values(ascending=False).head(10)
        fig_top_buyers = px.bar(top_buyers, x=top_buyers.index, y=top_buyers.values,
                                title='Top 10 Buyers by Total Amount',
                                labels={'x': 'Buyer Email', 'y': 'Total Amount (USD)'},
                                color_discrete_sequence=[color_scheme[4]])
        fig_top_buyers.update_layout(xaxis_title='Buyer Email', xaxis_tickangle=-45)
        st.plotly_chart(fig_top_buyers, use_container_width=True)

        # Data table with formatting
        st.header("Invoice Data Table")
        st.dataframe(df_filtered[['date_created', 'Amount_In_USD', 'status', 'currency', 'buyer_email']]
                     .sort_values('date_created', ascending=False)
                     .style.format({'Amount_In_USD': '${:.2f}', 'date_created': '{:%Y-%m-%d %H:%M}'}),
                     height=400)

else:
    st.warning("No data available for the selected date range.")