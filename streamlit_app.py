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







# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# from datetime import datetime, timedelta
# import requests

# # Set page config
# st.set_page_config(page_title="Invoice Analytics Dashboard", layout="wide")

# # Custom CSS for a more professional look
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
#     h1, h2, h3 {
#         color: #1f2937;
#     }
#     .stPlotlyChart {
#         background: #ffffff;
#         border-radius: 5px;
#         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
#         padding: 1rem;
#         margin-bottom: 1rem;
#     }
#     .stMetric {
#         background: #f3f4f6;
#         padding: 1rem;
#         border-radius: 5px;
#         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
#     }
# </style>
# """, unsafe_allow_html=True)

# # Function to convert color to RGBA
# def color_to_rgba(color, alpha=0.2):
#     if color.startswith("#"):
#         r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
#     else:
#         # Assume it's an RGB string like "rgb(255, 0, 0)"
#         r, g, b = map(int, color.strip("rgb()").split(","))
#     return f"rgba({r}, {g}, {b}, {alpha})"

# # Title and description
# st.title("Invoice Analytics Dashboard")
# st.markdown("Analyze invoice data trends and patterns over time.")

# # Date selection
# col1, col2 = st.columns(2)
# with col1:
#     start_date = st.date_input("Start Date", datetime.now() - timedelta(days=180))
# with col2:
#     end_date = st.date_input("End Date", datetime.now())

# # Fetch data from API
# @st.cache_data(ttl=3600)
# def fetch_invoice_data(start_date, end_date):
#     url = "https://staging.api.crp22.yhh.ae/items/invoices"
#     params = {
#         "limit": 3000,
#         "filter[date_created][_between]": f"{start_date},{end_date}"
#     }
#     headers = {
#         "Authorization": "Bearer r3XYt4SgbI61JWUraxtD3aTzMcy4nc9X"    
#     }
#     response = requests.get(url, params=params, headers=headers)
#     if response.status_code == 200:
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
#         # Color scheme
#         color_scheme = px.colors.qualitative.Safe

#         # Summary statistics
#         st.header("Summary Statistics")
#         total_invoices = len(df_filtered)
#         total_amount = df_filtered['Amount_In_USD'].sum()
#         avg_amount = df_filtered['Amount_In_USD'].mean()

#         col1, col2, col3 = st.columns(3)
#         col1.metric("Total Invoices", f"{total_invoices:,}")
#         col2.metric("Total Amount (USD)", f"${total_amount:,.2f}")
#         col3.metric("Average Amount (USD)", f"${avg_amount:.2f}")

#         # Line chart with area and moving average
#         st.header("Daily Invoice Trends")
#         daily_totals = df_filtered.groupby(df_filtered['date_created'].dt.date)['Amount_In_USD'].agg(['sum', 'count']).reset_index()
#         daily_totals['moving_avg'] = daily_totals['sum'].rolling(window=7).mean()

#         fig_line = go.Figure()
#         fig_line.add_trace(go.Scatter(x=daily_totals['date_created'], y=daily_totals['sum'],
#                                       fill='tozeroy', fillcolor=color_to_rgba(color_scheme[0]),
#                                       line=dict(color=color_scheme[0]), name='Daily Total'))
#         fig_line.add_trace(go.Scatter(x=daily_totals['date_created'], y=daily_totals['moving_avg'],
#                                       line=dict(color=color_scheme[1], dash='dash'), name='7-day Moving Average'))
#         fig_line.update_layout(title='Daily Invoice Totals and 7-day Moving Average',
#                                xaxis_title='Date', yaxis_title='Amount (USD)',
#                                legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))
#         st.plotly_chart(fig_line, use_container_width=True)

#         # Bar chart with line overlay
#         st.header("Weekly Invoice Analysis")
#         weekly_totals = df_filtered.resample('W', on='date_created')['Amount_In_USD'].agg(['sum', 'count']).reset_index()
#         fig_bar = go.Figure()
#         fig_bar.add_trace(go.Bar(x=weekly_totals['date_created'], y=weekly_totals['sum'],
#                                  marker_color=color_scheme[2], name='Weekly Total'))
#         fig_bar.add_trace(go.Scatter(x=weekly_totals['date_created'], y=weekly_totals['count'],
#                                      line=dict(color=color_scheme[3]), name='Invoice Count', yaxis='y2'))
#         fig_bar.update_layout(title='Weekly Invoice Totals and Count',
#                               xaxis_title='Week', yaxis_title='Amount (USD)',
#                               yaxis2=dict(title='Invoice Count', overlaying='y', side='right'),
#                               legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))
#         st.plotly_chart(fig_bar, use_container_width=True)

