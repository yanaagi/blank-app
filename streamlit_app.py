import streamlit as st
import pandas as pd

# Define the price list
price_list = {
    "12-Lead ECG": 283.00,
    "ABO/RH": 103.40,
    "Albumin": 125.40,
    "Alkaline Phosphatase": 125.40,
    "ALT/SGPT": 209.00,
    "AST/SGOT": 209.00,
    "Blood Urea Nitrogen (BUN)": 129.80,
    "Calcium": 169.40,
    "Calcium Ionized": 506.00,
    "Chest X-Ray - AP": 323.00,
    "Chest X-Ray - Lateral": 323.00,
    "Chest X-Ray - PA": 323.00,
    "Chloride": 162.80,
    "Complete Blood Count (CBC)": 156.00,
    "Creatinine": 152.90,
    "Erythrocyte Sedimentation Rate (ESR)": 132.00,
    "Fecalysis": 77.00,
    "Glucose (FBS/RBS)": 110.00,
    "HbA1C": 400.00,
    "Hepa C (HCV)": 229.90,
    "Hepatitis B Surface Antigen (HBsAg)": 354.20,
    "Lipid Profile": 860.20,
    "Magnesium": 217.80,
    "Phosphorus": 200.20,
    "Potassium": 200.20,
    "Rapid Plasma Reagin (RPR)": 202.40,
    "Sodium": 200.20,
    "Total Calcium": 169.40,
    "Total Cholesterol": 136.40,
    "Total Protein": 125.40,
    "TPAG": 209.00,
    "Uric Acid": 134.20,
    "Urinalysis": 110.00,
}

# Streamlit UI
def main():
    st.title("Lab Test Table Generator")
    
    if "patients" not in st.session_state:
        st.session_state.patients = []
    
    # Input for patient name and date
    date = st.date_input("Select Date")
    patient_name = st.text_input("Enter Patient Name")
    
    # Multi-select for lab tests
    selected_tests = st.multiselect("Select Lab Tests", list(price_list.keys()))
    
    if st.button("Save Patient"):
        if not patient_name or not selected_tests:
            st.warning("Please enter a patient name and select at least one test.")
        else:
            total_price = sum(price_list[test] for test in selected_tests)
            st.session_state.patients.append({
                "Date": date.strftime("%Y-%m-%d"),
                "Patient Name": patient_name,
                "Test/Procedures": "\n".join(selected_tests),
                "Price": "\n".join([f"{price_list[test]:.2f}" for test in selected_tests]),
                "Total": f"P {total_price:.2f}"
            })
            st.success(f"Added {patient_name} to the table.")
    
    if st.session_state.patients:
        st.write("### Generated Table")
        df = pd.DataFrame(st.session_state.patients)
        st.table(df)
        
        total_amount = sum(float(row["Total"].replace("P ", "")) for row in st.session_state.patients)
        st.write(f"### Total Amount: P {total_amount:.2f}")

if __name__ == "__main__":
    main()
