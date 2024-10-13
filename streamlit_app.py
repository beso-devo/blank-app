import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Define scope for Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Authenticate with Google API credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/basel/PythonProjects/first-project/test.json', scope)
client = gspread.authorize({
  "type": "service_account",
  "project_id": "flutter-projects-16bc8",
  "private_key_id": "ed266700a8288fcb3062e06286346113d96d3a46",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDfCfy5iSHnJmi3\nDvsXBs6/3Q5fU6da2t5Yg4n0erWE6XndZcIxp4fe6JE2MLD8lKblFc5YsdOYm0hQ\nGtfqL0MMqPdDi8gMpPYb4gQmxPRmNFYi/JEElDLbgtNrhOtIgdBzlRFRFIwoiG46\nDuw9q6/tj/7ppqI+ByChwYQNA5CFfzNBPZnT57CmM7Cgr60S3yx0cSGZoN1nyTN+\np3KzWNgdHq124z5QEyaTXA4NY+Wi+0Mds04K2AVNeTj506eOGCjOg6cJAvQ4TjUC\nGpmUYhdN0A9DniLS7Yf/OdF8rs7gXfj4YCwlTiqPWp+6EG7Os+7oHU+3ab5gc62B\nFyvC6yvfAgMBAAECggEAARRpw6k9sLWDObrX1hJeKkLy9xAb4LKne/h6yChoL1qa\nQ9PI4mrrilWU9VDNB1e70YDCQU3u0DyD8SuZsoVmUX8JxhF4kOvnhNZezZMchAt7\nWatXvfszBKEpCg6trB0N1cBXl3PCer3jI8k2kypjaQsSrj8FiJUShICd7Rp4DCxS\njisnEckmuBYSw0tZP4lHqZFWMmUFwXpFPT+If3YGeDyMj9H/lwKLDO3PG0p3QNLJ\nj9m8jdLcNs1fK4kR19CX6hrG1o8ZRrUEIRPnOMwczMX44O1Hj2qbMJM9LZp1uEeZ\nOfiA74WlmucLh8UICS+VsrSCbp7ff6Fau5GqKpr28QKBgQDw62BUoTvE5Ks1o15H\nDD0YJxqqe7LzS8mrIVagghIkB3NWBEWe2NBQ455FOVLo7q3AyTBay81ZyvDTYJ4p\nKqeqUoVtPV1Sqs2YVZGU07L0j80wP/UrWwEkNXHUI/ggMTRHcJJ/MyPhGEPm0bXi\ni9phQBm9Nidx2fk/1w6N+zvoaQKBgQDtABXUY+3XEb6Ob1KTFu/B2mIc9jbzjMfR\nDOrtXM2Cpynq3V9uIZHA+Mw538L6lpOPJ/IHV9QluwbVFAonceFay18ZW0VeCb46\nsf71qdJDwWw1mDc7cF2eYjT1MI2zTi+9f06H+DQ+XvL6M0OgsD9sSTmTvqjJIjgv\nfNmLwbcpBwKBgDsYwcyAsHSf0w+ZP2sWKXZfQT9IkKD1mkaMKv+8aE7GNRiIe7t3\nW8I703sPkLLquVxs/ZuIGptIGMMBFErs16wECg692sKIe14+vzNOqrsq+x420iEM\ndb84DPAI0riy2SwdBRKGrOpuVVmtX3xu6eapHqc3PX3EBkwOqNdTJWLhAoGACSCj\ntpZSpqHMUPgAmiGcAj9C4BKrcx3M5EQ3GAUm9Q0zFBSKhFdOobvzQZdYjwYVkMHd\nFGNRjFJzpOksqvA72Z9TfkqBlWmSpfgM9bEgo/NjE31VQzjEokDuATNpgapVNFse\nzyXD/VLy0KgAxsOC7cy0JviEz5o9x7ZrOnKvdykCgYEAx3DSmiFwmiMM3+YwYwQV\nfjByfKVK1CdL0L90NdAX3/rC3ntFMMGI+HHnD8Id1Ly8V/kf70csIsf3QBTF+dFH\nqHZHPlX4YH/kkpOA6+FZ9FckbukLpe38Mnayn++zOzn61mlFYZ8l9gME6Zgv713u\nIc5U8ewN+3D8EfOfmo3BrWs=\n-----END PRIVATE KEY-----\n",
  "client_email": "sheets@flutter-projects-16bc8.iam.gserviceaccount.com",
  "client_id": "118172742949024871391",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/sheets%40flutter-projects-16bc8.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
)

# Open a Google Sheet by name or URL
sheet = client.open("StreamLit Form").sheet1

# Get data from a specific range or all values
existing_data = sheet.get_all_records()

def submit_record(data):
    sheet.append_row(data)

# Display data in Streamlit
st.dataframe(existing_data)

# List of Business Types and Products
BUSINESS_TYPES = [
    "Manufacturer",
    "Distributor",
    "Wholesaler",
    "Retailer",
    "Service Provider",
]
PRODUCTS = [
    "Electronics",
    "Apparel",
    "Groceries",
    "Software",
    "Other",
]

# Onboarding New Vendor Form
with st.form(key="vendor_form"):
    company_name = st.text_input(label="Company Name*")
    business_type = st.selectbox("Business Type*", options=BUSINESS_TYPES, index=None)
    products = st.multiselect("Products Offered", options=PRODUCTS)
    years_in_business = st.slider("Years in Business", 0, 50, 5)
    onboarding_date = st.date_input(label="Onboarding Date")
    additional_info = st.text_area(label="Additional Notes")

    # Mark mandatory fields
    st.markdown("**required*")

    submit_button = st.form_submit_button(label="Submit Vendor Details")

    # If the submit button is pressed
    if submit_button:
        submit_record([company_name, business_type, ", ".join(products), years_in_business, onboarding_date.strftime("%Y-%m-%d"), additional_info]);
        # submit_record(["John Doe", "johndoe@example.com", "New York", "October 12, 2024"]);
        existing_data = sheet.get_all_records()
        st.dataframe(existing_data)
        st.success("Vendor details successfully submitted!")
