import streamlit as st
import pandas as pd

# --- Initialize session state for customers ---
if 'customers' not in st.session_state:
    st.session_state.customers = pd.DataFrame(columns=["ID", "Name", "Email", "Phone", "Status"])

# --- Sidebar Navigation ---
st.sidebar.title("📊 CRM Dashboard")
page = st.sidebar.radio("Go to", ["Dashboard", "Add Customer","Add Customer2", "Search"])

# --- Dashboard Page ---
if page == "Dashboard":
    st.title("📋 Customer Overview")
    st.write("List of all customers in the system.")
    st.dataframe(st.session_state.customers)

# --- Add Customer Page ---
elif page == "Add Customer":
    st.title("➕ Add New Customer")
    
    with st.form("add_customer_form"):
        id = st.text_input("Customer ID")
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        status = st.selectbox("Status", ["Active", "Prospect", "Inactive"])
        
        submitted = st.form_submit_button("Add Customer")
        
        if submitted:
            new_customer = {
                "ID": id,
                "Name": name,
                "Email": email,
                "Phone": phone,
                "Status": status
            }
            st.session_state.customers = pd.concat([
                st.session_state.customers,
                pd.DataFrame([new_customer])
            ], ignore_index=True)
            st.success(f"Customer '{name}' added successfully!")

# --- Add Customer Page ---
elif page == "Add Customer2":
    st.title("➕ Add New Customer2")
    
    with st.form("add_customer_form2"):
        id = st.text_input("Customer ID")
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        status = st.selectbox("Status", ["Active", "Prospect", "Inactive"])
        
        submitted = st.form_submit_button("Add Customer2")
        
        if submitted:
            new_customer = {
                "ID": id,
                "Name": name,
                "Email": email,
                "Phone": phone,
                "Status": status
            }
            st.session_state.customers = pd.concat([
                st.session_state.customers,
                pd.DataFrame([new_customer])
            ], ignore_index=True)
            st.success(f"Customer '{name}' added successfully!")

# --- Search Page ---
elif page == "Search":
    st.title("🔍 Search Customers")
    
    search_term = st.text_input("Enter name, email, or phone to search")
    if search_term:
        mask = (
            st.session_state.customers["Name"].str.contains(search_term, case=False) |
            st.session_state.customers["Email"].str.contains(search_term, case=False) |
            st.session_state.customers["Phone"].str.contains(search_term, case=False)
        )
        results = st.session_state.customers[mask]
        st.write(f"Found {len(results)} matching customer(s):")
        st.dataframe(results)
    else:
        st.info("Enter a search term above to find customers.")
