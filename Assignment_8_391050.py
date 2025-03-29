import streamlit as st

class ExpertSystem:
    def __init__(self):
        self.disease_symptoms = {
            "Common Cold": {"cough": 2, "sneezing": 1, "runny nose": 2, "sore throat": 2, "mild fever": 1},
            "Flu": {"fever": 3, "chills": 2, "body ache": 2, "fatigue": 2, "cough": 2, "headache": 2},
            "COVID-19": {"fever": 3, "dry cough": 3, "shortness of breath": 3, "loss of taste or smell": 4, "fatigue": 2},
            "Malaria": {"fever": 3, "chills": 3, "sweating": 2, "headache": 2, "nausea": 2, "vomiting": 2},
            "Migraine": {"headache": 4, "nausea": 3, "sensitivity to light": 3, "blurred vision": 2, "vomiting": 3},
            "Pneumonia": {"fever": 3, "cough": 3, "chills": 2, "shortness of breath": 4, "chest pain": 3},
            "Dengue": {"fever": 4, "severe headache": 3, "joint pain": 3, "rash": 3, "fatigue": 2}
        }
        self.disease_descriptions = {
            "Common Cold": "A mild viral infection of the nose and throat.",
            "Flu": "A contagious respiratory illness caused by influenza viruses.",
            "COVID-19": "A viral illness affecting the respiratory system, potentially severe.",
            "Malaria": "A mosquito-borne disease caused by parasites.",
            "Migraine": "A neurological condition causing severe headaches.",
            "Pneumonia": "An infection causing inflammation of air sacs in one or both lungs.",
            "Dengue": "A mosquito-borne viral infection that causes flu-like symptoms."
        }
    
    def diagnose(self, user_symptoms):
        disease_confidence = {}
        for disease, symptoms in self.disease_symptoms.items():
            total_weight = sum(symptoms.values())
            match_weight = sum(symptoms[symptom] * intensity for symptom, intensity in user_symptoms.items() if symptom in symptoms)
            confidence = (match_weight / total_weight) * 100 if total_weight > 0 else 0
            if confidence > 0:
                disease_confidence[disease] = confidence
        return disease_confidence

# Streamlit UI
st.title("Medical Expert System")
st.write("Select your symptoms:")

all_symptoms = sorted({symptom for symptoms in ExpertSystem().disease_symptoms.values() for symptom in symptoms})
selected_symptoms = st.multiselect("Select symptoms:", all_symptoms)

user_symptoms = {}
if selected_symptoms:
    st.write("Set intensity for each symptom:")
    for symptom in selected_symptoms:
        intensity = st.slider(f"{symptom.capitalize()} intensity (1-5):", 1, 5, 1)
        user_symptoms[symptom] = intensity

if st.button("Diagnose") and user_symptoms:
    expert_system = ExpertSystem()
    results = expert_system.diagnose(user_symptoms)
    
    if results:
        st.subheader("Possible Diagnoses:")
        for disease, confidence in sorted(results.items(), key=lambda x: x[1], reverse=True):
            st.write(f"**{disease}**: {confidence:.2f}% confidence")
            st.write(f"_Description_: {expert_system.disease_descriptions.get(disease, 'No description available.')}")
    else:
        st.write("No matching diseases found. Please consult a doctor.")