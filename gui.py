import streamlit as st

from blood_donor_views import BloodDonorManager

donor_instance = BloodDonorManager()

tab1, tab2 = st.tabs(["Add", "View"])

with tab1:
    st.title("Add New Blood Donor")
    name = st.text_input("Enter Donor Name")
    blood = st.selectbox("Select Your Blood Group", ["A+", "B+", "O+", "AB+", "A-", "B-", "O-", "AB-"])
    phone = st.text_input("Enter Phone Number")
    city = st.text_input("Enter City")
    last_d = st.date_input("Enter Last Donation Date ")
    if st.button("Add New Donor"):
        donor_instance.post(name=name, blood_group= blood, phone= phone, city= city, last_donation= last_d)
        st.success("Blood Donor Added Successfully")

with tab2:
    st.title("View Blood Donor Details")
    records = donor_instance.get()
    if records:
        st.table(records)
    else:
        st.warning("No Donors Found!")

