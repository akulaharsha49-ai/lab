
import streamlit as st
import base64


def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("bg.jpeg")

st.markdown(f"""
<style>
.stApp {{
    background: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)),
                url("data:image/jpeg;base64,{img}");
    background-size: cover;
    background-position: center;
}}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="91 Care Helpdesk", page_icon="🏥")


# Center container
col1, col2, col3 = st.columns([2,3,2])

with col2:
    colA, colB = st.columns([1,3])

    with colA:
        st.image("loginlogo.jpg", width=70)

    with colB:
        st.markdown(
            "<h2 style='margin-top:15px;'>91 Care</h2>",
            unsafe_allow_html=True
        )
# -----------------------------
# Session State
# -----------------------------
if "step" not in st.session_state:
    st.session_state.step = "greeting"

if "role" not in st.session_state:
    st.session_state.role = None

# -----------------------------
# ✅ Reusable Back Button (to Main Menu)
# -----------------------------
def back_to_main():
    if st.button("⬅ Back"):
        st.session_state.step = "main"


# -----------------------------
# Greeting Section
# -----------------------------
def greeting():
    st.subheader("Welcome to 91 Care Helpdesk")
    st.write("**Your Role please:**")

    # Row 1 (3 columns)
    row1 = st.columns(3)

    with row1[0]:
        if st.button("👨‍⚕️ Doctor", use_container_width=True):
            st.session_state.role = "Doctor"
            st.session_state.step = "main"

    with row1[1]:
        if st.button("👩‍⚕️ Nurse", use_container_width=True):
            st.session_state.role = "Nurse"
            st.session_state.step = "main"

    with row1[2]:
        if st.button("🧑‍💼 Receptionist", use_container_width=True):
            st.session_state.role = "Receptionist"
            st.session_state.step = "main"

    # Row 2 (3 columns but center-aligned)
    row2 = st.columns(3)  # equal spacing

    with row2[0]:
        if st.button("🧑‍💼 Admin", use_container_width=True):
            st.session_state.role = "Admin"
            st.session_state.step = "main"

    with row2[1]:
        if st.button("👤 Phlebotomist", use_container_width=True):
            st.session_state.role = "Phlebotomist"
            st.session_state.step = "main"
    with row2[2]:
        if st.button("🧪 Pathologist", use_container_width=True):
            st.session_state.role = "Pathologist"
            st.session_state.step = "main"      
    # row2[2] empty → keeps center alignment
# -----------------------------
# ✅ Role-Based Main Menu
# -----------------------------
def main_menu():
    role = st.session_state.role

    # ✅ Back to Role Selection (2nd screen)
    col1, col2 = st.columns([6,1])
    with col2:
        if st.button("🔙"):
            st.session_state.role = None
            st.session_state.step = "greeting"

    st.subheader(f"Hello {role}, How can I help you?")

    # 👨‍⚕️ Doctor View
    if role == "Doctor":
        if st.button("👤 Add patient"):
            st.session_state.step = "add_patient"  
        if st.button("📋Download Reports"):
            st.session_state.step = "DR" 
        if st.button("📋 Update Reports"):
            st.session_state.step = "UR" 
        if  st.button("👤Search Patient"):
            st.session_state.step = "sp" 

            
    # 👩‍⚕️ Nurse View
    elif role == "Nurse":
        if st.button("💳 Billing "):
            st.session_state.step = "billing"
        if st.button("👤 Add patient"):
            st.session_state.step = "add_patient"  
        if st.button("📋Download Reports"):
            st.session_state.step = "DR" 
        if st.button("📋 Update Reports"):
            st.session_state.step = "UR" 
        if  st.button("👤Search Patient"):
            st.session_state.step = "sp" 
        if st.button("👁️ Transaction History"):   
            st.session_state.step = "TH"
        if st.button("🧪Add Test"):
            st.session_state.step = "AT"  
        if st.button("📝 Test List"):
            st.session_state.step = "TL"   
    # 🧑‍💼 Receptionist View
    elif role == "Receptionist":
        if st.button("💳 Billing "):
            st.session_state.step = "billing"
        
        
#Admin

    elif role == "Admin":
        if st.button("💳 Billing "):
            st.session_state.step = "billing"
        if st.button("👤 Add patient"):
            st.session_state.step = "add_patient"  
        if st.button("📋Download Reports"):
            st.session_state.step = "DR" 
        if st.button("📋 Update Reports"):
            st.session_state.step = "UR" 
        if  st.button("👤Search Patient"):
            st.session_state.step = "sp" 
        if st.button("👁️ Transaction History"):   
            st.session_state.step = "TH"
        if st.button("🧪Add Test"):
            st.session_state.step = "AT"  
        if st.button("📝 Test List"):
            st.session_state.step = "TL"                                          

        # 👤 Phlebotomist Viw
    elif role == "Phlebotomist":
        if st.button("👤 Add patient"):
            st.session_state.step = "add_patient"  
        if st.button("📋Download Reports"):
            st.session_state.step = "DR" 
        if st.button("📋 Update Reports"):
            st.session_state.step = "UR" 
        if  st.button("👤Search Patient"):
            st.session_state.step = "sp" 
        if st.button("👁️ Transaction History"):   
            st.session_state.step = "TH"
        if st.button("🧪Add Test"):
            st.session_state.step = "AT"  
        if st.button("📝 Test List"):
            st.session_state.step = "TL"
        if st.button("💳 Billing "):
            st.session_state.step = "billing"  
#pathologist
    elif role == "Pathologist":
        if st.button("📋Download Reports",key="dr_5"):
            st.session_state.step = "DR" 
        if st.button("📋 Update Reports",key="ur_5"):
            st.session_state.step = "UR" 
        if st.button("✅  Report Approval",key="ra_5"):
            st.session_state.step = "RA"



def billing():
    

    st.markdown("""
### 🧾 Billing Instructions

🔹 Go to the **Dashboard**  
🔹 Click on **Add Bill** in the top right corner  

🔹 To add to an existing bill:  
   • Select the bill from the list  

🔹 To create a new bill:  
   • Click on **New Bill**  
   • Search and select the **patient name**  
   • Patient details will be **auto-filled**  
   • Add the required **bill details**  

🔹 Finally, you can:  
   • **Save** the bill  
   • Or **Pay** the bill           
 
""")
    back_to_main()   
def add_patient():    
   st.markdown("""
### 🧾 Patient Instructions

🔹 Go to the **Dashboard**  
🔹 Click on **Add Patient** in the top right corner  
🔹 Fill the form with patient details  
🔹 Save the details  
""")
   back_to_main()
def DR(): 
    st.markdown("""
### 🧾 Download Reports

🔹 Go to the **Billing** section  
🔹 View the list of patients  
🔹 Locate the **Invoice PDF** option at the end of each row  
🔹 Click on it to download the patient report  
""")  
    back_to_main()
def UR():
    st.markdown("""
### 📋 Update Report Instructions

🔹 Go to the **Dashboard**  
🔹 View the list of patients  
🔹 Locate the **Update Report** option at the end of each row  
🔹 Click on it to update the patient report.
""")  
    back_to_main()
def sp():
    st.markdown("""
    ### 🔍 Search Patient Instructions

    🔹 Go to the **Dashboard**  
    🔹 Use the **Search Box** to enter the patient name  
    🔹 View the patient details from the results  
    """)
    back_to_main()
def TH():
    st.markdown("""
### 👁️ Patient Transaction History Instructions

🔹 Go to the **Patients** section  
🔹 View the list of patients  
🔹 Locate the **👁️ (View)** icon at the end of each row  
🔹 Click on it to view the transaction history of the patient  
""")
    back_to_main()
def AT():
    st.markdown("""
### 🧪 Lab Services Instructions

🔹 Go to the **Lab Services** section  
🔹 Click on **Add Test** in the top right corner  

🔹 Fill in the required test details  

🔹 While filling details, you will see a **Type** field with two options:  
   - **One Time**  
   - **Package**  

🔹 If you select **Package**, enter the number of tests.  
   - The total amount will be automatically calculated in the billing section  
   - You can either keep the auto-generated total or modify it manually  

🔹 Click on **Submit** to save
""")
 
    back_to_main() 
def TL():
   
 
    st.markdown("""
### 🧪 Lab Services Instructions

🔹 Go to the **Lab Services** section  
🔹 View the list of available tests  
🔹 Check the test details from the list  
""")  
    back_to_main()
def AD():
    st.markdown("""
### 📦 Add Stock

🔹 Go to the **Inventory** section  
🔹 Click on the **Add Stock** button  
🔹 Enter the stock details  
🔹 Save to add stock  
""") 

    back_to_main()

def RA():
    st.markdown("""
### 📌 Approval Steps
1. Go to **Dashboard**
2. Click on **Waiting for Approval**
3. Approve the request
""")
    back_to_main()    

# Navigation Controller
# -----------------------------
# 
if st.session_state.step == "greeting":
    greeting()

elif st.session_state.step == "main":
    main_menu()

elif st.session_state.step == "billing":
    billing()  

elif st.session_state.step == "add_patient":
    add_patient() 

elif st.session_state.step == "DR":
    DR() 
elif st.session_state.step == "sp":
    sp()  
elif st.session_state.step == "TH":         
    TH()
elif st.session_state.step == "AT":
    AT()  
elif st.session_state.step == "TL":
    TL()  
elif st.session_state.step == "UR":
    UR()    
elif st.session_state.step == "DR":
    DR()  
elif st.session_state.step == "RA":
    RA()               
   