# Streamlit MVC Demo

A proof-of-concept Streamlit application demonstrating an MVC (Model-View-Controller) style architecture with reusable layouts, modular views, and state management.

## Features

- ✅ **Reusable Layout Component**: Single layout definition with header, horizontal navigation, and footer
- ✅ **Modular Views**: Independent view modules with typed `render()` functions
- ✅ **Query Parameter Routing**: Navigate using URLs like `?page=reports`
- ✅ **State Persistence**: User state preserved across view navigation
- ✅ **No Code Duplication**: Layout code written once, reused everywhere
- ✅ **Clean Architecture**: Separation of concerns with dedicated modules

## Project Structure

```text
StreamlightUI/
├── app.py                    # Main entrypoint
├── router.py                 # Routing logic with query params
├── state.py                  # State management utilities
├── components/
│   └── layout.py            # Reusable layout component
├── views/
│   ├── home.py              # Home view
│   ├── reports.py           # Reports view with data visualization
│   └── settings.py          # Settings view
└── README.md                # This file
```

## Requirements

- Python ≥3.9
- Streamlit ≥1.24

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/WillCode4Food87/StreamlightUI.git
    cd StreamlightUI
    ```

1. Install dependencies:

    ```bash
    pip install streamlit
    ```

## Running the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## Usage

### Navigation

- Use the horizontal navigation bar beneath the header to switch between views
- Click **🏠 Home** to go to the landing page
- Click **📊 Reports** to view the reports dashboard
- Click **⚙️ Settings** to configure preferences

### Direct URL Access

You can navigate directly to specific pages using query parameters:

- Home: `http://localhost:8501/?page=home`
- Reports: `http://localhost:8501/?page=reports`
- Settings: `http://localhost:8501/?page=settings`

### State Persistence

Each view maintains its own state:

- **Home**: Try the counter demo - increment/decrement values persist when you navigate away and return
- **Reports**: Select chart types and data seeds - your selections are preserved
- **Settings**: Configure preferences - all settings persist across navigation

## Architecture

### Layout Component (`components/layout.py`)

The layout component provides a consistent structure across all pages:

- **Header**: Application title and description
- **Horizontal Navigation**: Primary view switching controls
- **About Panel**: Optional contextual information beneath the nav
- **Main Content**: Swappable area for view rendering
- **Footer**: Application footer

The layout accepts a `render_main` callback, allowing any view to be rendered in the main content area.

### Router (`router.py`)

The router manages:

- Route registration (mapping page names to render functions)
- Query parameter parsing
- Navigation between views
- Current page determination

### State Management (`state.py`)

Utility functions for working with Streamlit's session state:

- `init_state()`: Initialize state variables with defaults
- `get_state()`: Retrieve state values
- `set_state()`: Update state values

### Views (`views/`)

Each view is an independent module with a typed `render()` function:

- **home.py**: Landing page with state persistence demo
- **reports.py**: Data visualization with cached data generation
- **settings.py**: Configuration interface with form controls

## Design Patterns

### MVC Pattern

- **Model**: State management (`state.py`) and data generation (in views)
- **View**: Independent view modules (`views/*.py`)
- **Controller**: Router (`router.py`) and layout orchestration

### Separation of Concerns

- Layout logic is separate from view logic
- Routing is independent of view rendering
- State management is centralized and reusable

### No Code Duplication

- Layout code (header, navigation, footer) is written once in `components/layout.py`
- All views reuse the same layout without duplication
- Common utilities are centralized in `state.py`

## Extending the Application

### Adding a New View

1. Create a new file in `views/` (e.g., `views/analytics.py`)
1. Implement a `render()` function:

   ```python
   def render() -> None:
       """Render the analytics view."""
       st.title("📈 Analytics")
       # Your view code here
   ```

1. Register the route in `app.py`:

    ```python
    from views import analytics
    router.register("analytics", analytics.render)
    ```

1. Add a navigation button in the horizontal navigation bar inside `components/layout.py`

### Customizing the Layout

Edit `components/layout.py` to modify:

- Header styling and content
- Horizontal navigation behavior and styling
- About panel visibility and copy
- Footer content
- Overall page structure

### Adding State Variables

Use the state management utilities in your views:

```python
from state import init_state, get_state, set_state

# Initialize
init_state("my_variable", default_value)

# Read
value = get_state("my_variable")

# Update
set_state("my_variable", new_value)
```

## Constraints & Design Decisions

- **No External Dependencies**: Only Streamlit is required (no databases, APIs, or additional frameworks)
- **Type Hints**: All functions include type annotations for better code quality
- **Caching**: `st.cache_data` is used in reports view to avoid expensive re-computation
- **Keyboard-Safe IDs**: All widgets have explicit `key` parameters
- **Minimal Custom CSS**: Inline styles enhance the layout while staying dependency-free

## License

This is a demonstration project for educational purposes.

## Author

Built as a proof-of-concept for MVC-style architecture in Streamlit.
