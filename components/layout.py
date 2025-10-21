"""Layout component for consistent page structure across all views."""
from typing import Callable
import streamlit as st
from router import router


NAV_ITEMS = [
    {"name": "home", "label": "Home", "icon": "🏠"},
    {"name": "reports", "label": "Reports", "icon": "📊"},
    {"name": "settings", "label": "Settings", "icon": "⚙️"},
]


def render_header() -> None:
    """Render the application header."""
    st.markdown(
        """
        <div style="background-color: #0e1117; padding: 1rem; border-bottom: 2px solid #ff4b4b;">
            <h1 style="color: #ff4b4b; margin: 0;">🎯 Streamlit MVC Demo</h1>
            <p style="color: #fafafa; margin: 0.5rem 0 0 0;">
                Proof of Concept: Layout with Swappable Views
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_navigation() -> None:
    """Render a horizontal navigation bar between header and main content."""
    current_page = router.get_current_page()

    # Inject lightweight styling to keep the nav visually anchored beneath the header.
    st.markdown(
        """
        <style>
            .streamlight-horizontal-nav {
                background-color: #0e1117;
                border-bottom: 1px solid #1f2129;
                padding: 0.75rem 0.5rem;
                margin-bottom: 1.5rem;
            }
            .streamlight-horizontal-nav .stButton>button {
                background-color: #1f232b;
                border: 1px solid #30343d;
                color: #fafafa;
            }
            .streamlight-horizontal-nav .stButton>button:hover {
                border-color: #ff4b4b;
                color: #ff4b4b;
            }
            .streamlight-horizontal-nav .stButton>button[kind="primary"] {
                background: linear-gradient(90deg, #ff4b4b 0%, #ff6f6f 100%);
                border: none;
                color: #0e1117;
            }
            .streamlight-horizontal-nav .stButton>button[kind="primary"]:hover {
                opacity: 0.9;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    with st.container():
        st.markdown('<div class="streamlight-horizontal-nav">', unsafe_allow_html=True)

        columns = st.columns(len(NAV_ITEMS), gap="medium")
        for column, item in zip(columns, NAV_ITEMS):
            is_current = current_page == item["name"]
            button_type = "primary" if is_current else "secondary"

            with column:
                if st.button(
                    f"{item['icon']} {item['label']}",
                    key=f"nav-horizontal-{item['name']}",
                    use_container_width=True,
                    type=button_type,
                ):
                    router.navigate(item["name"])

        st.markdown('</div>', unsafe_allow_html=True)


def render_about_panel() -> None:
    """Render an about panel beneath the navigation bar."""
    with st.expander("About this demo", expanded=False):
        st.markdown(
            """
            This is a demonstration of an MVC-style layout in Streamlit.

            **Features:**
            - Horizontal navigation with query-parameter routing
            - Reusable layout component
            - State preservation across navigation
            - Modular view structure
            """
        )


def render_footer() -> None:
    """Render the application footer."""
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; color: #808495; padding: 1rem;">
            <p>Built with Streamlit | MVC Pattern Demo | 2024</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def layout(render_main: Callable[[], None]) -> None:
    """Main layout component that wraps all views.

    Provides a consistent layout structure with header, horizontal navigation,
    optional about panel, and footer while accepting a callback to render the
    main content area.

    Args:
        render_main: A callable that renders the main content area
    """
    # Render the fixed components
    render_header()
    render_navigation()
    render_about_panel()

    # Render the swappable main content
    st.markdown("<div id='main-content'>", unsafe_allow_html=True)
    render_main()
    st.markdown("</div>", unsafe_allow_html=True)

    # Render footer
    render_footer()
