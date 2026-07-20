import os
from datetime import date
import pandas as pd
import streamlit as st

# ---------------------------------------------------------
# 1. Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Sri Kanakadurgamma Thalli", page_icon="🪔", layout="wide"
)

# ---------------------------------------------------------
# 2. CSV File Setup
# ---------------------------------------------------------
CHANDA_FILE = "chanda.csv"
EXPENSES_FILE = "expenses.csv"

if not os.path.exists(CHANDA_FILE):
    df_chanda_init = pd.DataFrame([
        {
            "Surname": "కట్ట (Katta)",
            "Name": "రమేష్ (Ramesh)",
            "Amount": 1116,
            "Date": "2026-07-20",
        },
        {
            "Surname": "బండారి (Bandari)",
            "Name": "సురేష్ (Suresh)",
            "Amount": 501,
            "Date": "2026-07-20",
        },
        {
            "Surname": "గౌడ్ (Goud)",
            "Name": "మహేష్ (Mahesh)",
            "Amount": 2016,
            "Date": "2026-07-19",
        },
        {
            "Surname": "వేముల (Vemula)",
            "Name": "రాజేష్ (Rajesh)",
            "Amount": 1000,
            "Date": "2026-07-19",
        },
    ])
    df_chanda_init.to_csv(CHANDA_FILE, index=False)

if not os.path.exists(EXPENSES_FILE):
    df_exp_init = pd.DataFrame([
        {
            "Year": "2026",
            "Date": "2026-07-20",
            "Expense Item": "లైటింగ్ & మైక్ సెట్",
            "Cost": 15000,
        },
        {
            "Year": "2026",
            "Date": "2026-07-20",
            "Expense Item": "పూల అలంకరణ",
            "Cost": 8000,
        },
        {
            "Year": "2026",
            "Date": "2026-07-19",
            "Expense Item": "ప్రసాదం తయారీ",
            "Cost": 12000,
        },
        {
            "Year": "2025",
            "Date": "2025-10-12",
            "Expense Item": "పండిత సన్మానం",
            "Cost": 5000,
        },
    ])
    df_exp_init.to_csv(EXPENSES_FILE, index=False)


def load_chanda():
    return pd.read_csv(CHANDA_FILE)


def load_expenses():
    return pd.read_csv(EXPENSES_FILE)


