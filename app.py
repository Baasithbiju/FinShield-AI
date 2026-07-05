import streamlit as st
from financial_engine import analyze_customer
import plotly.graph_objects as go
from report_Generator import generate_report
from customer_database import save_customer, load_customers
from datetime import datetime
from PIL import Image
from pathlib import Path


#logo = Image.open("assets/images/logo.png")
#banner = Image.open("assets/images/bank_banner.jpg")

logo=None
banner = None

logo_path = Path("assets/images/logo.png")
banner_path = Path("assets/images/bank_banner.jpg")

if logo_path.exists():
    logo = Image.open(logo_path)
if banner_path.exists():
    banner = Image.open(banner_path)

# ---------- SIDEBAR ----------
st.sidebar.image(
    "assets/images/logo.png",
    width=80
)
#st.sidebar.image(logo, width=80)
st.sidebar.title("FinShield AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "👤 Customer Analysis",
        "📈 Reports",
        "ℹ About"
    ]
)

st.sidebar.markdown("---")
st.sidebar.success("Version 1.0")

# ---------- DASHBOARD ----------
if page == "🏠 Dashboard":

    st.image(banner, width="stretch")
    st.title("🏦 FinShield AI")
    st.subheader("Intelligent Banking Risk & Customer Insights")

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Customers",
        "1,245",
        "+14%"
    )

    col2.metric(
        "Loans Approved",
        "918",
        "+9%"
    )

    col3.metric(
        "Fraud Alerts",
        "23",
        "-3"
    )

    col4.metric(
        "Risk Cases",
        "74",
        "+6"
    )

    st.markdown("---")

    st.header("🏛 Welcome")

    st.info(
        """
        FinShield AI is an intelligent banking assistant.

        It helps banks:

        ✅ Assess customer financial health

        ✅ Estimate loan eligibility

        ✅ Detect risky applicants

        ✅ Recommend suitable banking products

        ✅ Generate downloadable reports
        """
    )

