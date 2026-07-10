import streamlit as st

from supabase import create_client, Client
# from src.ui.styles import apply_all_styles

# apply_all_styles()


supabase: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)