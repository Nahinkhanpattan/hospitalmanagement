import streamlit as st


def inject_responsive_css():
    """Injects responsive meta tag, CSS and a small JS helper to improve mobile rendering."""
    st.markdown(
        """
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
        input[type="text"], input[type="number"], select, textarea { width: 100% !important; box-sizing: border-box; }
        /* Make tables and dataframes scrollable horizontally */
        [data-testid="stTable"], [data-testid="stDataFrame"] { display:block; width:100%; overflow-x:auto; -webkit-overflow-scrolling:touch; }
        /* Ensure table content uses its natural width so the container can scroll */
        [data-testid="stDataFrame"] table, [data-testid="stTable"] table { width: max-content; border-collapse: collapse; }
        /* Prevent cell content from wrapping so horizontal scroll is used instead */
        [data-testid="stDataFrame"] thead th, [data-testid="stDataFrame"] tbody td, [data-testid="stTable"] th, [data-testid="stTable"] td { white-space: nowrap; }
        [data-testid="metric-container"] { min-width: 120px; }
        img { max-width: 100%; height: auto; }
        .stApp { padding: 0.5rem 1rem; }
        @media (max-width: 600px) {
            div[data-testid="column"] { width: 100% !important; min-width: 100% !important; }
            h1, h2, h3 { font-size: 1.2rem; }
            .stMetric-value { font-size: 1.2rem; }
            [data-testid="stTable"], [data-testid="stDataFrame"] { font-size: 0.9rem; }
        }
        </style>
        <script>
        (function(){
            // Add a "mobile" class to the document when width <= 600px so additional CSS can target it
            function syncMobileClass(){
                if(window.innerWidth <= 600) document.documentElement.classList.add('mobile');
                else document.documentElement.classList.remove('mobile');
            }
            window.addEventListener('resize', syncMobileClass);
            syncMobileClass();
        })();
        </script>
        """,
        unsafe_allow_html=True,
    )
