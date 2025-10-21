"""Home view - Landing page for the application."""
import streamlit as st
from state import init_state, get_state, set_state


def render() -> None:
    """Render the home view.
    
    This view demonstrates:
    - Basic content rendering
    - State persistence with a counter
    - Use of Streamlit widgets
    """
    st.title("🏠 Welcome to the Home Page")
    
    st.markdown(
        """
        This is the **Home** view of our Streamlit MVC demo. This page demonstrates:
        
        - ✅ Reusable layout components
        - ✅ Independent view modules
        - ✅ State persistence across page navigation
        - ✅ Query parameter routing
        
        ### Try the Demo
        
        Use the breadcrumb navigation at the top to switch between different views. Your state 
        will be preserved when you return to this page!
        """
    )
    
    # Demonstrate state persistence
    st.markdown("---")
    st.subheader("🔢 State Persistence Demo")
    
    # Initialize counter in session state
    init_state("home_counter", 0)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("➕ Increment", key="home-increment", use_container_width=True):
            current = get_state("home_counter", 0)
            set_state("home_counter", current + 1)
            st.rerun()
    
    with col2:
        if st.button("➖ Decrement", key="home-decrement", use_container_width=True):
            current = get_state("home_counter", 0)
            set_state("home_counter", current - 1)
            st.rerun()
    
    with col3:
        if st.button("🔄 Reset", key="home-reset", use_container_width=True):
            set_state("home_counter", 0)
            st.rerun()
    
    # Display counter
    counter_value = get_state("home_counter", 0)
    st.metric(
        label="Current Counter Value",
        value=counter_value,
        delta=None
    )
    
    st.info(
        "💡 **Tip:** Navigate to another page and come back. "
        "Your counter value will be preserved!"
    )
    
    # Additional info section
    st.markdown("---")
    st.subheader("📚 What's Next?")
    st.markdown(
        """
        - **Reports Page:** See data visualization examples
        - **Settings Page:** Configure application preferences
        
        Each view is an independent module with its own `render()` function!
        """
    )
