import pandas as pd 
import plotly.express as px 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

PROJECT_NAME = "Road Safety Atlas India"
CREATOR_NAME = "Kartikey Rajpoot"
PROJECT_TAGLINE = "A personal dashboard exploring road accident trends across India."

st.set_page_config(
    page_title=f"{PROJECT_NAME} | {CREATOR_NAME}",
    page_icon="logo.png",
    layout="wide",
)

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1.2rem;
            padding-bottom: 2rem;
        }
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #eff6ff 0%, #f8fafc 100%);
        }
        div[data-testid="stMetric"] {
            background: #f8fafc;
            border: 1px solid #dbeafe;
            border-radius: 18px;
            padding: 0.9rem;
        }
        .hero-card {
            padding: 1rem 1.1rem;
            border-radius: 18px;
            border: 1px solid rgba(15, 118, 110, 0.2);
            background: linear-gradient(135deg, rgba(14, 116, 144, 0.08), rgba(249, 115, 22, 0.10));
            margin-bottom: 1rem;
        }
        .footer-note {
            margin-top: 1.75rem;
            padding-top: 1rem;
            border-top: 1px solid #e2e8f0;
            color: #475569;
            font-size: 0.95rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.image("logo.png", width="stretch")
st.sidebar.markdown(
    f"""
    <div style='padding: 1rem 0.85rem; border-radius: 18px; background: linear-gradient(135deg, #0f172a, #0f766e); color: white; text-align: center; box-shadow: 0 16px 32px rgba(15, 23, 42, 0.12);'>
        <h1 style='margin-bottom: 0.35rem; font-size: 1.8rem;'>{PROJECT_NAME}</h1>
        <p style='margin: 0; font-size: 0.95rem; line-height: 1.5;'>{PROJECT_TAGLINE}</p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.sidebar.caption(f"Designed and developed by {CREATOR_NAME}")
st.sidebar.caption("Built with Streamlit, Plotly, pandas, and public MoRTH data.")
option = st.sidebar.selectbox(
    "Explore",
    [
        "Dashboard Overview",
        "Low-Accident Regions",
        "High-Accident Regions",
        "State Comparison",
        "Union Territory Comparison",
    ],
)

# function for loading data and saving into cache
@st.cache_data
def load_data():
    df_states = pd.read_csv(r"datasets/states_dataset.csv", index_col=0)
    df_ut = pd.read_csv(r"datasets/ut_dataset.csv", index_col=0)
    return df_states, df_ut

df_states, df_ut = load_data()
total_accidents = int(df_states["Total_5yr"].sum() + df_ut["Total_5yr"].sum())
highest_state = df_states["Total_5yr"].idxmax()
highest_state_count = int(df_states["Total_5yr"].max())
lowest_state = df_states["Total_5yr"].idxmin()
lowest_state_count = int(df_states["Total_5yr"].min())

# option selection
if option == "Dashboard Overview":
    st.title(PROJECT_NAME)
    st.markdown(
        f"""
        <div class='hero-card'>
            I built <strong>{PROJECT_NAME}</strong> as a personal data analytics project to
            study how road accident counts changed across Indian states and union territories
            between 2018 and 2022. The dashboard turns cleaned public data into a clearer story
            through comparisons, rankings, and interactive charts.
        </div>
        """,
        unsafe_allow_html=True,
    )
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    metric_col1.metric("Total accidents studied", f"{total_accidents:,}")
    metric_col2.metric("Highest 5-year state total", highest_state, f"{highest_state_count:,}")
    metric_col3.metric("Lowest 5-year state total", lowest_state, f"{lowest_state_count:,}")
    st.markdown("""
    ## 🗂️ Dataset Information

    - **Years Covered:** 2018 — 2022  
    - **Regions:** 28 States & 8 Union Territories  
    - **Source:** *Ministry of Road Transport & Highways (MoRTH)*  
    - **Columns:**  
        - State/UT  
        - Accident Count (Year-wise)  
        - Total accidents over 5 years   
    - **Data Type:** Cleaned numerical dataset  
    """)

    sde_option = st.sidebar.selectbox("Breakdown", ["State Analysis", "Union Territory Analysis"])
    if sde_option == "State Analysis":
      st.subheader("📈 State Accident Trend Comparison")
      opt = st.selectbox("Choose a chart", ["Line Graph", "Heatmap", "Bar Graph"])
      if opt == "Line Graph":
        st.subheader("Line graph view")
        fig = px.line(df_states.reset_index(), x='State', y=['2018','2019','2020','2021','2022'], markers=True)
        st.plotly_chart(fig, width="stretch")

      elif opt == "Heatmap":
        st.subheader("Heatmap view")
        fig2, ax = plt.subplots(figsize=(12, 6))
        fig = sns.heatmap(df_states, cmap='Reds', ax=ax)
        st.pyplot(fig2)
      
      elif opt == "Bar Graph":
         st.subheader("Bar graph view")
         fig = px.bar(df_states.reset_index(), x='State', y=['2018','2019','2020','2021','2022'],color='State', log_y=True)
         st.plotly_chart(fig, width="stretch")

      st.subheader("📊 Preview of States Dataset")
      st.dataframe(df_states)

    elif sde_option == "Union Territory Analysis":
      st.subheader("📈 Union Territory Accident Trend Comparison")
      opt = st.selectbox("Choose a chart", ["Line Graph", "Heatmap", "Bar Graph"])
      if opt == "Line Graph":
        st.subheader("Line graph view")
        fig = px.line(df_ut.reset_index(),
                      x='UTs', y=['2018','2019','2020','2021','2022'], markers=True)
        st.plotly_chart(fig, width="stretch")

      elif opt == "Heatmap":
        st.subheader("Heatmap view")
        fig2, ax = plt.subplots(figsize=(12, 6))
        fig = sns.heatmap(df_ut, cmap='Reds', ax=ax)
        st.pyplot(fig2)

      elif opt == "Bar Graph":
        st.subheader("Bar graph view")
        fig = px.bar(df_ut.reset_index(), x='UTs', y=['2018','2019','2020','2021','2022'],color='UTs', log_y=True)
        st.plotly_chart(fig, width="stretch")
      
      st.subheader("📊 Preview of Union Territories Dataset")
      st.dataframe(df_ut)
        
    st.markdown("""
    ### 🗂️ Dataset Source  
    The accident dataset used in this dashboard is sourced from **Data.gov.in**,  
    the official open data portal of the Government of India.  

    👉 **Source:** https://www.data.gov.in/  
    👉 **Department:** Ministry of Road Transport & Highways (MoRTH)  
    """)


## safe states and union territories
elif option == "Low-Accident Regions":
  opt = st.sidebar.selectbox("View", ["States", "Union Territories"])
  if opt == "States":
    st.title("10 States with the Lowest Accident Counts")
    top_state = df_states['Total_5yr'].sort_values(ascending=True).head(10).reset_index()
    top_state = top_state.rename(columns={'index':'state'}) 
    fig =px.bar(top_state, x='State', y='Total_5yr', color='State', log_y=True) 
    st.plotly_chart(fig, width="stretch")

  elif opt == "Union Territories":
      st.title("Union Territories with the Lowest Accident Counts")
      top_ut = df_ut['Total_5yr'].sort_values(ascending=True).reset_index()
      top_ut = top_ut.rename(columns={'index':'UT'}) 
      fig =px.bar(top_ut, x='UTs', y='Total_5yr', color='UTs', log_y=True) 
      st.plotly_chart(fig, width="stretch")
  
  st.markdown("""
  ### 🛡️ About the Safest States & Union Territories
  The regions listed here have recorded the **lowest number of road accidents** from **2018 to 2022**.  
  These low accident counts are generally influenced by factors such as:

  - Smaller population size  
  - Lower vehicle density  
  - Fewer highways and major roads  
  - Better compliance with traffic rules  
  - Limited commercial or heavy-vehicle movement

  Safe Union Territories (like **Lakshadweep**, **Daman & Diu**, **Andaman & Nicobar Islands**)  
  are especially low-risk due to their size and controlled transportation systems.

  These places represent the **lowest accident-prone regions** in India based on the dataset.
  """)


## Dangerous states and union terr.
elif option == "High-Accident Regions":
  opt_2 = st.sidebar.selectbox("View", ["States", "Union Territories"])
  # for state
  if opt_2 == "States":
    st.title("10 States with the Highest Accident Counts")
    least_state = df_states['Total_5yr'].sort_values(ascending=False).head(10).reset_index()
    least_state = least_state.rename(columns={'index':'state'}) 
    fig =px.bar(least_state, x='State', y='Total_5yr', color='State', log_y=True) 
    st.plotly_chart(fig, width="stretch")

  # for union territory 
  elif opt_2 == "Union Territories":
      st.title("Union Territories with the Highest Accident Counts")
      least = df_ut['Total_5yr'].sort_values(ascending=False).reset_index()
      least = least.rename(columns={'index':'UT'}) 
      fig =px.bar(least, x='UTs', y='Total_5yr', color='UTs', log_y=True) 
      st.plotly_chart(fig, width="stretch")
  
  st.markdown("""
  ## ⚠️ High-Accident States & Union Territories (2018–2022)

  Some regions in India consistently report **high accident numbers**, making them statistically
  more **accident-prone** during the 5-year period from **2018 to 2022**.

  ---

  ### 🔥 What Makes a State or UT High-Risk?
  Areas with high accident counts generally have:

  - Large & dense populations  
  - Heavy commercial vehicle traffic  
  - Multiple national highways & expressways  
  - Fast urbanization  
  - High registered vehicle volume  
  - Congested road networks  

  These factors significantly increase the probability of road accidents.

  ---

  ### 🚨 High-Accident States
  States that frequently appear at the **top of accident statistics** include:

  - Tamil Nadu  
  - Karnataka  
  - Madhya Pradesh  
  - Maharashtra  
  - Uttar Pradesh  

  These states have high mobility, dense traffic flow, industrial zones, and urban hubs —  
  leading to **high accident risk**.

  ---

  ### 🚨 High-Accident Union Territories
  Some UTs such as:

  - **Delhi**  
  - **Jammu & Kashmir**  
  - **Ladakh**  

  report a higher number of accidents compared to other UTs.

  This is due to:

  - Urban congestion (Delhi)  
  - Mountainous terrain (J&K, Ladakh)  
  - Tourism pressure  
  - Busy interstate transport routes  

  """)


## State to state comparison
elif option == "State Comparison":
  st.title("State Comparison")
  states = st.sidebar.multiselect("Select states:", df_states.index)

  if len(states) > 0:
        # select & transpose
        states_df = df_states.loc[states].T
        states_df = states_df.reset_index().rename(columns={'index': 'Year'})

        # melt into long format for plotly
        df_long = states_df.melt(id_vars='Year', var_name='State', value_name='Accidents')

        # plot line chart
        fig = px.line(
            df_long,
            x='Year',
            y='Accidents',
            color='State',
            markers=True,
            title="Accident Trends Across Selected States (2018–2022)", 
            log_y=True
        )

        st.plotly_chart(fig, width="stretch")
  else:
        st.warning("Please select at least one state to compare.")
  st.markdown("""
  ## 🔄 State vs State Comparison

  This section allows you to **compare multiple Indian states** based on their  
  year-wise accident trends from **2018 to 2022**.

  You can select any combination of states from the sidebar, and the dashboard will  
  visualize how accident counts have changed over the 5-year period.

  ### 🧩 What This Comparison Helps You Understand
  - How different states perform relative to each other  
  - Which states show continuous growth or decline in accidents  
  - The gap between high-accident and low-accident states  
  - Patterns across years like drops in 2020 (lockdown impact)  
  - Identify similar or contrasting accident trends  

  ### 📊 Visualization
  A dynamic **line chart** is shown where:
  - Each line represents a selected state  
  - The x-axis shows years (2018–2022)  
  - The y-axis shows accident counts  
  - Colors differentiate the states  
  - Hovering reveals exact yearly accident values  

  This makes it easy to compare multiple states at once and study their accident patterns visually.
  """)


## Union territorries to union territories comparison 
elif option == "Union Territory Comparison":
  st.title("Union Territories Comparison")
  union_t = st.sidebar.multiselect("Select union territories:", df_ut.index)
    
  if len(union_t) > 0:
        # select & transpose
        union_t_df = df_ut.loc[union_t].T
        union_t_df = union_t_df.reset_index().rename(columns={'index': 'Year'})

        # melt into long format for plotly
        df_long = union_t_df.melt(id_vars='Year', var_name='Union Territory', value_name='Accidents')

        # plot line chart
        fig = px.line(
            df_long,
            x='Year',
            y='Accidents',
            color='Union Territory',
            markers=True,
            title="Accident Trends Across Selected Union Territories (2018–2022)",
            log_y=True
        )

        st.plotly_chart(fig, width="stretch")

  else:
        st.warning("Please select at least one union territory to compare.")
  st.markdown("""
  ## 🔄 Union Terr. vs Union Terr Comparison

  This section allows you to **compare multiple Indian Union Terr.** based on their  
  year-wise accident trends from **2018 to 2022**.

  You can select any combination of Union Terr. from the sidebar, and the dashboard will  
  visualize how accident counts have changed over the 5-year period.

  ### 🧩 What This Comparison Helps You Understand
  - How different Union Terr perform relative to each other  
  - Which Union Terr show continuous growth or decline in accidents  
  - The gap between high-accident and low-accident Union Terr.
  - Patterns across years like drops in 2020 (lockdown impact)  
  - Identify similar or contrasting accident trends  

  ### 📊 Visualization
  A dynamic **line chart** is shown where:
  - Each line represents a selected Union Terr.
  - The x-axis shows years (2018–2022)  
  - The y-axis shows accident counts
  - Colors differentiate the Union Terr.
  - Hovering reveals exact yearly accident values  

  This makes it easy to compare multiple Union Terr. at once and study their accident patterns visually.
  """)

st.markdown(
    f"""
    <div class='footer-note'>
        Designed and developed by <strong>{CREATOR_NAME}</strong>. {PROJECT_NAME} is a personal
        dashboard built with Streamlit, pandas, Plotly, matplotlib, and seaborn using public road
        accident data released by the Ministry of Road Transport & Highways.
    </div>
    """,
    unsafe_allow_html=True,
)
