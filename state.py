"""State management utilities for the Streamlit application."""
from typing import Any
import streamlit as st


def init_state(key: str, default_value: Any) -> None:
    """Initialize a session state variable if it doesn't exist.
    
    Args:
        key: The session state key
        default_value: The default value to set if key doesn't exist
    """
    if key not in st.session_state:
        st.session_state[key] = default_value


def get_state(key: str, default_value: Any = None) -> Any:
    """Get a value from session state.
    
    Args:
        key: The session state key
        default_value: Default value if key doesn't exist
        
    Returns:
        The value from session state or default_value
    """
    return st.session_state.get(key, default_value)


def set_state(key: str, value: Any) -> None:
    """Set a value in session state.
    
    Args:
        key: The session state key
        value: The value to set
    """
    st.session_state[key] = value
