"""Settings view - Application configuration and preferences."""
import streamlit as st
from state import init_state, get_state, set_state


def render() -> None:
    """Render the settings view.
    
    This view demonstrates:
    - Form-based configuration
    - State persistence for user preferences
    - Toggle switches and selections
    """
    st.title("⚙️ Application Settings")
    
    st.markdown(
        """
        Configure your application preferences. All settings are stored 
        in session state and persist across page navigation.
        """
    )
    
    # Initialize settings in state
    init_state("settings_theme", "Dark")
    init_state("settings_language", "English")
    init_state("settings_notifications", True)
    init_state("settings_auto_refresh", False)
    init_state("settings_items_per_page", 10)
    init_state("settings_username", "")
    
    # Display Settings Form
    st.markdown("---")
    st.subheader("🎨 Display Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        theme = st.selectbox(
            "Theme",
            ["Light", "Dark", "Auto"],
            index=["Light", "Dark", "Auto"].index(get_state("settings_theme", "Dark")),
            key="settings-theme-select"
        )
        if theme != get_state("settings_theme"):
            set_state("settings_theme", theme)
    
    with col2:
        language = st.selectbox(
            "Language",
            ["English", "Spanish", "French", "German", "Chinese"],
            index=["English", "Spanish", "French", "German", "Chinese"].index(
                get_state("settings_language", "English")
            ),
            key="settings-language-select"
        )
        if language != get_state("settings_language"):
            set_state("settings_language", language)
    
    items_per_page = st.slider(
        "Items per page",
        min_value=5,
        max_value=50,
        value=get_state("settings_items_per_page", 10),
        step=5,
        key="settings-items-slider"
    )
    if items_per_page != get_state("settings_items_per_page"):
        set_state("settings_items_per_page", items_per_page)
    
    # Notification Settings
    st.markdown("---")
    st.subheader("🔔 Notification Settings")
    
    notifications_enabled = st.toggle(
        "Enable Notifications",
        value=get_state("settings_notifications", True),
        key="settings-notifications-toggle"
    )
    if notifications_enabled != get_state("settings_notifications"):
        set_state("settings_notifications", notifications_enabled)
    
    auto_refresh = st.toggle(
        "Auto-refresh Data",
        value=get_state("settings_auto_refresh", False),
        key="settings-auto-refresh-toggle"
    )
    if auto_refresh != get_state("settings_auto_refresh"):
        set_state("settings_auto_refresh", auto_refresh)
    
    # User Profile
    st.markdown("---")
    st.subheader("👤 User Profile")
    
    username = st.text_input(
        "Username",
        value=get_state("settings_username", ""),
        placeholder="Enter your username",
        key="settings-username-input"
    )
    if username != get_state("settings_username"):
        set_state("settings_username", username)
    
    # Current Settings Summary
    st.markdown("---")
    st.subheader("📋 Current Settings Summary")
    
    settings_summary = f"""
    - **Theme:** {get_state("settings_theme", "Dark")}
    - **Language:** {get_state("settings_language", "English")}
    - **Items per page:** {get_state("settings_items_per_page", 10)}
    - **Notifications:** {"✅ Enabled" if get_state("settings_notifications", True) else "❌ Disabled"}
    - **Auto-refresh:** {"✅ Enabled" if get_state("settings_auto_refresh", False) else "❌ Disabled"}
    - **Username:** {get_state("settings_username", "") or "(not set)"}
    """
    
    st.markdown(settings_summary)
    
    st.info(
        "💡 **Tip:** Navigate to another page and come back. "
        "Your settings will be preserved!"
    )
    
    # Reset Settings
    st.markdown("---")
    if st.button("🔄 Reset All Settings", key="settings-reset", type="secondary"):
        set_state("settings_theme", "Dark")
        set_state("settings_language", "English")
        set_state("settings_notifications", True)
        set_state("settings_auto_refresh", False)
        set_state("settings_items_per_page", 10)
        set_state("settings_username", "")
        st.success("✅ All settings have been reset to defaults!")
        st.rerun()
