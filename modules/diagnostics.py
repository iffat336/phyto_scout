import streamlit as st

def render():
    st.header("🩺 Deficiency Detective")
    st.markdown("Identify 'Hidden Hunger' (Micronutrient Deficiency) based on visual symptoms.")
    
    with st.expander("🧬 Genetics of Nutrient Uptake"):
        st.info("""
        **Diagnostic Enhancement:** We are integrating genomic data to correlate nutrient deficiency patterns with genetic variations in transport genes (e.g., **IRT1** for Iron, **HMA4** for Zinc).
        
        **Insight:** Plants with specific genetic variations in these transporters may show more pronounced symptoms. This tool aims to identify not just the *symptom* (phenotype), but the *genetic predisposition* (genotype) behind it.
        """)
    
    st.subheader("Visual Symptom Checker")
    
    location = st.selectbox("Where are the symptoms located?", 
                            ["Select...", "Old Leaves (Bottom)", "New Leaves (Top)", "Whole Plant"])
    
    pattern = st.selectbox("What is the pattern?",
                           ["Select...", "Yellowing between veins (Interveinal Chlorosis)", 
                            "Complete yellowing", "Purple/Reddish spots", "Brown/Necrotic edges"])
    
    st.divider()
    
    if st.button("Diagnose"):
        if location == "Select..." or pattern == "Select...":
            st.error("Please select both location and pattern.")
        
        # Decision Logic based on Biology
        elif location == "New Leaves (Top)":
            if pattern == "Yellowing between veins (Interveinal Chlorosis)":
                st.warning("⚠️ **Diagnosis: Iron (Fe) Deficiency**")
                st.markdown("Iron is immobile in plants, so young leaves suffer first.")
            elif pattern == "Complete yellowing":
                st.warning("⚠️ **Diagnosis: Sulfur (S) Deficiency**")
            else:
                 st.warning("⚠️ **Diagnosis: Zinc (Zn) Deficiency**")
                 st.markdown("**High Probability.** Zinc deficiency often causes 'rosetting' (stunted leaves) and chlorosis in new growth.")
                 st.info("💡 **Recommendation:** This aligns with Prof. Aarts' research on *ZIP* transporters. Apply Zinc Sulfate foliar spray.")
                 
        elif location == "Old Leaves (Bottom)":
            if pattern == "Yellowing between veins (Interveinal Chlorosis)":
                 st.warning("⚠️ **Diagnosis: Magnesium (Mg) Deficiency**")
            elif pattern == "Complete yellowing":
                 st.warning("⚠️ **Diagnosis: Nitrogen (N) Deficiency**")
            else:
                 st.error("Unable to determine with high confidence.")
                 
        else:
            st.info("Analysis inconclusive. Please consult a lab test.")

    st.markdown("---")
    st.caption("🔍 **AI Vision Mode** (Coming Soon): Train a CNN on the dataset to detect early-onset chlorosis before the human eye can see it, utilizing NPEC thermal imaging data.")
