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


def render_sidebar() -> None:
    """Render the vertical breadcrumb-style navigation sidebar."""
    with st.sidebar:
        st.markdown("### 📋 Navigation Path")
        
        current_page = router.get_current_page()
        
        # Define navigation structure with hierarchy
        nav_items = [
            {"name": "home", "label": "Home", "icon": "🏠", "level": 0},
            {"name": "reports", "label": "Reports", "icon": "📊", "level": 1},
            {"name": "settings", "label": "Settings", "icon": "⚙️", "level": 1},
        ]
        
        # Render breadcrumb-style navigation
        for i, item in enumerate(nav_items):
            is_current = current_page == item["name"]
            is_before_current = False
            
            # Check if this item is before the current page in the path
            for j, check_item in enumerate(nav_items):
                if check_item["name"] == current_page and j > i:
                    is_before_current = True
                    break
            
            # Determine styling based on position relative to current page
            if is_current:
                # Current page - highlighted
                style_class = "breadcrumb-current"
                connector = "└─►"
            elif is_before_current:
                # Before current page in path - show as visited
                style_class = "breadcrumb-visited"
                connector = "├──"
            else:
                # After current page - show as available
                style_class = "breadcrumb-available"
                connector = "├──"
            
            # Add indentation for hierarchy levels
            indent = "　" * item["level"]  # Full-width space for alignment
            
            # Create the breadcrumb item with visual connector
            if i == 0:
                # First item (root) - no connector
                breadcrumb_label = f"{indent}{item['icon']} {item['label']}"
            else:
                # Subsequent items - show connector
                breadcrumb_label = f"{connector} {item['icon']} {item['label']}"
            
            # Render as clickable button with appropriate styling
            button_type = "primary" if is_current else "secondary"
            
            if st.button(
                breadcrumb_label,
                key=f"nav-breadcrumb-{item['name']}",
                use_container_width=True,
                type=button_type,
                disabled=is_current
            ):
                router.navigate(item["name"])
            
            # Add visual path indicator between items
            if i < len(nav_items) - 1 and not is_current:
                st.markdown(
                    '<div style="margin-left: 0px; color: #888; font-size: 1.2em;">│</div>',
                    unsafe_allow_html=True
                )
        
        st.markdown("---")
        st.markdown("### 📖 About")
        st.markdown(
            """
            This is a demonstration of an MVC-style layout in Streamlit.
            
            **Features:**
            - Vertical breadcrumb navigation
            - Reusable layout component
            - State preservation
            - Query parameter routing
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
    
    This function provides a consistent layout structure with header, 
    sidebar, and footer, while accepting a callback to render the 
    main content area.
    
    Args:
        render_main: A callable that renders the main content area
    """
    # Set page config (must be first Streamlit command)
    # Note: This is typically done in app.py, but included here for reference
    
    # Render the fixed components
    render_header()
    render_sidebar()
    
    # Render the swappable main content
    st.markdown("<div id='main-content'>", unsafe_allow_html=True)
    render_main()
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Render footer
    render_footer()
