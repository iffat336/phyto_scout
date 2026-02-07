import pandas as pd
import numpy as np

def generate_remediation_data(initial_zinc_ppm, weeks):
    """
    Generates a mock dataset for metal uptake over time.
    
    Args:
        initial_zinc_ppm (float): Starting soil concentration.
        weeks (int): Duration of the experiment.
        
    Returns:
        pd.DataFrame: Data with 'Week', 'Soil_Zinc_PPM', and 'Plant_Zinc_Accumulated'.
    """
    weeks_range = list(range(1, weeks + 1))
    
    # Simulate logarithmic decay of Soil Zinc (Plants suck it up fast then slow down)
    decay_rate = 0.05
    soil_zinc = [initial_zinc_ppm * np.exp(-decay_rate * w) for w in weeks_range]
    
    # Simulate Logistic Growth of Plant Zinc (S-curve)
    # Saturation point is roughly how much the soil lost
    removed_zinc_total = initial_zinc_ppm - soil_zinc[-1]
    
    plant_zinc = []
    for w in weeks_range:
        # Sigmoid function for accumulation
        uptake = removed_zinc_total / (1 + np.exp(-0.5 * (w - (weeks/2))))
        plant_zinc.append(uptake)
        
    df = pd.DataFrame({
        "Week": weeks_range,
        "Soil Zinc (PPM)": soil_zinc,
        "Accumulated Plant Zinc (mg/kg)": [z * 50 for z in plant_zinc] # Scale up for realistic plant tissue numbers
    })
    
    return df
