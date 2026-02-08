import streamlit as st

def render():
    st.header("💰 Phytomining Economy")
    st.markdown("""
    Calculate the economic potential of **"farming for metals"** (Phytomining).
    
    **Scientific Focus:** Connecting *biomass yield* and *metal accumulation* to real-world market value—demonstrating the "Impact" side of **Botanickel's** mission.
    """)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Field Inputs")
        hectares = st.number_input("Land Area (Hectares)", value=1.0, step=0.5)
        biomass_per_ha = st.number_input("Dry Biomass Yield (tons/ha)", value=10.0, step=0.5, help="Typical yield for Noccaea / hyperaccumulators")
        
    with col2:
        st.subheader("2. Metal Stats")
        metal_type = st.selectbox("Target Metal", ["Zinc (Zn)", "Nickel (Ni)"])
        concentration = st.slider(f"Plant {metal_type} Concentration (mg/kg)", 
                                  min_value=1000, max_value=30000, value=10000, step=500,
                                  help="Concentration in dried leaf tissue")
        
    # Market Prices (Approximate)
    prices = {
        "Zinc (Zn)": 2.50, # $/kg
        "Nickel (Ni)": 18.00 # $/kg (Nickel is much more valuable!)
    }
    
    selected_price = prices[metal_type]
    
    st.subheader("3. Market Data")
    price_input = st.number_input(f"Current Market Price ($/kg)", value=selected_price, step=0.1)
    
    # Calculations
    # 1. Total Biomass (kg) = Hectares * tons/ha * 1000
    total_biomass_kg = hectares * biomass_per_ha * 1000
    
    # 2. Total Metal (kg) = Biomass (kg) * (Concentration (mg/kg) / 1,000,000) -> mg to kg
    total_metal_kg = total_biomass_kg * (concentration / 1000000)
    
    # 3. Gross Value ($)
    gross_value = total_metal_kg * price_input
    
    # 4. Ash Amount (for bio-ore) - Assuming ~5-10% ash content
    ash_mass_kg = total_biomass_kg * 0.08 
    metal_in_ash = (total_metal_kg / ash_mass_kg) * 100 # Percentage
    
    st.divider()
    
    # Results Dashboard
    st.markdown("## 📊 Economic Projection")
    
    r1, r2, r3 = st.columns(3)
    
    r1.metric("Total Metal Harvested", f"{total_metal_kg:.1f} kg")
    r2.metric("Gross Revenue", f"${gross_value:,.2f}")
    r3.metric("Revenue per Hectare", f"${gross_value/hectares:,.2f} /ha")
    
    st.info(f"""
    **Bio-ore Analysis:**
    After burning the biomass for energy, you would be left with **{ash_mass_kg:.0f} kg of Bio-ore ash**.
    
    This ash would contain approx. **{metal_in_ash:.1f}% {metal_type.split()[0]}**. 
    
    *{'High-grade ore! Smelters pay a premium for this.' if metal_in_ash > 10 else 'Low grade, might need enrichment.'}*
    """)
    
    if metal_type == "Nickel (Ni)":
        st.success("💡 **Insight:** Nickel phytomining is generally more profitable than Zinc due to higher market prices, which is why companies like *Botanickel* focus on it.")