#         # Scatter plot with size and color (handling NaN values)
#         st.header("Invoice Distribution")
#         df_scatter = df_filtered.dropna(subset=['Amount_In_USD'])
#         fig_scatter = px.scatter(df_scatter, x='date_created', y='Amount_In_USD',
#                                  color='status', size='Amount_In_USD',
#                                  hover_data=['currency', 'buyer_email'],
#                                  title='Invoice Distribution by Amount and Status',
#                                  color_discrete_sequence=color_scheme)
#         fig_scatter.update_layout(xaxis_title='Date', yaxis_title='Amount (USD)',
#                                   legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))
#         st.plotly_chart(fig_scatter, use_container_width=True)

#         # Status distribution pie chart
#         st.header("Invoice Status Distribution")
#         status_counts = df_filtered['status'].value_counts()
#         fig_pie = px.pie(values=status_counts.values, names=status_counts.index,
#                          title='Invoice Status Distribution',
#                          color_discrete_sequence=color_scheme)
#         fig_pie.update_traces(textposition='inside', textinfo='percent+label')
#         st.plotly_chart(fig_pie, use_container_width=True)

#         # Top buyers
#         st.header("Top Buyers")
#         top_buyers = df_filtered.groupby('buyer_email')['Amount_In_USD'].sum().sort_values(ascending=False).head(10)
#         fig_top_buyers = px.bar(top_buyers, x=top_buyers.index, y=top_buyers.values,
#                                 title='Top 10 Buyers by Total Amount',
#                                 labels={'x': 'Buyer Email', 'y': 'Total Amount (USD)'},
#                                 color_discrete_sequence=[color_scheme[4]])
#         fig_top_buyers.update_layout(xaxis_title='Buyer Email', xaxis_tickangle=-45)
#         st.plotly_chart(fig_top_buyers, use_container_width=True)

#         # Data table with formatting
#         st.header("Invoice Data Table")
#         st.dataframe(df_filtered[['date_created', 'Amount_In_USD', 'status', 'currency', 'buyer_email']]
#                      .sort_values('date_created', ascending=False)
#                      .style.format({'Amount_In_USD': '${:.2f}', 'date_created': '{:%Y-%m-%d %H:%M}'}),
#                      height=400)

# else:
#     st.warning("No data available for the selected date range.")









# import streamlit as st
# import speech_recognition as sr
# from gtts import gTTS
# import os
# import base64
# import tempfile
# from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
# import av
# import queue
# import pydub
# import numpy as np

# # Initialize session state
# if 'conversation' not in st.session_state:
#     st.session_state.conversation = []
# if 'audio_buffer' not in st.session_state:
#     st.session_state.audio_buffer = []

# def text_to_speech(text, lang='en'):
#     tts = gTTS(text=text, lang=lang, slow=False)
#     fp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
#     tts.save(fp.name)
#     return fp.name

# def get_audio_player(file_path):
#     with open(file_path, "rb") as f:
#         data = f.read()
#         b64 = base64.b64encode(data).decode()
#         return f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}" controls></audio>'

# def process_audio(audio_data):
#     recognizer = sr.Recognizer()
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_wav_file:
#         pydub.AudioSegment(
#             data=audio_data,
#             sample_width=2,
#             frame_rate=48000,
#             channels=1
#         ).export(tmp_wav_file.name, format="wav")
        
#         with sr.AudioFile(tmp_wav_file.name) as source:
#             audio = recognizer.record(source)
#             text = recognizer.recognize_google(audio)
        
#         os.unlink(tmp_wav_file.name)
#     return text

# def simulate_ai_response(user_input, model):
#     return f"As an AI using the {model} model, I understood your input: '{user_input}'. How can I assist you further?"

# st.title("Voice Chatbot (Multi-Model)")

