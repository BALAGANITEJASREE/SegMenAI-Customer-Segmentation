"""
SegMenAI - Streamlit Application

Main frontend entrypoint for the customer segmentation dashboard.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import requests
import streamlit as st


# ============================================================
# PROJECT ROOT
# ============================================================

ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


# ============================================================
# THEME
# ============================================================

from frontend.theme import inject_base_styles


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SegMenAI | Customer Segmentation & Insights",
    page_icon=(
        str(ROOT_DIR / "assets" / "logo.png")
        if (ROOT_DIR / "assets" / "logo.png").exists()
        else "◎"
    ),
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# FASTAPI BACKEND URL
# ============================================================

API_URL = os.getenv(
    "SEGEMAI_API_URL",
    "http://127.0.0.1:8000",
).rstrip("/")


# ============================================================
# BACKEND HEALTH CHECK
# ============================================================

def check_backend_status() -> bool:
    """Return True when the FastAPI backend is available."""

    try:
        response = requests.get(
            f"{API_URL}/api/v1/health",
            timeout=2,
        )
        return response.status_code == 200

    except requests.RequestException:
        return False


backend_online = check_backend_status()


# ============================================================
# PAGE DEFINITIONS
# ============================================================

dashboard_page = st.Page(
    "pages/home.py",
    title="Dashboard",
    icon=":material/space_dashboard:",
    default=True,
)

segments_page = st.Page(
    "pages/customer_segmentation.py",
    title="Customer Segments",
    icon=":material/groups:",
)

analysis_page = st.Page(
    "pages/insights.py",
    title="Segment Analysis",
    icon=":material/query_stats:",
)

recommendations_page = st.Page(
    "pages/recommendations.py",
    title="Recommendations",
    icon=":material/tips_and_updates:",
)


# ============================================================
# NAVIGATION
# ============================================================

pg = st.navigation(
    [
        dashboard_page,
        segments_page,
        analysis_page,
        recommendations_page,
    ],
    position="hidden",
)


# ============================================================
# GLOBAL STYLES
# ============================================================

inject_base_styles()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    # --------------------------------------------------------
    # BRANDING
    # --------------------------------------------------------

    st.markdown(
        "## SegMenAI"
    )

    st.caption(
        "AI-Powered Customer Segmentation"
    )

    st.divider()

    # --------------------------------------------------------
    # NAVIGATION TITLE
    # --------------------------------------------------------

    st.markdown(
        "**NAVIGATION**"
    )

    # --------------------------------------------------------
    # NAVIGATION LINKS
    # --------------------------------------------------------

    st.page_link(
        dashboard_page,
        label="Dashboard",
        icon=":material/space_dashboard:",
    )

    st.page_link(
        segments_page,
        label="Customer Segments",
        icon=":material/groups:",
    )

    st.page_link(
        analysis_page,
        label="Segment Analysis",
        icon=":material/query_stats:",
    )

    st.page_link(
        recommendations_page,
        label="Recommendations",
        icon=":material/tips_and_updates:",
    )

    # --------------------------------------------------------
    # SPACING
    # --------------------------------------------------------

    st.markdown(
        "<br>",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # BACKEND STATUS
    # --------------------------------------------------------

    if backend_online:
        st.success(
            "Backend connected",
            icon="✅",
        )
    else:
        st.error(
            "Backend unavailable",
            icon="🔴",
        )


# ============================================================
# RUN APPLICATION
# ============================================================

pg.run()