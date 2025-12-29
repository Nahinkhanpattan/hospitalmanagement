import streamlit as st


def inject_responsive_css():
    """Injects responsive meta tag, CSS and a small JS helper to improve mobile rendering."""
    st.markdown(
        """
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
        /* Make form controls full width so inputs are easy to tap on mobile */
        input[type="text"], input[type="number"], select, textarea {
            width: 100% !important;
            box-sizing: border-box;
        }

        /* Make tables horizontally scrollable on small screens */
        [data-testid="stTable"] { display:block; width:100%; overflow-x:auto; -webkit-overflow-scrolling:touch; }

        /* Ensure metrics are readable and can wrap */
        [data-testid="metric-container"] { min-width: 120px; }

        /* Make images responsive */
        img { max-width: 100%; height: auto; }

        /* General app padding adjustments */
        .stApp { padding: 0.5rem 1rem; }

        /* Responsive tweaks for narrow viewports */
        @media (max-width: 600px) {
            /* Column containers should stack vertically on small screens */
            div[data-testid="column"] { width: 100% !important; min-width: 100% !important; }
            /* Slightly smaller headings for mobile */
            h1, h2, h3 { font-size: 1.2rem; }
            .stMetric-value { font-size: 1.2rem; }
            /* Make sure tables don't overflow the viewport */
            [data-testid="stTable"] { font-size: 0.9rem; }
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
