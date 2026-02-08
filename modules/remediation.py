import streamlit as st
import plotly.express as px
from utils.mock_data import generate_remediation_data

def render():
    st.header("🌱 Phytoremediation Tracker")
    st.markdown("Monitor the removal of heavy metals (Zinc) from contaminated soil using *Noccaea caerulescens*.")
    
    with st.expander("🧬 Genetic Mechanism: How does it work?"):
        st.info("""
        **Genomic Driver:** The hyperaccumulation trait in *Noccaea caerulescens* is driven by genomic variations in the **HMA4** gene. 
        
        **Mechanism:** These genetic variations, specifically **Copy Number Variations (CNV)**, enable the plant to pump zinc from roots to shoots at high rates. 
        
        *By integrating this genomic data, we can predict how specific genetic markers contribute to faster or more efficient soil remediation.*
        """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        initial_zinc = st.slider("Initial Soil Zinc (PPM)", min_value=100, max_value=2000, value=800, step=50)
    
    with col2:
        weeks = st.slider("Growth Duration (Weeks)", min_value=4, max_value=24, value=12)
        
    # Generate Data
    df = generate_remediation_data(initial_zinc, weeks)
    
    # Visualization
    tab1, tab2 = st.tabs(["📉 Soil Cleanup", "🌿 Plant Accumulation"])
    
    with tab1:
        fig_soil = px.line(df, x="Week", y="Soil Zinc (PPM)", title="Soil Zinc Depletion", 
                           color_discrete_sequence=["brown"])
        st.plotly_chart(fig_soil, use_container_width=True)
        
    with tab2:
        fig_plant = px.area(df, x="Week", y="Accumulated Plant Zinc (mg/kg)", title="Zinc Accumulation in Plant Tissue",
                            color_discrete_sequence=["green"])
        # Add a threshold line for "Hyperaccumulation" definition (>3000 mg/kg typically)
        fig_plant.add_hline(y=3000, line_dash="dash", annotation_text="Hyperaccumulation Threshold")
        st.plotly_chart(fig_plant, use_container_width=True)
        
    # KPI / Interpretation
    final_soil = df["Soil Zinc (PPM)"].iloc[-1]
    removed_pct = ((initial_zinc - final_soil) / initial_zinc) * 100
    
    st.success(f"**Remediation Status:** {removed_pct:.1f}% reduction in soil Zinc.")
    
    if final_soil < 300: # Arbitrary "Safe" limit
        st.balloons()
        st.info("✅ Soil is now within safe agricultural limits!")
    else:
        st.warning(f"⚠️ Soil still above safe limit (300 PPM). Estimated {(initial_zinc-300)/((initial_zinc-final_soil)/weeks):.1f} more weeks needed.")
