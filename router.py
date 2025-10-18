"""Router module for handling page navigation and query parameters."""
from typing import Callable, Dict
import streamlit as st


class Router:
    """Simple router that maps page names to view render functions."""
    
    def __init__(self) -> None:
        """Initialize the router with an empty routes dictionary."""
        self.routes: Dict[str, Callable[[], None]] = {}
    
    def register(self, name: str, render_func: Callable[[], None]) -> None:
        """Register a route with a render function.
        
        Args:
            name: The route name (used in query params)
            render_func: The function to call to render this view
        """
        self.routes[name] = render_func
    
    def get_current_page(self) -> str:
        """Get the current page from query params or return default.
        
        Returns:
            The current page name
        """
        # Check query params first
        query_params = st.query_params
        page = query_params.get("page", "home")
        
        # Validate that page exists in routes
        if page not in self.routes:
            page = "home"
        
        return page
    
    def navigate(self, page: str) -> None:
        """Navigate to a different page by updating query params.
        
        Args:
            page: The page name to navigate to
        """
        if page in self.routes:
            st.query_params["page"] = page
            st.rerun()
    
    def render_current_page(self) -> None:
        """Render the current page based on query params."""
        current_page = self.get_current_page()
        render_func = self.routes.get(current_page)
        
        if render_func:
            render_func()
        else:
            st.error(f"Page '{current_page}' not found")


# Global router instance
router = Router()
