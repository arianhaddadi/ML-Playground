"""
To run this script, run streamlit run streamlit-server.py
"""

import my_langchain as lch
import streamlit as stl

stl.title("Pets Name Generator")


pet_type = stl.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Cow"))

pet_color = stl.sidebar.text_area(f"What color is your {pet_type}?", max_chars=15)

if pet_color:
    response = lch.generate_pet_name(pet_type, pet_color)
    stl.text(response)