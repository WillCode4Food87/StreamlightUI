"""Reports view - Data visualization and reporting page."""
import streamlit as st
from state import init_state, get_state, set_state
from datetime import datetime, timedelta
import random


@st.cache_data
def generate_sample_data(seed: int = 42) -> dict:
    """Generate sample data for the reports.
    
    Uses st.cache_data to avoid expensive re-computation on reruns.
    
    Args:
        seed: Random seed for reproducible data
        
    Returns:
        Dictionary containing sample report data
    """
    random.seed(seed)
    
    # Generate sample metrics
    dates = [(datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7, 0, -1)]
    values = [random.randint(50, 150) for _ in range(7)]
    
    return {
        "dates": dates,
        "values": values,
        "total": sum(values),
        "average": sum(values) / len(values),
        "max": max(values),
        "min": min(values)
    }


def render() -> None:
    """Render the reports view.
    
    This view demonstrates:
    - Data caching with st.cache_data
    - Chart rendering
    - Metric displays
    - State persistence for user selections
    """
    st.title("📊 Reports Dashboard")
    
    st.markdown(
        """
        This page demonstrates data visualization and state management 
        in a reports context.
        """
    )
    
    # Initialize report settings in state
    init_state("report_seed", 42)
    init_state("report_chart_type", "Line Chart")
    
    # Configuration section
    st.markdown("---")
    st.subheader("⚙️ Report Configuration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        chart_type = st.selectbox(
            "Select Chart Type",
            ["Line Chart", "Bar Chart", "Area Chart"],
            key="report-chart-type-select",
            index=["Line Chart", "Bar Chart", "Area Chart"].index(
                get_state("report_chart_type", "Line Chart")
            )
        )
        if chart_type != get_state("report_chart_type"):
            set_state("report_chart_type", chart_type)
    
    with col2:
        data_seed = st.number_input(
            "Data Seed (for regeneration)",
            min_value=1,
            max_value=1000,
            value=get_state("report_seed", 42),
            key="report-seed-input"
        )
        if data_seed != get_state("report_seed"):
            set_state("report_seed", data_seed)
    
    # Generate data
    data = generate_sample_data(seed=get_state("report_seed", 42))
    
    # Display metrics
    st.markdown("---")
    st.subheader("📈 Key Metrics")
    
    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
    
    with metric_col1:
        st.metric("Total", f"{data['total']}")
    
    with metric_col2:
        st.metric("Average", f"{data['average']:.1f}")
    
    with metric_col3:
        st.metric("Maximum", f"{data['max']}")
    
    with metric_col4:
        st.metric("Minimum", f"{data['min']}")
    
    # Display chart
    st.markdown("---")
    st.subheader(f"📊 {get_state('report_chart_type', 'Line Chart')}")
    
    chart_data = {"Date": data["dates"], "Value": data["values"]}
    
    current_chart_type = get_state("report_chart_type", "Line Chart")
    
    if current_chart_type == "Line Chart":
        st.line_chart(chart_data, x="Date", y="Value")
    elif current_chart_type == "Bar Chart":
        st.bar_chart(chart_data, x="Date", y="Value")
    else:  # Area Chart
        st.area_chart(chart_data, x="Date", y="Value")
    
    # Additional info
    st.info(
        "💡 **Tip:** Change the data seed or chart type, then navigate away and back. "
        "Your selections will be preserved!"
    )
    
    # Data table
    st.markdown("---")
    st.subheader("📋 Data Table")
    st.dataframe(chart_data, use_container_width=True)
