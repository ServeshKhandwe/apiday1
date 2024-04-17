import streamlit as st
from datetime import datetime
from google.oauth2 import service_account
import gspread

# Load the Google Sheets credentials from secrets
credentials_info = st.secrets["gcp_service_account"]

# Authenticate using the credentials
gc = gspread.service_account_from_dict(credentials_info)

# Open the Google Sheet by ID extracted from the secrets
spreadsheet_id = "1BJ8iuKggYgrVWsEyc_SYG4qjEnQs4Lt09ie72zcjJHY"  # Directly use the ID from the URL
sheet = gc.open_by_key(spreadsheet_id).sheet1

st.title("Green Boot Camp")
st.subheader("API day 1")
st.subheader("Statusinformationen des ProITK")

Stichtag = st.date_input("Stichtag")
Status_options = ["Gesamtstatus", "Fortschritt", "Finanzen", "Personal"]
Status = st.selectbox("Status", Status_options)
AKZ = st.text_input("AKZ")
Ampelfarbe_options = ["rot", "gelb", "grün"]
Ampelfarbe = st.selectbox("Ampelfarbe", Ampelfarbe_options)
Qualitative_Erläuterung = st.text_input("Qualitative Erläuterung")
Einschätzung_Unterstützungs_Eskalationsbedarf_options = ["ja", "nein"]
Einschätzung_Unterstützungs_Eskalationsbedarf = st.selectbox("Einschätzung Unterstützungs-/Eskalationsbedarf", Einschätzung_Unterstützungs_Eskalationsbedarf_options)
Wo_besteht_Unterstützungs_Eskalationsbedarf = st.text_input("Wo besteht Unterstützungs-/Eskalationsbedarf?")

if st.button("Submit"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_to_append = [timestamp, Stichtag.strftime("%Y-%m-%d"), Status, AKZ, Ampelfarbe, Qualitative_Erläuterung, Einschätzung_Unterstützungs_Eskalationsbedarf, Wo_besteht_Unterstützungs_Eskalationsbedarf]
    sheet.append_rows([data_to_append])
    st.success("Data submitted successfully!")