# model = st.sidebar.radio(
#     "Choose a Model:",
#     ("OpenAI GPT-4", "Claude Sonnet 3.5", "Llama 3.1 70b", "Gemini Pro 1.5")
# )

# class AudioProcessor:
#     def __init__(self):
#         self.audio_buffer = []

#     def recv(self, frame):
#         sound = pydub.AudioSegment(
#             data=frame.to_ndarray().tobytes(),
#             sample_width=frame.format.bytes,
#             frame_rate=frame.sample_rate,
#             channels=len(frame.layout.channels)
#         )
#         sound = sound.set_channels(1).set_frame_rate(16000)
#         self.audio_buffer.append(sound.raw_data)
#         return frame

# webrtc_ctx = webrtc_streamer(
#     key="speech-to-text",
#     mode=WebRtcMode.SENDONLY,
#     rtc_configuration=RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}),
#     media_stream_constraints={"video": False, "audio": True},
#     video_processor_factory=None,
#     audio_processor_factory=AudioProcessor,
# )

# if st.button("Process Recording"):
#     if webrtc_ctx.audio_processor:
#         try:
#             audio_data = b"".join(webrtc_ctx.audio_processor.audio_buffer)
#             user_input = process_audio(audio_data)

#             st.session_state.conversation.append(("You", user_input))

#             ai_response = simulate_ai_response(user_input, model)
#             st.session_state.conversation.append(("AI", ai_response))

#             audio_file = text_to_speech(ai_response)
#             st.markdown(get_audio_player(audio_file), unsafe_allow_html=True)
#             os.unlink(audio_file)

#             # Clear the audio buffer
#             webrtc_ctx.audio_processor.audio_buffer = []
#         except Exception as e:
#             st.error(f"An error occurred: {str(e)}")
#     else:
#         st.warning("No audio recorded. Please record some audio before processing.")

# st.markdown("## Conversation History")
# for speaker, message in st.session_state.conversation:
#     st.markdown(f"**{speaker}:** {message}")

# st.markdown("---")
# st.markdown("Click the 'Start' button to begin recording, then 'Stop' when finished. Press 'Process Recording' to analyze the audio and get a response.")







# import streamlit as st
# from openai import OpenAI
# import speech_recognition as sr
# from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
# import numpy as np
# import queue
# import tempfile
# import os
# import pydub
# import requests
# from openai import RateLimitError, APIError

# # Set up OpenAI client
# client = OpenAI(api_key="",
#                 organization='org-obHOmTCwtebsLu30UYdbB9RV',
#                 project='proj_u3IQfTzhXdtThzBYchibz1jv')

# def fetchResponsesData(message):
#     headers = {
#         "Authorization": "Bearer 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",
#         "OpenAI-Organization": "org-obHOmTCwtebsLu30UYdbB9RV",
#         "OpenAI-Project": "proj_u3IQfTzhXdtThzBYchibz1jv"
#     }
#     data = {
#         "model": "gpt-4o-mini",
#         "messages": [{"role": "user", "content": message}],
#         "temperature": 0.7
#     }
#     response = requests.get("https://api.openai.com/v1/chat/completions", headers=headers, data=data)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         st.error(f"Failed to fetch data: {response.status_code}")
#         return None


# def transcribe_audio(audio_file):
#     r = sr.Recognizer()
#     with sr.AudioFile(audio_file) as source:
#         audio = r.record(source)
#     try:
#         return r.recognize_google(audio)
#     except sr.UnknownValueError:
#         return "Speech recognition could not understand the audio"
#     except sr.RequestError:
#         return "Could not request results from the speech recognition service"

# def get_ai_response(prompt):
#     try:
#         response = fetchResponsesData(prompt)
#         return response.choices[0].message.content
#     except RateLimitError:
#         return "I apologize, but I'm currently unavailable due to high demand. Please try again later."
#     except APIError:
#         return "I'm having trouble connecting to my knowledge base. Please try again in a moment."
#     except Exception as e:
#         return f"An unexpected error occurred: {str(e)}"

# st.title("AI Chatbot with Live Voice Input")

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# input_option = st.radio("Choose input method:", ("Text", "Voice"))

# if input_option == "Text":
#     prompt = st.chat_input("Enter your message:")
#     if prompt:
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)
        