# ---------------------------------------------------------
# 3. Custom Dark Red & Glowing Styling
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #2b0000;
        background-image: linear-gradient(180deg, #3d0000 0%, #1a0000 100%);
        color: #FFD700 !important;
    }
    
    .main-title {
        text-align: center;
        color: #FFD700;
        font-size: 3.2rem;
        font-weight: bold;
        text-shadow: 2px 2px 6px #000000;
        margin: 15px 0px 5px 0px;
    }
    .sub-title {
        text-align: center;
        color: #FFFAED;
        font-size: 1.3rem;
        margin-bottom: 5px;
    }
    .location-title {
        text-align: center;
        color: #FFD700;
        font-size: 1.1rem;
        font-weight: bold;
        margin-bottom: 25px;
    }

    div[data-testid="stHorizontalBlock"] div[role="radiogroup"] {
        display: flex;
        justify-content: center;
        gap: 12px;
        width: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        padding: 12px;
        border-radius: 12px;
        border: 2px solid #FFD700;
        margin-top: 10px;
    }

    div[role="radiogroup"] > label {
        background-color: #5C0000 !important;
        border: 2px solid #FFD700 !important;
        border-radius: 8px !important;
        padding: 10px 18px !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
        cursor: pointer;
    }

    div[role="radiogroup"] > label[data-checked="true"] {
        background-color: #FFD700 !important;
        color: #000000 !important;
        box-shadow: 0px 0px 15px #FFD700 !important;
    }

    div[role="radiogroup"] > label > div:first-child { display: none; }

    .telugu-quote, .wiki-box {
        background-color: rgba(255, 215, 0, 0.08);
        border-left: 5px solid #FFD700;
        border-right: 1px solid rgba(255, 215, 0, 0.2);
        padding: 20px;
        border-radius: 8px;
        margin: 20px 0px;
    }
    .telugu-quote { text-align: center; }
    .telugu-quote h2 { color: #FFD700; font-size: 1.8rem; margin: 0; }

    .stTable, div[data-testid="stDataFrame"] {
        background-color: rgba(40, 0, 0, 0.7) !important;
        border: 1px solid #FFD700 !important;
        border-radius: 10px;
        padding: 5px;
    }

    th { color: #FFD700 !important; background-color: #4a0000 !important; }
    td { color: #FFFFFF !important; }
    p, span, label, div { color: #FFFAED; }

    .img-box {
        background: rgba(0, 0, 0, 0.6);
        border: 3px solid #FFD700;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0px 0px 15px #FFD700;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# STEP 1: OPTIONS FIRST (Top Navigation Menu)
# ---------------------------------------------------------
selected_tab = st.radio(
    "",
    options=[
        "📖 Home (హోమ్)",
        "💰 Day-wise Chanda (చందా)",
        "🖼️ Festival Pics (ఫోటోలు)",
        "📊 Day-wise Expenses (ఖర్చులు)",
        "🤝 Committee (కమిటీ)",
    ],
    horizontal=True,
    label_visibility="collapsed",
)

st.write("---")

# ---------------------------------------------------------
# STEP 2: MIDDLE HEADLINE WITH LOCATION
# ---------------------------------------------------------
st.markdown(
    "<h1 class='main-title'>🪔 శ్రీ కనకదుర్గమ్మ తల్లి 🪔</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h4 class='sub-title'>గ్రామ ఉత్సవాలు, చందా మరియు వ్యయాల పోర్టల్</h4>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p class='location-title'>📍 కూరడ దిగువ, గుడ్లవల్లేరు (Kurada Dhiguva, Gudlavalleru)</p>",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# STEP 3 & 4: HOME TAB (Image & Wikipedia Below Headline)
# ---------------------------------------------------------
if selected_tab == "📖 Home (హోమ్)":
    col1, col2, col3 = st.columns([1, 2, 1])
    image_file = "amma.jpg"

    with col2:
        st.markdown("<div class='img-box'>", unsafe_allow_html=True)
        if os.path.exists(image_file):
            st.image(
                image_file,
                caption="శ్రీ కనకదుర్గమ్మ తల్లి",
                use_container_width=True,
            )
        else:
            st.error(
                f"⚠️ Image file `{image_file}` not found in the project directory."
            )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='telugu-quote'>
            <h2>"దుర్గమ్మ మనకి కొత్త లైఫ్ తీస్కొస్తుంది"</h2>
            <p style='color: #FFFAED; font-size: 1.1rem; margin-top: 5px;'>- అమ్మవారి ఆశీస్సులతో మన గ్రామం సుభిక్షంగా ఉండాలని ఆకాంక్షిస్తూ...</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='wiki-box'>
            <h3 style='color: #FFD700; margin-top:0;'>📚 శ్రీ కనకదుర్గ అమ్మవారి చరిత్ర (Wikipedia Overview)</h3>
            <p style='line-height: 1.6; font-size: 1.05rem;'>
                <b>శ్రీ కనక దుర్గ గుడి</b> భారతదేశంలోని ఆంధ్ర ప్రదేశ్ రాష్ట్రంలోని విజయవాడ నగరంలో కృష్ణా నది ఒడ్డున ఉన్న ఇంద్రకీలాద్రి పర్వతంపై వెలసిన ప్రసిద్ధ పుణ్యక్షేత్రం. 
                శ్రీ కనకదుర్గమ్మ వారు స్వయంభూగా ఇంద్రకీలాద్రిపై అవతరించారని క్షేత్ర పురాణం చెబుతోంది. 
                రాక్షస సంహారం చేసి భక్తులను కాపాడిన దుర్గమ్మ తల్లిని దర్శించుకోవడానికి ప్రతీ ఏటా లక్షలాది మంది భక్తులు విచ్చేస్తారు. 
                నవరాత్రి ఉత్సవాలు మరియు గ్రామోత్సవాలు ఇక్కడ అత్యంత వైభవంగా జరుగుతాయి.
            </p>
        </div>
    """,
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------
# CHANDA PAGE
# ---------------------------------------------------------
elif selected_tab == "💰 Day-wise Chanda (చందా)":
    st.subheader("💰 చందాల వివరాలు (Day-wise Chanda)")
    chanda_df = load_chanda()

    with st.expander("➕ కొత్త చందా నమోదు చేయండి"):
        with st.form("add_chanda_form", clear_on_submit=True):
            col_s, col_n, col_a, col_d = st.columns(4)
            new_surname = col_s.text_input("ఇంటి పేరు (Surname)")
            new_name = col_n.text_input("పేరు (Name)")
            new_amount = col_a.number_input(
                "చందా మొత్తం ₹ (Amount)", min_value=1, step=50
            )
            new_date = col_d.date_input("తేదీ (Date)", value=date.today())

            submit_chanda = st.form_submit_button("నమోదు చేయి (Save Entry)")
            if submit_chanda:
                if new_surname and new_name:
                    new_row = pd.DataFrame([{
                        "Surname": new_surname,
                        "Name": new_name,
                        "Amount": new_amount,
                        "Date": str(new_date),
                    }])
                    new_row.to_csv(
                        CHANDA_FILE, mode="a", header=False, index=False
                    )
                    st.success("చందా విజయవంతంగా నమోదు చేయబడింది!")
                    st.rerun()
                else:
                    st.warning("దయచేసి ఇంటి పేరు మరియు పేరు నమోదు చేయండి.")

    selected_date = st.date_input(
        "తేదీని ఎంచుకోండి (Select Date)", value=date.today(), key="chanda_date"
    )
    chanda_df["Date"] = pd.to_datetime(chanda_df["Date"]).dt.date
    filtered_chanda = chanda_df[chanda_df["Date"] == selected_date][
        ["Surname", "Name", "Amount", "Date"]
    ]

    st.write(f"### వివరాలు: {selected_date}")
    if not filtered_chanda.empty:
        st.table(filtered_chanda)
        st.success(
            f"**ఈరోజు సేకరించిన మొత్తం చందా:** ₹{filtered_chanda['Amount'].sum():,}"
        )
    else:
        st.warning("ఈ తేదీన చందా వివరాలు నమోదు కాలేదు.")

# ---------------------------------------------------------
# FESTIVAL PICS PAGE
# ---------------------------------------------------------
elif selected_tab == "🖼️ Festival Pics (ఫోటోలు)":
    st.subheader("🖼️ ఉత్సవ ఫోటోలు (Year-wise Photos)")
    selected_year = st.selectbox(
        "సంవత్సరాన్ని ఎంచుకోండి", ["2026", "2025", "2024"]
    )

    st.write(f"### {selected_year} ఉత్సవ చిత్రాలు")
    img_col1, img_col2 = st.columns(2)
    with img_col1:
        st.image(
            "https://images.unsplash.com/photo-1609137144813-7d9921338f24?w=500",
            caption=f"గ్రామ ఊరేగింపు - {selected_year}",
        )
    with img_col2:
        st.image(
            "https://images.unsplash.com/photo-1567157577867-05ccb1388e66?w=500",
            caption=f"ఆలయ అలంకరణ - {selected_year}",
        )

# ---------------------------------------------------------
# EXPENSES PAGE
# ---------------------------------------------------------
elif selected_tab == "📊 Day-wise Expenses (ఖర్చులు)":
    st.subheader("📊 ఉత్సవ ఖర్చుల వివరాలు (Expenses)")
    exp_df = load_expenses()

    with st.expander("➕ కొత్త ఖర్చు నమోదు చేయండి"):
        with st.form("add_expense_form", clear_on_submit=True):
            ec1, ec2, ec3, ec4 = st.columns(4)
            e_year = ec1.selectbox("సంవత్సరం (Year)", ["2026", "2025"])
            e_item = ec2.text_input("ఖర్చు వివరాలు (Expense Item)")
            e_cost = ec3.number_input(
                "ఖర్చు మొత్తం ₹ (Cost)", min_value=1, step=100
            )
            e_date = ec4.date_input(
                "తేదీ (Date)", value=date.today(), key="exp_form_date"
            )

            submit_exp = st.form_submit_button("ఖర్చు నమోదు చేయి (Save Expense)")
            if submit_exp:
                if e_item:
                    new_exp_row = pd.DataFrame([{
                        "Year": str(e_year),
                        "Date": str(e_date),
                        "Expense Item": e_item,
                        "Cost": e_cost,
                    }])
                    new_exp_row.to_csv(
                        EXPENSES_FILE, mode="a", header=False, index=False
                    )
                    st.success("ఖర్చు వివరాలు నమోదు చేయబడ్డాయి!")
                    st.rerun()
                else:
                    st.warning("దయచేసి ఖర్చు వివరాలు టైప్ చేయండి.")

    col_yr, col_dt = st.columns(2)
    with col_yr:
        exp_year = st.selectbox(
            "సంవత్సరం ఫిల్టర్", ["2026", "2025"], key="exp_yr_filter"
        )
    with col_dt:
        exp_date = st.date_input(
            "తేదీ ఫిల్టర్", value=date.today(), key="exp_dt_filter"
        )

    exp_df["Date"] = pd.to_datetime(exp_df["Date"]).dt.date
    filtered_expenses = exp_df[
        (exp_df["Year"].astype(str) == str(exp_year))
        & (exp_df["Date"] == exp_date)
    ]

    if not filtered_expenses.empty:
        st.table(filtered_expenses[["Expense Item", "Cost", "Date"]])
        st.error(
            f"**మొత్తం ఖర్చు:** ₹{filtered_expenses['Cost'].sum():,}"
        )
    else:
        st.info("ఈ తేదీన ఖర్చులు ఏవీ నమోదు కాలేదు.")

# ---------------------------------------------------------
# COMMITTEE PAGE (NO ROLE COLUMN)
# ---------------------------------------------------------
elif selected_tab == "🤝 Committee (కమిటీ)":
    st.subheader("🤝 ఉత్సవ కమిటీ సభ్యులు (Committee Members)")

    members_data = [
        {"పేరు (Name)": "వి. రామారావు"},
        {"పేరు (Name)": "కె. శ్రీనివాస్"},
        {"పేరు (Name)": "ఎమ్. కృష్ణ"},
        {"పేరు (Name)": "బి. ఆంజనేయులు"},
    ]

    st.table(pd.DataFrame(members_data))
