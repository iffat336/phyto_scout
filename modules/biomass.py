import streamlit as st
from utils.image_processing import calculate_green_index
from PIL import Image

def render():
    st.header("📸 Biomass Predictor (NPEC-Lite)")
    st.markdown("Estimate plant biomass from top-down photos using Computer Vision (Greenness Index).")
    
    uploaded_file = st.file_uploader("Upload a top-down photo of the plant", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(uploaded_file, caption="Original Image", use_column_width=True)
            
        with st.spinner("Analyzing spectral data..."):
            green_ratio, processed_img = calculate_green_index(uploaded_file)
            
            # Simple "Dummy" Regression Model based on Prof. Aarts' lab concept
            # Biomass = GreenRatio * Factor
            estimated_biomass_g = green_ratio * 3.5  # Arbitrary factor for demo
            projected_yield_g = estimated_biomass_g * 4.2 # Projected growth
            
        with col2:
            st.image(processed_img, caption="Green Mask (Computer Vision)", use_column_width=True)
            
        st.divider()
        
        # Results Display
        m1, m2, m3 = st.columns(3)
        m1.metric("Green Pixel Ratio", f"{green_ratio:.1f}%")
        m2.metric("Est. Current Biomass", f"{estimated_biomass_g:.1f} g")
        m3.metric("Projected Yield (Day 40)", f"{projected_yield_g:.1f} g")
        
        st.info("ℹ️ **Scientific Note:** This module mimics the high-throughput phenotyping done at NPEC. "
                "By masking non-green pixels, we remove soil background to correlate 'Projected Canopy Area' with biomass.")
    
    else:
        st.info("Please upload an image to start analysis.")