#         with st.chat_message("assistant"):
#             message_placeholder = st.empty()
#             full_response = get_ai_response(prompt)
#             message_placeholder.markdown(full_response)
#         st.session_state.messages.append({"role": "assistant", "content": full_response})

# else:
#     webrtc_ctx = webrtc_streamer(
#         key="speech-to-text",
#         mode=WebRtcMode.SENDRECV,
#         audio_receiver_size=1024,
#         rtc_configuration=RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}),
#         media_stream_constraints={"video": False, "audio": True},
#     )

#     if webrtc_ctx.audio_receiver:
#         sound_chunk = pydub.AudioSegment.empty()
#         audio_frames = []

#         while True:
#             try:
#                 audio_frames.append(webrtc_ctx.audio_receiver.get_frame())
#             except queue.Empty:
#                 break

#         if len(audio_frames) > 0:
#             sound_chunk = pydub.AudioSegment(
#                 data=b''.join([frame.to_ndarray().tobytes() for frame in audio_frames]),
#                 sample_width=4,
#                 frame_rate=48000,
#                 channels=1,
#             )

#             with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
#                 sound_chunk.export(tmp_file.name, format="wav")
#                 tmp_file_path = tmp_file.name

#             transcript = transcribe_audio(tmp_file_path)
#             os.remove(tmp_file_path)

#             st.session_state.messages.append({"role": "user", "content": f"🎤 Voice Recording\n\nTranscript: {transcript}"})
#             with st.chat_message("user"):
#                 st.markdown(f"🎤 Voice Recording\n\nTranscript: {transcript}")
            
#             with st.chat_message("assistant"):
#                 message_placeholder = st.empty()
#                 full_response = get_ai_response(transcript)
#                 message_placeholder.markdown(full_response)
#             st.session_state.messages.append({"role": "assistant", "content": full_response})

# st.button("Clear Chat History", on_click=lambda: st.session_state.clear())



import streamlit as st
import pandas as pd
from datetime import timedelta, datetime

# Set page config
st.set_page_config(page_title="Arabee Dashboard CRP22", layout="wide")

# Helper functions
@st.cache_data
def load_data():
    data = pd.read_csv("youtube_channel_data.csv")
    data['DATE'] = pd.to_datetime(data['DATE'])
    data['NET_SUBSCRIBERS'] = data['SUBSCRIBERS_GAINED'] - data['SUBSCRIBERS_LOST']
    return data

def custom_quarter(date):
    month = date.month
    year = date.year
    if month in [2, 3, 4]:
        return pd.Period(year=year, quarter=1, freq='Q')
    elif month in [5, 6, 7]:
        return pd.Period(year=year, quarter=2, freq='Q')
    elif month in [8, 9, 10]:
        return pd.Period(year=year, quarter=3, freq='Q')
    else:  # month in [11, 12, 1]
        return pd.Period(year=year if month != 1 else year-1, quarter=4, freq='Q')

def aggregate_data(df, freq):
    if freq == 'Q':
        df = df.copy()
        df['CUSTOM_Q'] = df['DATE'].apply(custom_quarter)
        df_agg = df.groupby('CUSTOM_Q').agg({
            'VIEWS': 'sum',
            'WATCH_HOURS': 'sum',
            'NET_SUBSCRIBERS': 'sum',
            'LIKES': 'sum',
            'COMMENTS': 'sum',
            'SHARES': 'sum',
        })
        return df_agg
    else:
        return df.resample(freq, on='DATE').agg({
            'VIEWS': 'sum',
            'WATCH_HOURS': 'sum',
            'NET_SUBSCRIBERS': 'sum',
            'LIKES': 'sum',
            'COMMENTS': 'sum',
            'SHARES': 'sum',
        })

def get_weekly_data(df):
    return aggregate_data(df, 'W-MON')

def get_monthly_data(df):
    return aggregate_data(df, 'M')

def get_quarterly_data(df):
    return aggregate_data(df, 'Q')

def format_with_commas(number):
    return f"{number:,}"

def create_metric_chart(df, column, color, chart_type, height=150, time_frame='Daily'):
    chart_data = df[[column]].copy()
    if time_frame == 'Quarterly':
        chart_data.index = chart_data.index.strftime('%Y Q%q ')
    if chart_type=='Bar':
        st.bar_chart(chart_data, y=column, color=color, height=height)
    if chart_type=='Area':
        st.area_chart(chart_data, y=column, color=color, height=height)