# ---------- CUSTOMER PAGE ----------
elif page == "👤 Customer Analysis":

    st.title("👤 Customer Financial Assessment")

    st.markdown("Enter customer details for intelligent banking analysis.")

    st.markdown("---")

    with st.form("customer_form"):

        col1, col2 = st.columns(2)

        with col1:

            customer_name = st.text_input("Customer Name")

            age = st.number_input(
                "Age",
                min_value=18,
                max_value=80,
                value=25
            )

            gender = st.selectbox(
                "Gender",
                [
                    "Male",
                    "Female",
                    "Other"
                ]
            )

            occupation = st.selectbox(
                "Occupation",
                [
                    "Software Engineer",
                    "Doctor",
                    "Teacher",
                    "Business",
                    "Government Employee",
                    "Student",
                    "Self Employed",
                    "Other"
                ]
            )

            employment = st.selectbox(
                "Employment Type",
                [
                    "Permanent",
                    "Contract",
                    "Self Employed"
                ]
            )

            salary = st.number_input(
                "Monthly Income (₹)",
                min_value=0,
                value=50000
            )

        with col2:

            expenses = st.number_input(
                "Monthly Expenses (₹)",
                min_value=0,
                value=20000
            )

            savings = st.number_input(
                "Current Savings (₹)",
                min_value=0,
                value=100000
            )

            existing_loan = st.number_input(
                "Existing Loan Amount (₹)",
                min_value=0,
                value=0
            )

            credit_bill = st.number_input(
                "Credit Card Outstanding (₹)",
                min_value=0,
                value=0
            )

            cibil = st.slider(
                "CIBIL Score",
                300,
                900,
                750
            )

            loan_amount = st.number_input(
                "Loan Amount Requested (₹)",
                min_value=0,
                value=500000
            )

            loan_type = st.selectbox(
                "Loan Type",
                [
                    "Home Loan",
                    "Car Loan",
                    "Education Loan",
                    "Personal Loan",
                    "Business Loan"
                ]
            )

        submitted = st.form_submit_button(
            "Analyze Customer"
        )

    if submitted:

        st.success("Customer information captured successfully!")

        st.markdown("---")

        st.subheader("Customer Summary")

        st.write("### Personal Information")

        st.write(f"**Name:** {customer_name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Occupation:** {occupation}")
        st.write(f"**Employment:** {employment}")

        st.write("### Financial Information")

        st.write(f"Monthly Income : ₹{salary:,}")
        st.write(f"Monthly Expenses : ₹{expenses:,}")
        st.write(f"Savings : ₹{savings:,}")
        st.write(f"Existing Loan : ₹{existing_loan:,}")
        st.write(f"Credit Card Outstanding : ₹{credit_bill:,}")
        st.write(f"CIBIL Score : {cibil}")
        st.write(f"Loan Requested : ₹{loan_amount:,}")
        st.write(f"Loan Type : {loan_type}")
        result = analyze_customer(
            salary,
            expenses,
            savings,
            existing_loan,
            credit_bill,
            cibil,
            employment
        )


        customer_record = {

        "Date": datetime.now().strftime("%d-%m-%Y %H:%M"),

        "Customer Name": customer_name,

        "Age": age,

        "Occupation": occupation,

        "Employment": employment,

        "Income": salary,

        "Expenses": expenses,

        "Savings": savings,

        "Existing Loan": existing_loan,

        "Credit Bill": credit_bill,

        "CIBIL": cibil,

        "Loan Requested": loan_amount,

        "Financial Score": result["score"],

        "Risk": result["risk"],

        "Decision": result["decision"]

        }

        save_customer(customer_record)

        st.markdown("---")

        st.header("Financial Analysis")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Financial Score",
            result["score"]
        )

        col2.metric(
            "Risk",
            result["risk"]
        )

        col3.metric(
            "Loan Decision",
            result["decision"]
        )

        st.markdown("---")

        st.subheader("Financial Indicators")

        st.write(f"Debt Ratio : {result['debt_ratio']} %")

        st.write(f"Savings Ratio : {result['savings_ratio']} %")

        st.write(f"Disposable Income : ₹{result['disposable_income']:,}")

        st.markdown("---")

        st.subheader("Decision Factors")

        for reason in result["reasons"]:

            st.success(reason)

        st.markdown("---")

        st.subheader("Relationship Manager Recommendations")

        for item in result["recommendations"]:

            st.info(item)
        
        st.markdown("---")
        st.header("📊 Financial Dashboard")

        col1, col2 = st.columns(2)

        with col1:

            gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=result["score"],
                title={"text": "Financial Health Score"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "green"},
                    "steps": [
                        {"range": [0, 40], "color": "#ffcccc"},
                        {"range": [40, 70], "color": "#fff3cd"},
                        {"range": [70, 100], "color": "#d4edda"}
                    ]
                }
            ))

            st.plotly_chart(gauge, use_container_width=True)

        with col2:

            pie = go.Figure(data=[go.Pie(
                labels=["Expenses", "Savings", "Loan", "Credit Card"],
                values=[
                    expenses,
                    savings,
                    existing_loan,
                    credit_bill
                ],
                hole=0.45
            )])

            pie.update_layout(title="Financial Distribution")

            st.plotly_chart(pie, use_container_width=True)

        bar = go.Figure()

        bar.add_bar(
            x=["Income", "Expenses", "Savings"],
            y=[salary, expenses, savings]
        )

        bar.update_layout(
            title="Income vs Expenses vs Savings",
            xaxis_title="Category",
            yaxis_title="Amount (₹)"
        )

        st.plotly_chart(bar, use_container_width=True)
        st.markdown("---")

        st.header("🤖 AI Relationship Manager Summary")

        if result["score"] >= 80:

            st.success("""
        Customer demonstrates excellent financial discipline.

        Recommended for premium banking services.

        Very low repayment risk.

        Suitable for cross-selling Home Loan, Premium Credit Card and Fixed Deposit.
        """)

        elif result["score"] >= 60:

            st.warning("""
        Customer has moderate financial stability.

        Manual review is recommended before approval.

        Offer secured banking products.
        """)

        else:

            st.error("""
        Customer has significant financial risk.

        Loan approval is not recommended at this stage.

        Suggest improving CIBIL score and reducing debt before reapplying.
        """)


        pdf_file = generate_report(customer_name, result)

        with open(pdf_file, "rb") as file:

            st.download_button(
                "📄 Download Customer Report",
                file,
                file_name=pdf_file.split("/")[-1],
                mime="application/pdf"
            )


# ---------- REPORT PAGE ----------
elif page == "📈 Reports":

    st.title("📈 Customer Reports")

    df = load_customers()

    if df.empty:

        st.warning("No customer reports available.")

    else:

        st.success(f"{len(df)} Customers Analyzed")

        st.dataframe(df, use_container_width=True)

        st.download_button(

            "📥 Download Excel Report",

            df.to_csv(index=False).encode("utf-8"),

            file_name="Customer_Reports.csv",

            mime="text/csv"
        )

# ---------- ABOUT ----------
else:

    st.title("ℹ About")

    st.write("""
FinShield AI

A Python + Streamlit BFSI application.

Built for Banking & Financial Services.

Developed using

• Python

• Streamlit

• Pandas

• Plotly

• FPDF
""")

st.markdown("---")
st.markdown(
    """
    <div style = 'text-align: center'>
    <h4>FinShield AI - Intelligent Banking Assistant</h4>
    <p> Intellegent Banking Risk & Customer Insights</p>
    <p> Developed by <b>Mohammed Baasith</b></p>
    </div>
    """,
    unsafe_allow_html=True
)