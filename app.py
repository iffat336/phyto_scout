import streamlit as st
from modules import remediation, biomass, diagnostics

# Page Config
st.set_page_config(
    page_title="PhytoScout | WUR",
    page_icon="🌱",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("🌱 PhytoScout")
st.sidebar.markdown("*Science for Impact*")
st.sidebar.markdown("---")

page = st.sidebar.radio("Navigate", ["Home", "Phytoremediation Tracker", "Biomass Predictor", "Deficiency Detective"])

st.sidebar.markdown("---")
st.sidebar.caption("Prototype built for Prof. Mark Aarts' Lab")
st.sidebar.caption("v1.0.0 | Wageningen University")

if page == "Home":
    st.title("Welcome to PhytoScout 🌍")
    st.image("https://www.wur.nl/upload/f9829878-3617-48f8-9a3d-495c0244405a_WUR_Logo.png", width=200) # Placeholder WUR logo or generic
    
    st.markdown("""
    ### Bridging Fundamental Genetics & Field Application
    
    **PhytoScout** is a unified platform integrating three critical pillars of modern plant science:
    
    1.  **🧲 Metal Hyperaccumulation (Remediation)**
        *   *Based on:* Research on *Noccaea caerulescens* and ZIP transporters.
        *   *Goal:* Monitor soil cleanup progress and optimize harvest timing.
        
    2.  **📸 Digital Phenotyping (Biomass)**
        *   *Based on:* NPEC high-throughput imaging & Photosynthesis studies.
        *   *Goal:* Predict yield/biomass from simple canopy images using CV.
        
    3.  **🩺 Hidden Hunger (Diagnostics)**
        *   *Based on:* Nutrient homeostasis and deficiency signaling.
        *   *Goal:* Early detection of Zinc/Iron deficiency in crops.
    """)
    
    st.info("👈 Select a module from the sidebar to begin.")

elif page == "Phytoremediation Tracker":
    remediation.render()

elif page == "Biomass Predictor":
    biomass.render()

elif page == "Deficiency Detective":
    diagnostics.render()
