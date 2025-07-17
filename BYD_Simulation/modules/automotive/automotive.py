import json
import math
import random
import numpy as np
import pandas as pd
from datetime import datetime
from scipy import stats
from sklearn.linear_model import LinearRegression

class AutomotiveModule:
    def __init__(self, simulation_data):
        self.simulation_data = simulation_data
        self.config = simulation_data['config']
        
        # Enhanced automotive data structure
        self.automotive_data = {
            'production': {},
            'sales': {},
            'inventory': {},
            'capacity_utilization': {},
            'market_share': {},
            'pricing': {},
            'demand_forecast': {},
            'production_efficiency': {},
            'quality_metrics': {},
            'customer_satisfaction': {}
        }
        
        # Production capacity by region (annual units)
        self.production_capacity = {
            'China': 3500000,
            'Europe': 150000,
            'NorthAmerica': 100000,
            'SoutheastAsia': 200000,
            'LatinAmerica': 50000,
            'MiddleEast': 30000
        }
        
        # Market dynamics and competitive landscape
        self.market_dynamics = {
            'competitors': {
                'Tesla': {'market_share': 0.18, 'price_competitiveness': 0.85},
                'Volkswagen': {'market_share': 0.12, 'price_competitiveness': 0.90},
                'NIO': {'market_share': 0.08, 'price_competitiveness': 0.88},
                'XPeng': {'market_share': 0.06, 'price_competitiveness': 0.92},
                'Li Auto': {'market_share': 0.05, 'price_competitiveness': 0.89}
            },
            'market_growth_rates': {},
            'price_sensitivity': {},
            'brand_perception': 0.78
        }
        
        # Initialize demand models
        self.demand_models = {}
        self.historical_data = []
        
        self.initialize()

    def initialize(self):
        """Initialize automotive module with enhanced data structures"""
        regions = list(self.config['regions'].keys())
        models = list(self.config['vehicle_models'].keys())
        
        for model in models:
            self.automotive_data['production'][model] = {region: 0 for region in regions}
            self.automotive_data['sales'][model] = {region: 0 for region in regions}
            self.automotive_data['inventory'][model] = {region: 0 for region in regions}
            self.automotive_data['pricing'][model] = {region: 0 for region in regions}
            self.automotive_data['demand_forecast'][model] = {region: 0 for region in regions}
            
        for region in regions:
            self.automotive_data['capacity_utilization'][region] = 0.0
            self.automotive_data['market_share'][region] = 0.0
            self.automotive_data['production_efficiency'][region] = 0.85
            self.automotive_data['quality_metrics'][region] = 0.92
            self.automotive_data['customer_satisfaction'][region] = 0.88
            
        # Initialize market growth rates
        for region in regions:
            self.market_dynamics['market_growth_rates'][region] = self.config['regions'][region]['gdp_growth'] * 2.5
            self.market_dynamics['price_sensitivity'][region] = abs(self.config['market_dynamics']['price_elasticity'])
            
        # Initialize demand models for each model-region combination
        self._initialize_demand_models()
        
    def _initialize_demand_models(self):
        """Initialize AI-based demand forecasting models"""
        regions = list(self.config['regions'].keys())
        models = list(self.config['vehicle_models'].keys())
        
        for model in models:
            self.demand_models[model] = {}
            for region in regions:
                # Simple linear regression model for demand forecasting
                self.demand_models[model][region] = LinearRegression()
                
                # Generate initial training data (synthetic historical data)
                months = np.arange(1, 25)  # 24 months of history
                base_demand = self._calculate_base_demand(model, region)
                
                # Add seasonality and trend
                seasonal_pattern = np.array(self.config['market_dynamics']['seasonality_factors'])
                seasonal_demand = np.tile(seasonal_pattern, 2)[:24]
                
                trend = np.linspace(0.9, 1.1, 24)
                noise = np.random.normal(0, 0.1, 24)
                
                historical_demand = base_demand * seasonal_demand * trend * (1 + noise)
                
                # Features: month, trend, seasonality, economic factors
                X = np.column_stack([
                    months,
                    np.sin(2 * np.pi * months / 12),  # Seasonality
                    np.cos(2 * np.pi * months / 12),
                    np.ones(24) * self.config['regions'][region]['gdp_growth'],
                    np.ones(24) * self.config['regions'][region]['ev_adoption_rate']
                ])
                
                self.demand_models[model][region].fit(X, historical_demand)
                
    def _calculate_base_demand(self, model, region):
        """Calculate base monthly demand for a model in a region"""
        region_config = self.config['regions'][region]
        model_config = self.config['vehicle_models'][model]
        
        # Market size adjusted for EV adoption and segment appeal
        segment_appeal = {
            'A': 0.35, 'B': 0.25, 'C': 0.20, 'D': 0.10,
            'SUV': 0.15, 'Compact_SUV': 0.30, 'Mid_SUV': 0.20
        }
        
        monthly_market = region_config['market_size'] / 12
        ev_market = monthly_market * region_config['ev_adoption_rate']
        segment_market = ev_market * segment_appeal.get(model_config['segment'], 0.15)
        
        # BYD's potential market share (starts conservative, grows with brand strength)
        byd_potential_share = min(0.25, 0.05 + self.market_dynamics['brand_perception'] * 0.25)
        
        base_demand = segment_market * byd_potential_share
        return max(100, base_demand)  # Minimum 100 units per month

    def update_production(self):
        """Advanced production planning with demand forecasting and optimization"""
        current_date = self.simulation_data['current_date']
        regions = list(self.config['regions'].keys())
        models = list(self.config['vehicle_models'].keys())
        
        # Update demand forecasts first
        self._update_demand_forecasts()
        
        # Calculate monthly production capacity for each region
        monthly_capacity = {}
        for region in regions:
            base_capacity = self.production_capacity[region] / 12
            efficiency = self.automotive_data['production_efficiency'][region]
            seasonal_factor = self.config['market_dynamics']['seasonality_factors'][current_date.month - 1]
            
            # Apply efficiency and seasonal adjustments
            monthly_capacity[region] = int(base_capacity * efficiency * seasonal_factor)
            
        # Optimize production allocation using demand forecasts
        self._optimize_production_allocation(monthly_capacity)
        
        # Update inventory levels
        self._update_inventory()
        
        # Calculate capacity utilization
        self._calculate_capacity_utilization(monthly_capacity)
        
        # Update pricing based on demand-supply dynamics
        self._update_dynamic_pricing()
        
        self.log_data()
        self.update_sales()
        
    def _update_demand_forecasts(self):
        """Update demand forecasts using AI models"""
        current_date = self.simulation_data['current_date']
        month_number = (current_date.year - 2025) * 12 + current_date.month
        
        regions = list(self.config['regions'].keys())
        models = list(self.config['vehicle_models'].keys())
        
        for model in models:
            for region in regions:
                # Prepare features for prediction
                features = np.array([[
                    month_number,
                    np.sin(2 * np.pi * current_date.month / 12),
                    np.cos(2 * np.pi * current_date.month / 12),
                    self.config['regions'][region]['gdp_growth'],
                    self.config['regions'][region]['ev_adoption_rate']
                ]])
                
                # Predict demand
                predicted_demand = self.demand_models[model][region].predict(features)[0]
                
                # Apply market dynamics adjustments
                market_growth = self.market_dynamics['market_growth_rates'][region]
                competition_factor = 1.0 - sum(comp['market_share'] for comp in self.market_dynamics['competitors'].values()) * 0.1
                
                adjusted_demand = predicted_demand * (1 + market_growth/12) * competition_factor
                
                # Add stochastic variation
                noise_factor = 1 + np.random.normal(0, 0.05)
                final_demand = max(50, adjusted_demand * noise_factor)
                
                self.automotive_data['demand_forecast'][model][region] = int(final_demand)
                
    def _optimize_production_allocation(self, monthly_capacity):
        """Optimize production allocation across models and regions"""
        regions = list(self.config['regions'].keys())
        models = list(self.config['vehicle_models'].keys())
        
        for region in regions:
            total_demand = sum(self.automotive_data['demand_forecast'][model][region] for model in models)
            available_capacity = monthly_capacity[region]
            
            if total_demand <= available_capacity:
                # Sufficient capacity - produce to meet demand
                for model in models:
                    self.automotive_data['production'][model][region] = self.automotive_data['demand_forecast'][model][region]
            else:
                # Capacity constraint - prioritize by profitability
                model_priorities = []
                for model in models:
                    model_config = self.config['vehicle_models'][model]
                    margin = model_config['target_margin']
                    demand = self.automotive_data['demand_forecast'][model][region]
                    priority_score = margin * demand
                    model_priorities.append((model, priority_score, demand))
                
                # Sort by priority (highest margin * demand first)
                model_priorities.sort(key=lambda x: x[1], reverse=True)
                
                remaining_capacity = available_capacity
                for model, _, demand in model_priorities:
                    allocated = min(demand, remaining_capacity)
                    self.automotive_data['production'][model][region] = allocated
                    remaining_capacity -= allocated
                    
                    if remaining_capacity <= 0:
                        break
                        
                # Set remaining models to 0 if no capacity left
                for model, _, _ in model_priorities:
                    if model not in [m[0] for m in model_priorities[:len([m for m in model_priorities if remaining_capacity > 0])]]:
                        self.automotive_data['production'][model][region] = 0
                        
    def _update_inventory(self):
        """Update inventory levels based on production and previous sales"""
        regions = list(self.config['regions'].keys())
        models = list(self.config['vehicle_models'].keys())
        
        for model in models:
            for region in regions:
                # Add production to inventory
                self.automotive_data['inventory'][model][region] += self.automotive_data['production'][model][region]
                
                # Subtract previous month's sales (if any)
                # This will be properly updated in update_sales method
                
    def _calculate_capacity_utilization(self, monthly_capacity):
        """Calculate capacity utilization for each region"""
        regions = list(self.config['regions'].keys())
        models = list(self.config['vehicle_models'].keys())
        
        for region in regions:
            total_production = sum(self.automotive_data['production'][model][region] for model in models)
            if monthly_capacity[region] > 0:
                utilization = total_production / monthly_capacity[region]
                self.automotive_data['capacity_utilization'][region] = min(1.0, utilization)
            else:
                self.automotive_data['capacity_utilization'][region] = 0.0
                
    def _update_dynamic_pricing(self):
        """Update pricing based on demand-supply dynamics"""
        regions = list(self.config['regions'].keys())
        models = list(self.config['vehicle_models'].keys())
        
        for model in models:
            model_config = self.config['vehicle_models'][model]
            base_price = model_config['base_price_cny']
            
            for region in regions:
                demand = self.automotive_data['demand_forecast'][model][region]
                supply = self.automotive_data['production'][model][region] + self.automotive_data['inventory'][model][region]
                
                # Calculate demand-supply ratio
                if supply > 0:
                    ds_ratio = demand / supply
                else:
                    ds_ratio = 2.0  # High demand, no supply
                    
                # Price adjustment based on demand-supply dynamics
                if ds_ratio > 1.2:  # High demand
                    price_multiplier = 1.0 + min(0.15, (ds_ratio - 1.0) * 0.1)
                elif ds_ratio < 0.8:  # Low demand
                    price_multiplier = 1.0 - min(0.10, (1.0 - ds_ratio) * 0.1)
                else:
                    price_multiplier = 1.0
                    
                # Regional price adjustments
                regional_multipliers = {
                    'China': 1.0, 'Europe': 1.35, 'NorthAmerica': 1.45,
                    'SoutheastAsia': 1.15, 'LatinAmerica': 1.25, 'MiddleEast': 1.30
                }
                
                final_price = base_price * price_multiplier * regional_multipliers.get(region, 1.0)
                self.automotive_data['pricing'][model][region] = int(final_price)

    def update_sales(self):
        """Advanced sales simulation with market dynamics and customer behavior"""
        regions = list(self.config['regions'].keys())
        models = list(self.config['vehicle_models'].keys())
        
        for model in models:
            for region in regions:
                # Get forecasted demand
                demand = self.automotive_data['demand_forecast'][model][region]
                
                # Available inventory (production + existing inventory)
                available_inventory = self.automotive_data['inventory'][model][region]
                
                # Apply price elasticity effect
                current_price = self.automotive_data['pricing'][model][region]
                base_price = self.config['vehicle_models'][model]['base_price_cny']
                price_ratio = current_price / base_price if base_price > 0 else 1.0
                
                price_elasticity = self.config['market_dynamics']['price_elasticity']
                price_adjusted_demand = demand * (price_ratio ** price_elasticity)
                
                # Apply brand loyalty and market factors
                brand_loyalty = self.config['market_dynamics']['brand_loyalty']
                regulatory_support = self.config['regions'][region]['regulatory_support']
                infrastructure_factor = self.config['regions'][region]['charging_infrastructure']
                
                market_adjusted_demand = price_adjusted_demand * brand_loyalty * regulatory_support * infrastructure_factor
                
                # Competition impact
                total_competitor_share = sum(comp['market_share'] for comp in self.market_dynamics['competitors'].values())
                competition_factor = max(0.3, 1.0 - total_competitor_share * 0.5)
                
                final_demand = market_adjusted_demand * competition_factor
                
                # Sales are limited by available inventory
                actual_sales = min(int(final_demand), available_inventory)
                
                # Update sales and inventory
                self.automotive_data['sales'][model][region] = max(0, actual_sales)
                self.automotive_data['inventory'][model][region] = max(0, available_inventory - actual_sales)
                
        # Update market share and customer satisfaction
        self._update_market_metrics()
        
        self.log_sales()
        
    def _update_market_metrics(self):
        """Update market share and customer satisfaction metrics"""
        regions = list(self.config['regions'].keys())
        models = list(self.config['vehicle_models'].keys())
        
        for region in regions:
            # Calculate BYD's market share in the region
            total_byd_sales = sum(self.automotive_data['sales'][model][region] for model in models)
            market_size = self.config['regions'][region]['market_size'] / 12  # Monthly market
            ev_market = market_size * self.config['regions'][region]['ev_adoption_rate']
            
            if ev_market > 0:
                market_share = min(0.5, total_byd_sales / ev_market)  # Cap at 50%
                self.automotive_data['market_share'][region] = market_share
                
                # Update brand perception based on market performance
                if market_share > 0.15:
                    self.market_dynamics['brand_perception'] = min(0.95, self.market_dynamics['brand_perception'] + 0.001)
                elif market_share < 0.05:
                    self.market_dynamics['brand_perception'] = max(0.5, self.market_dynamics['brand_perception'] - 0.001)
                    
            # Update customer satisfaction based on quality and pricing
            avg_quality = self.automotive_data['quality_metrics'][region]
            avg_price_competitiveness = self._calculate_price_competitiveness(region)
            
            satisfaction = (avg_quality * 0.6 + avg_price_competitiveness * 0.4)
            self.automotive_data['customer_satisfaction'][region] = satisfaction
            
    def _calculate_price_competitiveness(self, region):
        """Calculate price competitiveness compared to competitors"""
        models = list(self.config['vehicle_models'].keys())
        
        total_competitiveness = 0
        model_count = 0
        
        for model in models:
            byd_price = self.automotive_data['pricing'][model][region]
            
            # Estimate competitor prices (simplified)
            segment = self.config['vehicle_models'][model]['segment']
            competitor_price_multipliers = {
                'A': 1.1, 'B': 1.15, 'C': 1.2, 'D': 1.25,
                'SUV': 1.3, 'Compact_SUV': 1.2, 'Mid_SUV': 1.25
            }
            
            estimated_competitor_price = byd_price * competitor_price_multipliers.get(segment, 1.2)
            
            if estimated_competitor_price > 0:
                competitiveness = min(1.0, estimated_competitor_price / byd_price)
                total_competitiveness += competitiveness
                model_count += 1
                
        return total_competitiveness / model_count if model_count > 0 else 0.8

    def log_sales(self):
        """Log comprehensive sales data"""
        log_entry = {
            'timestamp': self.simulation_data['current_date'].isoformat(),
            'type': 'Sales',
            'data': {
                'sales': self.automotive_data['sales'],
                'inventory': self.automotive_data['inventory'],
                'market_share': self.automotive_data['market_share'],
                'customer_satisfaction': self.automotive_data['customer_satisfaction'],
                'pricing': self.automotive_data['pricing']
            }
        }
        log_path = f"data/sales_{self.simulation_data['current_date'].strftime('%Y%m')}.json"
        with open(log_path, 'w') as f:
            json.dump(log_entry, f, indent=4)

    def log_data(self):
        """Log comprehensive production and operational data"""
        log_entry = {
            'timestamp': self.simulation_data['current_date'].isoformat(),
            'type': 'Production',
            'data': {
                'production': self.automotive_data['production'],
                'demand_forecast': self.automotive_data['demand_forecast'],
                'capacity_utilization': self.automotive_data['capacity_utilization'],
                'production_efficiency': self.automotive_data['production_efficiency'],
                'quality_metrics': self.automotive_data['quality_metrics'],
                'brand_perception': self.market_dynamics['brand_perception']
            }
        }
        log_path = f"data/production_{self.simulation_data['current_date'].strftime('%Y%m')}.json"
        with open(log_path, 'w') as f:
            json.dump(log_entry, f, indent=4)
            
    def get_production(self, model=None, region=None):
        """Get production data with enhanced filtering"""
        if model and region:
            return self.automotive_data['production'][model][region]
        elif model:
            return self.automotive_data['production'][model]
        return self.automotive_data['production']
        
    def get_sales(self, model=None, region=None):
        """Get sales data with enhanced filtering"""
        if model and region:
            return self.automotive_data['sales'][model][region]
        elif model:
            return self.automotive_data['sales'][model]
        return self.automotive_data['sales']
        
    def get_market_metrics(self):
        """Get comprehensive market performance metrics"""
        # Calculate weighted average market share across all regions
        total_market_share = 0
        total_weight = 0
        
        for region, share in self.automotive_data['market_share'].items():
            region_weight = self.config['regions'][region]['market_size']
            total_market_share += share * region_weight
            total_weight += region_weight
        
        avg_market_share = total_market_share / total_weight if total_weight > 0 else 0
        
        # Calculate average customer satisfaction
        avg_satisfaction = 0
        if self.automotive_data['customer_satisfaction']:
            satisfaction_values = list(self.automotive_data['customer_satisfaction'].values())
            avg_satisfaction = sum(satisfaction_values) / len(satisfaction_values)
        
        return {
            'market_share': avg_market_share,
            'customer_satisfaction': avg_satisfaction,
            'brand_perception': self.market_dynamics['brand_perception'],
            'capacity_utilization': self.automotive_data['capacity_utilization'],
            'production_efficiency': self.automotive_data['production_efficiency']
        }
        
    def get_financial_metrics(self):
        """Calculate financial metrics for the automotive division"""
        regions = list(self.config['regions'].keys())
        models = list(self.config['vehicle_models'].keys())
        
        total_revenue = 0
        total_units_sold = 0
        
        for model in models:
            for region in regions:
                units_sold = self.automotive_data['sales'][model][region]
                price = self.automotive_data['pricing'][model][region]
                revenue = units_sold * price
                total_revenue += revenue
                total_units_sold += units_sold
                
        avg_selling_price = total_revenue / total_units_sold if total_units_sold > 0 else 0
        
        return {
            'total_revenue': total_revenue,
            'total_units_sold': total_units_sold,
            'average_selling_price': avg_selling_price,
            'revenue_by_region': self._calculate_revenue_by_region(),
            'units_by_model': self._calculate_units_by_model()
        }
    
    def get_performance_metrics(self):
        """Get comprehensive performance metrics for integration with finance module"""
        financial_metrics = self.get_financial_metrics()
        market_metrics = self.get_market_metrics()
        
        return {
            'financial': financial_metrics,
            'market': market_metrics,
            'operational': {
                'capacity_utilization': self.automotive_data['capacity_utilization'],
                'production_efficiency': self.automotive_data['production_efficiency'],
                'quality_metrics': self.automotive_data['quality_metrics']
            }
        }
        
    def _calculate_revenue_by_region(self):
        """Calculate revenue breakdown by region"""
        regions = list(self.config['regions'].keys())
        models = list(self.config['vehicle_models'].keys())
        
        revenue_by_region = {}
        
        for region in regions:
            region_revenue = 0
            for model in models:
                units_sold = self.automotive_data['sales'][model][region]
                price = self.automotive_data['pricing'][model][region]
                region_revenue += units_sold * price
            revenue_by_region[region] = region_revenue
            
        return revenue_by_region
        
    def _calculate_units_by_model(self):
        """Calculate units sold breakdown by model"""
        regions = list(self.config['regions'].keys())
        models = list(self.config['vehicle_models'].keys())
        
        units_by_model = {}
        
        for model in models:
            model_units = sum(self.automotive_data['sales'][model][region] for region in regions)
            units_by_model[model] = model_units
            
        return units_by_model
