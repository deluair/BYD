import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
import os
from datetime import datetime, timedelta
import glob

# Configure Streamlit page
st.set_page_config(
    page_title="BYD Global Mobility Simulation Dashboard",
    page_icon="🔋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

class BYDDashboard:
    def __init__(self):
        self.data_path = "data"
        self.automotive_data = []
        self.battery_data = []
        self.financial_data = []
        self.load_data()
    
    def load_data(self):
        """Load simulation data from JSON files"""
        try:
            # Load automotive data
            automotive_files = glob.glob(os.path.join(self.data_path, "automotive_*.json"))
            for file in automotive_files:
                with open(file, 'r') as f:
                    data = json.load(f)
                    self.automotive_data.append(data)
            
            # Load battery data
            battery_files = glob.glob(os.path.join(self.data_path, "battery_*.json"))
            for file in battery_files:
                with open(file, 'r') as f:
                    data = json.load(f)
                    self.battery_data.append(data)
            
            # Load financial data
            financial_files = glob.glob(os.path.join(self.data_path, "financial_*.json"))
            for file in financial_files:
                with open(file, 'r') as f:
                    data = json.load(f)
                    self.financial_data.append(data)
                    
        except Exception as e:
            st.error(f"Error loading data: {str(e)}")
            # Generate sample data for demonstration
            self.generate_sample_data()
    
    def generate_sample_data(self):
        """Generate sample data for demonstration purposes"""
        dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
        
        # Sample automotive data
        for i, date in enumerate(dates):
            self.automotive_data.append({
                'date': date.isoformat(),
                'production': {
                    'Sedan': {'China': 15000 + i*500, 'Europe': 3000 + i*100, 'NorthAmerica': 2000 + i*80},
                    'SUV': {'China': 20000 + i*600, 'Europe': 4000 + i*150, 'NorthAmerica': 3000 + i*120},
                    'Truck': {'China': 8000 + i*300, 'Europe': 1500 + i*50, 'NorthAmerica': 2500 + i*100}
                },
                'sales': {
                    'Sedan': {'China': 14500 + i*480, 'Europe': 2900 + i*95, 'NorthAmerica': 1950 + i*75},
                    'SUV': {'China': 19500 + i*580, 'Europe': 3900 + i*140, 'NorthAmerica': 2900 + i*115},
                    'Truck': {'China': 7800 + i*290, 'Europe': 1450 + i*48, 'NorthAmerica': 2400 + i*95}
                },
                'market_share': np.random.uniform(0.15, 0.25),
                'customer_satisfaction': np.random.uniform(0.80, 0.95)
            })
        
        # Sample battery data
        for i, date in enumerate(dates):
            self.battery_data.append({
                'date': date.isoformat(),
                'production_data': {
                    'LFP_Blade': {'China': 8.5 + i*0.2, 'Europe': 1.2 + i*0.05, 'NorthAmerica': 0.8 + i*0.03},
                    'NMC': {'China': 2.1 + i*0.1, 'Europe': 0.4 + i*0.02, 'NorthAmerica': 0.25 + i*0.01},
                    'SolidState': {'China': 0.15 + i*0.01, 'Europe': 0.03 + i*0.002, 'NorthAmerica': 0.02 + i*0.001}
                },
                'financial_metrics': {
                    'revenue': 680000000 + i*15000000,
                    'raw_material_costs': 280000000 + i*8000000,
                    'gross_margin': np.random.uniform(0.55, 0.65)
                },
                'production_metrics': {
                    'capacity_utilization': {'LFP_Blade': np.random.uniform(0.85, 0.95), 'NMC': np.random.uniform(0.75, 0.90)},
                    'supply_chain_status': {'material_shortage_risk': np.random.uniform(0.1, 0.3)}
                }
            })
        
        # Sample financial data
        for i, date in enumerate(dates):
            self.financial_data.append({
                'date': date.isoformat(),
                'revenue': 2500000000 + i*50000000,
                'costs': 1800000000 + i*35000000,
                'profit': 700000000 + i*15000000,
                'cash_position': 15000000000 + i*100000000
            })
    
    def create_executive_summary(self):
        """Create executive summary with key metrics"""
        st.markdown('<div class="main-header">🔋 BYD Global Mobility Simulation Dashboard</div>', unsafe_allow_html=True)
        
        # Key Performance Indicators
        col1, col2, col3, col4 = st.columns(4)
        
        if self.financial_data:
            latest_financial = self.financial_data[-1]
            
            with col1:
                st.metric(
                    label="Monthly Revenue",
                    value=f"¥{latest_financial['revenue']/1e8:.1f}B",
                    delta=f"{((latest_financial['revenue']/self.financial_data[-2]['revenue'])-1)*100:.1f}%" if len(self.financial_data) > 1 else None
                )
            
            with col2:
                st.metric(
                    label="Net Profit",
                    value=f"¥{latest_financial['profit']/1e8:.1f}B",
                    delta=f"{((latest_financial['profit']/self.financial_data[-2]['profit'])-1)*100:.1f}%" if len(self.financial_data) > 1 else None
                )
            
            with col3:
                st.metric(
                    label="Cash Position",
                    value=f"¥{latest_financial['cash_position']/1e8:.1f}B",
                    delta=f"{((latest_financial['cash_position']/self.financial_data[-2]['cash_position'])-1)*100:.1f}%" if len(self.financial_data) > 1 else None
                )
        
        if self.automotive_data:
            latest_auto = self.automotive_data[-1]
            total_production = sum(sum(model.values()) for model in latest_auto['production'].values())
            
            with col4:
                st.metric(
                    label="Monthly Vehicle Production",
                    value=f"{total_production:,}",
                    delta=f"{latest_auto['market_share']*100:.1f}% Market Share"
                )
    
    def create_automotive_dashboard(self):
        """Create automotive division dashboard"""
        st.header("🚗 Automotive Division")
        
        if not self.automotive_data:
            st.warning("No automotive data available")
            return
        
        # Production trends
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Vehicle Production Trends")
            
            # Prepare data for plotting
            dates = [datetime.fromisoformat(d['date']) for d in self.automotive_data]
            
            fig = go.Figure()
            
            for model in ['Sedan', 'SUV', 'Truck']:
                production_data = []
                for data in self.automotive_data:
                    total = sum(data['production'][model].values()) if model in data['production'] else 0
                    production_data.append(total)
                
                fig.add_trace(go.Scatter(
                    x=dates,
                    y=production_data,
                    mode='lines+markers',
                    name=model,
                    line=dict(width=3)
                ))
            
            fig.update_layout(
                title="Monthly Vehicle Production by Model",
                xaxis_title="Date",
                yaxis_title="Units Produced",
                hovermode='x unified'
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("Regional Production Distribution")
            
            # Latest month regional data
            latest_data = self.automotive_data[-1]
            regional_totals = {'China': 0, 'Europe': 0, 'NorthAmerica': 0}
            
            for model in latest_data['production']:
                for region in regional_totals:
                    if region in latest_data['production'][model]:
                        regional_totals[region] += latest_data['production'][model][region]
            
            fig = px.pie(
                values=list(regional_totals.values()),
                names=list(regional_totals.keys()),
                title="Current Month Production by Region"
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        # Market performance metrics
        st.subheader("Market Performance")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Market share trend
            market_share_data = [d.get('market_share', 0) * 100 for d in self.automotive_data]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=dates,
                y=market_share_data,
                mode='lines+markers',
                name='Market Share',
                line=dict(color='green', width=3)
            ))
            
            fig.update_layout(
                title="Market Share Trend (%)",
                xaxis_title="Date",
                yaxis_title="Market Share (%)",
                yaxis=dict(range=[0, max(market_share_data) * 1.1])
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Customer satisfaction
            satisfaction_data = [d.get('customer_satisfaction', 0) * 100 for d in self.automotive_data]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=dates,
                y=satisfaction_data,
                mode='lines+markers',
                name='Customer Satisfaction',
                line=dict(color='orange', width=3)
            ))
            
            fig.update_layout(
                title="Customer Satisfaction (%)",
                xaxis_title="Date",
                yaxis_title="Satisfaction Score (%)",
                yaxis=dict(range=[70, 100])
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    def create_battery_dashboard(self):
        """Create battery division dashboard"""
        st.header("🔋 Battery Division")
        
        if not self.battery_data:
            st.warning("No battery data available")
            return
        
        # Battery production by technology
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Battery Production by Technology")
            
            dates = [datetime.fromisoformat(d['date']) for d in self.battery_data]
            
            fig = go.Figure()
            
            for tech in ['LFP_Blade', 'NMC', 'SolidState']:
                production_data = []
                for data in self.battery_data:
                    if 'production_data' in data and tech in data['production_data']:
                        total = sum(data['production_data'][tech].values())
                        production_data.append(total)
                    else:
                        production_data.append(0)
                
                fig.add_trace(go.Scatter(
                    x=dates,
                    y=production_data,
                    mode='lines+markers',
                    name=tech,
                    stackgroup='one'
                ))
            
            fig.update_layout(
                title="Monthly Battery Production (GWh)",
                xaxis_title="Date",
                yaxis_title="Production (GWh)"
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("Capacity Utilization")
            
            # Extract capacity utilization data
            utilization_data = []
            for data in self.battery_data:
                if 'production_metrics' in data and 'capacity_utilization' in data['production_metrics']:
                    avg_util = np.mean(list(data['production_metrics']['capacity_utilization'].values()))
                    utilization_data.append(avg_util * 100)
                else:
                    utilization_data.append(85)  # Default value
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=dates,
                y=utilization_data,
                mode='lines+markers',
                name='Capacity Utilization',
                line=dict(color='red', width=3),
                fill='tonexty'
            ))
            
            fig.update_layout(
                title="Average Capacity Utilization (%)",
                xaxis_title="Date",
                yaxis_title="Utilization (%)",
                yaxis=dict(range=[0, 100])
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        # Financial metrics
        st.subheader("Battery Division Financial Performance")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Revenue and costs
            revenue_data = []
            cost_data = []
            
            for data in self.battery_data:
                if 'financial_metrics' in data:
                    revenue_data.append(data['financial_metrics']['revenue'] / 1e8)  # Convert to billions
                    cost_data.append(data['financial_metrics']['raw_material_costs'] / 1e8)
                else:
                    revenue_data.append(6.8)
                    cost_data.append(2.8)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=dates, y=revenue_data, mode='lines+markers', name='Revenue', line=dict(color='green')))
            fig.add_trace(go.Scatter(x=dates, y=cost_data, mode='lines+markers', name='Raw Material Costs', line=dict(color='red')))
            
            fig.update_layout(
                title="Battery Division Revenue vs Costs (¥B)",
                xaxis_title="Date",
                yaxis_title="Amount (¥B)"
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Supply chain risk
            risk_data = []
            for data in self.battery_data:
                if 'production_metrics' in data and 'supply_chain_status' in data['production_metrics']:
                    risk = data['production_metrics']['supply_chain_status'].get('material_shortage_risk', 0.2)
                    risk_data.append(risk * 100)
                else:
                    risk_data.append(20)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=dates,
                y=risk_data,
                mode='lines+markers',
                name='Supply Chain Risk',
                line=dict(color='orange', width=3)
            ))
            
            fig.update_layout(
                title="Supply Chain Risk Score (%)",
                xaxis_title="Date",
                yaxis_title="Risk Score (%)",
                yaxis=dict(range=[0, 100])
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    def create_financial_dashboard(self):
        """Create financial dashboard"""
        st.header("💰 Financial Performance")
        
        if not self.financial_data:
            st.warning("No financial data available")
            return
        
        dates = [datetime.fromisoformat(d['date']) for d in self.financial_data]
        
        # Revenue and profit trends
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Revenue and Profit Trends")
            
            revenue_data = [d['revenue'] / 1e8 for d in self.financial_data]  # Convert to billions
            profit_data = [d['profit'] / 1e8 for d in self.financial_data]
            
            fig = make_subplots(specs=[[{"secondary_y": True}]])
            
            fig.add_trace(
                go.Scatter(x=dates, y=revenue_data, mode='lines+markers', name='Revenue', line=dict(color='blue')),
                secondary_y=False
            )
            
            fig.add_trace(
                go.Scatter(x=dates, y=profit_data, mode='lines+markers', name='Net Profit', line=dict(color='green')),
                secondary_y=True
            )
            
            fig.update_xaxes(title_text="Date")
            fig.update_yaxes(title_text="Revenue (¥B)", secondary_y=False)
            fig.update_yaxes(title_text="Net Profit (¥B)", secondary_y=True)
            
            fig.update_layout(title="Financial Performance Trends")
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("Cash Position")
            
            cash_data = [d['cash_position'] / 1e8 for d in self.financial_data]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=dates,
                y=cash_data,
                mode='lines+markers',
                name='Cash Position',
                line=dict(color='purple', width=3),
                fill='tonexty'
            ))
            
            fig.update_layout(
                title="Cash Position (¥B)",
                xaxis_title="Date",
                yaxis_title="Cash (¥B)"
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        # Profitability analysis
        st.subheader("Profitability Analysis")
        
        profit_margin = [(d['profit'] / d['revenue']) * 100 for d in self.financial_data]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=dates,
            y=profit_margin,
            mode='lines+markers',
            name='Profit Margin',
            line=dict(color='darkgreen', width=3)
        ))
        
        fig.update_layout(
            title="Profit Margin Trend (%)",
            xaxis_title="Date",
            yaxis_title="Profit Margin (%)"
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def run_dashboard(self):
        """Main dashboard runner"""
        # Sidebar navigation
        st.sidebar.title("Navigation")
        page = st.sidebar.selectbox(
            "Choose a dashboard:",
            ["Executive Summary", "Automotive Division", "Battery Division", "Financial Performance"]
        )
        
        # Data refresh button
        if st.sidebar.button("🔄 Refresh Data"):
            self.load_data()
            st.sidebar.success("Data refreshed!")
        
        # Display selected dashboard
        if page == "Executive Summary":
            self.create_executive_summary()
        elif page == "Automotive Division":
            self.create_automotive_dashboard()
        elif page == "Battery Division":
            self.create_battery_dashboard()
        elif page == "Financial Performance":
            self.create_financial_dashboard()
        
        # Footer
        st.sidebar.markdown("---")
        st.sidebar.markdown("**BYD Simulation Dashboard**")
        st.sidebar.markdown("Real-time business intelligence for BYD Global Mobility Simulation")

if __name__ == "__main__":
    dashboard = BYDDashboard()
    dashboard.run_dashboard()