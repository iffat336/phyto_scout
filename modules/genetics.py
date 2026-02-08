import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

def render():
    st.header("🧬 Genetics Explorer (CNV Analysis)")
    st.markdown("""
    Explore the genetic basis of metal hyperaccumulation in *Noccaea caerulescens*. 
    
    **Scientific Focus:** This module demonstrates the correlation between **Gene Copy Number Variation (CNV)** and **Zinc Tolerance**, a key research area of Prof. Mark Aarts.
    
    > [!NOTE]
    > **Mechanism of Adaptation:**
    > *Noccaea* has evolved to tolerate toxic soil not by inventing new genes, but by **duplicating** existing ones (Copy Number Variation).
    >
    > *   **Gene:** **Heavy Metal ATPase 4 (HMA4)**.
    > *   **Action:** Acts as a pump to move Zinc from roots to shoots.
    > *   **Expression:** High copy numbers lead to **transcriptional overexpression** (more mRNA -> more protein pumps).
    > *   **Outcome:** Massive removal of Zinc from roots preventing toxicity, allowing the plant to thrive.
    """)
    
    st.subheader("Population Analysis: Gene Dosage Effect")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        gene = st.selectbox("Select Candidate Gene", ["HMA4 (Heavy Metal ATPase 4)", "ZIP Transporter Family", "MTP1 (Metal Tolerance Protein)"])
        
        st.info(f"""
        **Gene Function:**
        
        *{gene.split('(')[0].strip()}* plays a critical role in sequestering Zinc into the vacuole or pumping it out of roots to prevent toxicity.
        
        **Hypothesis:** Higher copy numbers of this gene = Higher tolerance.
        """)
        
        population_size = st.slider("Population Size (n)", 50, 500, 150)
        
    # Generate Mock Data for CNV
    # Logic: More copies = Higher tolerance (with some noise)
    
    np.random.seed(42)
    
    # Simulate Copy Numbers (e.g., 1 to 10 copies)
    copy_numbers = np.random.randint(1, 8, size=population_size)
    
    # Simulate Tolerance (correlated to copy number + random environmental noise)
    # Base tolerance + (Copy Number * Effect Size) + Noise
    tolerance = 100 + (copy_numbers * 150) + np.random.normal(0, 50, size=population_size)
    
    # Simulate accumulation (also correlated)
    accumulation = 500 + (copy_numbers * 800) + np.random.normal(0, 200, size=population_size)

    df = pd.DataFrame({
        "Plant ID": range(1, population_size + 1),
        "Gene Copy Number": copy_numbers,
        "Zinc Tolerance Index": tolerance,
        "Leaf Zinc Accumulation (PPM)": accumulation
    })
    
    with col2:
        tab1, tab2 = st.tabs(["📊 Tolerance Correlation", "🌿 Leaf Accumulation"])
        
        with tab1:
            fig_tol = px.scatter(df, x="Gene Copy Number", y="Zinc Tolerance Index", 
                                 title=f"Copy Number Variation vs. Tolerance ({gene.split('(')[0]})",
                                 trendline="ols", # Add a trendline to show significant correlation
                                 color="Zinc Tolerance Index",
                                 color_continuous_scale="Viridis")
            st.plotly_chart(fig_tol, use_container_width=True)
            
            st.caption(f"**Observation:** Individuals with high copy numbers of *{gene.split('(')[0]}* display significantly higher tolerance to toxic Zinc levels.")

        with tab2:
             fig_acc = px.box(df, x="Gene Copy Number", y="Leaf Zinc Accumulation (PPM)",
                              title=f"Leaf Zinc Concentration by Copy Number Group",
                              color="Gene Copy Number")
             st.plotly_chart(fig_acc, use_container_width=True)

    st.divider()
    
    st.markdown("""
    ### 🔬 Evolutionary Pathway: From Mutation to Adaptation
    
    1.  **Duplication Event:** A random error in DNA replication creates a second copy of *HMA4*.
    2.  **Selection Pressure:** In toxic soil, plants with 2 copies pump metal faster and survive.
    3.  **Fixation:** Over generations, this Copy Number Variation (CNV) becomes fixed in the population.
    
    This is why *Noccaea caerulescens* is a hyperaccumulator, while its cousin *Arabidopsis thaliana* is not.
    """)
