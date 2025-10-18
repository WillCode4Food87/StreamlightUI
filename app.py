"""Main application entrypoint for the Streamlit MVC demo.

This application demonstrates a Model-View-Controller (MVC) style pattern
in Streamlit with:
- Reusable layout components
- Query parameter-based routing
- State persistence across views
- Modular view architecture
"""
import streamlit as st
from components.layout import layout
from router import router
from views import home, reports, settings


def main() -> None:
    """Main application function.
    
    Sets up page configuration, registers routes, and renders the application
    using the layout component.
    """
    # Configure the Streamlit page
    st.set_page_config(
        page_title="Streamlit MVC Demo",
        page_icon="🎯",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Register all available routes
    router.register("home", home.render)
    router.register("reports", reports.render)
    router.register("settings", settings.render)
    
    # Render the application with layout
    layout(render_main=router.render_current_page)


if __name__ == "__main__":
    main()