def is_period_complete(date, freq):
    today = datetime.now()
    if freq == 'D':
        return date.date() < today.date()
    elif freq == 'W':
        return date + timedelta(days=6) < today
    elif freq == 'M':
        next_month = date.replace(day=28) + timedelta(days=4)
        return next_month.replace(day=1) <= today
    elif freq == 'Q':
        current_quarter = custom_quarter(today)
        return date < current_quarter

def calculate_delta(df, column):
    if len(df) < 2:
        return 0, 0
    current_value = df[column].iloc[-1]
    previous_value = df[column].iloc[-2]
    delta = current_value - previous_value
    delta_percent = (delta / previous_value) * 100 if previous_value != 0 else 0
    return delta, delta_percent

def display_metric(col, title, value, df, column, color, time_frame):
    with col:
        with st.container(border=True):
            delta, delta_percent = calculate_delta(df, column)
            delta_str = f"{delta:+,.0f} ({delta_percent:+.2f}%)"
            st.metric(title, format_with_commas(value), delta=delta_str)
            create_metric_chart(df, column, color, time_frame=time_frame, chart_type=chart_selection)
            
            last_period = df.index[-1]
            freq = {'Daily': 'D', 'Weekly': 'W', 'Monthly': 'M', 'Quarterly': 'Q'}[time_frame]
            if not is_period_complete(last_period, freq):
                st.caption(f"Note: The last {time_frame.lower()[:-2] if time_frame != 'Daily' else 'day'} is incomplete.")

# Load data
df = load_data()

# Set up input widgets
st.logo(image="images/streamlit-logo-primary-colormark-lighttext.png", 
        icon_image="images/streamlit-mark-color.png")

with st.sidebar:
    st.title("Arabee Dashboard CRP22")
    st.header("⚙️ Settings")
    
    max_date = df['DATE'].max().date()
    default_start_date = max_date - timedelta(days=365)  # Show a year by default
    default_end_date = max_date
    start_date = st.date_input("Start date", default_start_date, min_value=df['DATE'].min().date(), max_value=max_date)
    end_date = st.date_input("End date", default_end_date, min_value=df['DATE'].min().date(), max_value=max_date)
    time_frame = st.selectbox("Select time frame",
                              ("Daily", "Weekly", "Monthly", "Quarterly"),
    )
    chart_selection = st.selectbox("Select a chart type",
                                   ("Bar", "Area"))

# Prepare data based on selected time frame
if time_frame == 'Daily':
    df_display = df.set_index('DATE')
elif time_frame == 'Weekly':
    df_display = get_weekly_data(df)
elif time_frame == 'Monthly':
    df_display = get_monthly_data(df)
elif time_frame == 'Quarterly':
    df_display = get_quarterly_data(df)

# Display Key Metrics
st.subheader("All-Time Statistics")

metrics = [
    ("Total Subscribers", "NET_SUBSCRIBERS", '#29b5e8'),
    ("Total Views", "VIEWS", '#FF9F36'),
    ("Total Watch Hours", "WATCH_HOURS", '#D45B90'),
    ("Total Likes", "LIKES", '#7D44CF')
]

cols = st.columns(4)
for col, (title, column, color) in zip(cols, metrics):
    total_value = df[column].sum()
    display_metric(col, title, total_value, df_display, column, color, time_frame)

st.subheader("Selected Duration")

if time_frame == 'Quarterly':
    start_quarter = custom_quarter(start_date)
    end_quarter = custom_quarter(end_date)
    mask = (df_display.index >= start_quarter) & (df_display.index <= end_quarter)
else:
    mask = (df_display.index >= pd.Timestamp(start_date)) & (df_display.index <= pd.Timestamp(end_date))
df_filtered = df_display.loc[mask]

cols = st.columns(4)
for col, (title, column, color) in zip(cols, metrics):
    display_metric(col, title.split()[-1], df_filtered[column].sum(), df_filtered, column, color, time_frame)

# DataFrame display
with st.expander('See DataFrame (Selected time frame)'):
    st.dataframe(df_filtered)
