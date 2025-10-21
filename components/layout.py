"""Layout component for consistent page structure across all views."""
from typing import Callable
import streamlit as st
from router import router


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


def render_breadcrumb_navigation() -> None:
    """Render vertical breadcrumb-style navigation below the header."""
    current_page = router.get_current_page()
    
    # Create a container for the breadcrumb navigation
    st.markdown(
        """
        <style>
        .breadcrumb-nav {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            padding: 1rem 0;
            border-bottom: 1px solid #2d3748;
            margin-bottom: 1.5rem;
        }
        .breadcrumb-item {
            display: flex;
            align-items: center;
            font-size: 0.95rem;
        }
        .breadcrumb-separator {
            color: #718096;
            margin: 0 0.5rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Create columns for the navigation buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button(
            "🏠 Home",
            key="nav-home",
            use_container_width=True,
            type="primary" if current_page == "home" else "secondary"
        ):
            router.navigate("home")
    
    with col2:
        if st.button(
            "📊 Reports",
            key="nav-reports",
            use_container_width=True,
            type="primary" if current_page == "reports" else "secondary"
        ):
            router.navigate("reports")
    
    with col3:
        if st.button(
            "⚙️ Settings",
            key="nav-settings",
            use_container_width=True,
            type="primary" if current_page == "settings" else "secondary"
        ):
            router.navigate("settings")


def render_sidebar() -> None:
    """Render the sidebar with information."""
    with st.sidebar:
        st.markdown("### 📖 About")
        st.markdown(
            """
            This is a demonstration of an MVC-style layout in Streamlit.
            
            **Features:**
            - Reusable layout component
            - State preservation
            - Query parameter routing
            - Modular view structure
            - Breadcrumb-style navigation
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
    
    This function provides a consistent layout structure with header, 
    breadcrumb navigation, sidebar, and footer, while accepting a callback 
    to render the main content area.
    
    Args:
        render_main: A callable that renders the main content area
    """
    # Set page config (must be first Streamlit command)
    # Note: This is typically done in app.py, but included here for reference
    
    # Render the fixed components
    render_header()
    render_breadcrumb_navigation()
    render_sidebar()
    
    # Render the swappable main content
    st.markdown("<div id='main-content'>", unsafe_allow_html=True)
    render_main()
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Render footer
    render_footer()
