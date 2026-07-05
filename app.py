import streamlit as st
import json
import os
# Aapki purani file (main.py) se function import kar rahe hain
from main import process_posts 

st.set_page_config(page_title="LinkedIn Post Enricher", page_icon="📝", layout="centered")

st.title("📝 LinkedIn Post Analyzer & Enricher")
st.write("Yeh app AI (Groq) ka use karke aapke LinkedIn posts ka metadata nikalta hai aur tags ko unify karta hai.")

# Button to trigger the process
if st.button("Process LinkedIn Posts 🚀", type="primary"):
    # Check agar input file exist karti hai
    if not os.path.exists("data/raw_posts.json"):
        st.error("❌ 'data/raw_posts.json' file nahi mili! Please check karein.")
    else:
        with st.spinner("Groq AI posts ko analyze kar raha hai... Kripya intezar karein..."):
            try:
                # Aapka main function call ho raha hai
                process_posts("data/raw_posts.json", "data/processed_posts.json")
                st.success("🎉 Processing Complete! Nayi file 'processed_posts.json' ban gayi hai.")
                
                # Output ko web screen par dikhane ke liye
                with open("data/processed_posts.json", "r", encoding="utf-8") as f:
                    output_data = json.load(f)
                
                st.subheader("📊 Processed Output Data:")
                st.json(output_data)
                
            except Exception as e:
                st.error(f"Kuch error aaya: {e}")