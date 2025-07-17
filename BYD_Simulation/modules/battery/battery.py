import json
import math
import numpy as np
import pandas as pd
import requests
from datetime import datetime
from scipy import stats
from sklearn.ensemble import RandomForestRegressor

class BatteryModule:
    def __init__(self, simulation_data):
        self.simulation_data = simulation_data
        self.config = simulation_data['config']
        
        # Enhanced battery data structure
        self.battery_data = {
            'production': {},
            'sales': {},
            'inventory': {},
            'capacity_utilization': {},
            'technology_advancement': {},
            'quality_metrics': {},
            'cost_structure': {},
            'supply_chain_risk': {},
            'customer_contracts': {},
            'research_pipeline': {}
        }
        
        # Production capacity by technology and region (GWh annually)
        self.production_capacity = {
            'LFP_Blade': {'China': 120, 'Europe': 15, 'NorthAmerica': 10, 'SoutheastAsia': 8},
            'NMC': {'China': 25, 'Europe': 5, 'NorthAmerica': 3, 'SoutheastAsia': 2},
            'SolidState': {'China': 2, 'Europe': 0.5, 'NorthAmerica': 0.3, 'SoutheastAsia': 0.2}
        }
        
        # Enhanced raw materials tracking
        self.raw_materials = {
            'lithium': {
                'current_price': 75000,  # CNY per ton
                'inventory_tons': 2500,
                'monthly_consumption': 180,
                'supplier_reliability': 0.92,
                'price_volatility': 0.25,
                'strategic_reserves': 1200
            },
            'cobalt': {
                'current_price': 55000,
                'inventory_tons': 800,
                'monthly_consumption': 45,
                'supplier_reliability': 0.88,
                'price_volatility': 0.30,
                'strategic_reserves': 400
            },
            'nickel': {
                'current_price': 25000,
                'inventory_tons': 3200,
                'monthly_consumption': 220,
                'supplier_reliability': 0.90,
                'price_volatility': 0.20,
                'strategic_reserves': 1600
            },
            'graphite': {
                'current_price': 8000,
                'inventory_tons': 1500,
                'monthly_consumption': 120,
                'supplier_reliability': 0.95,
                'price_volatility': 0.15,
                'strategic_reserves': 800
            }
        }
        
        # Customer portfolio and contracts
        self.customers = {
            'Internal_BYD': {'contract_gwh': 80, 'price_premium': 0.0, 'priority': 1},
            'Tesla': {'contract_gwh': 15, 'price_premium': 0.05, 'priority': 2},
            'Toyota': {'contract_gwh': 12, 'price_premium': 0.08, 'priority': 3},
            'Ford': {'contract_gwh': 10, 'price_premium': 0.06, 'priority': 4},
            'Volvo': {'contract_gwh': 8, 'price_premium': 0.10, 'priority': 5},
            'Spot_Market': {'contract_gwh': 25, 'price_premium': 0.15, 'priority': 6}
        }
        
        # Technology roadmap and R&D pipeline
        self.technology_roadmap = {
            'LFP_Blade_Gen2': {'readiness': 0.8, 'performance_improvement': 0.15, 'cost_reduction': 0.10},
            'LFP_Blade_Gen3': {'readiness': 0.4, 'performance_improvement': 0.25, 'cost_reduction': 0.18},
            'SolidState_Gen2': {'readiness': 0.3, 'performance_improvement': 0.40, 'cost_reduction': 0.05},
            'Sodium_Ion': {'readiness': 0.6, 'performance_improvement': -0.20, 'cost_reduction': 0.30}
        }
        
        # Market intelligence and forecasting models
        self.market_models = {}
        self.price_prediction_models = {}
        
        self.initialize()

    def initialize(self):
        # Initialize production tracking for each technology and region
        for tech in self.production_capacity:
            self.battery_data['production'][tech] = {}
            self.battery_data['sales'][tech] = {}
            self.battery_data['inventory'][tech] = {}
            self.battery_data['capacity_utilization'][tech] = {}
            
            for region in self.production_capacity[tech]:
                self.battery_data['production'][tech][region] = []
                self.battery_data['sales'][tech][region] = []
                self.battery_data['inventory'][tech][region] = []
                self.battery_data['capacity_utilization'][tech][region] = []
        
        # Initialize quality metrics
        self.battery_data['quality_metrics'] = {
            'defect_rate': [],
            'cycle_life_performance': [],
            'energy_density_achievement': [],
            'safety_incidents': [],
            'customer_satisfaction': []
        }
        
        # Initialize cost structure tracking
        self.battery_data['cost_structure'] = {
            'raw_materials': [],
            'manufacturing': [],
            'labor': [],
            'energy': [],
            'logistics': [],
            'overhead': []
        }
        
        # Initialize supply chain risk assessment
        self.battery_data['supply_chain_risk'] = {
            'material_shortage_risk': [],
            'price_volatility_impact': [],
            'supplier_performance': [],
            'logistics_disruption': [],
            'geopolitical_risk': []
        }
        
        # Initialize market intelligence models
        self._initialize_market_models()
        
        # Initialize raw material price prediction models
        self._initialize_price_models()
        
        # Set initial inventory levels (30 days of production)
        self._initialize_inventory()
        
        print(f"Battery module initialized with {len(self.customers)} customers and {len(self.raw_materials)} raw materials")
    
    def _initialize_market_models(self):
        """Initialize AI models for market demand forecasting"""
        # Create synthetic historical data for training
        np.random.seed(42)
        months = 24
        
        for tech in self.production_capacity:
            # Generate synthetic demand data with trends and seasonality
            time_trend = np.linspace(1, 2, months)
            seasonal = 1 + 0.1 * np.sin(2 * np.pi * np.arange(months) / 12)
            noise = np.random.normal(0, 0.05, months)
            
            base_demand = {
                'LFP_Blade': 8.0,  # GWh monthly
                'NMC': 2.5,
                'SolidState': 0.3
            }
            
            demand = base_demand[tech] * time_trend * seasonal * (1 + noise)
            
            # Features: month, trend, economic indicators, competition
            X = np.column_stack([
                np.arange(months),
                time_trend,
                seasonal,
                np.random.normal(1, 0.1, months),  # Economic factor
                np.random.normal(0.8, 0.05, months)  # Competition factor
            ])
            
            # Train Random Forest model
            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model.fit(X, demand)
            self.market_models[tech] = model
    
    def _initialize_price_models(self):
        """Initialize models for raw material price prediction"""
        np.random.seed(42)
        months = 36
        
        for material in self.raw_materials:
            # Generate synthetic price data with volatility
            base_price = self.raw_materials[material]['current_price']
            volatility = self.raw_materials[material]['price_volatility']
            
            # Random walk with mean reversion
            prices = [base_price]
            for _ in range(months - 1):
                change = np.random.normal(0, volatility * base_price * 0.01)
                mean_reversion = -0.1 * (prices[-1] - base_price)
                new_price = prices[-1] + change + mean_reversion
                prices.append(max(new_price, base_price * 0.3))  # Floor price
            
            # Features: time, previous prices, market indicators
            X = np.column_stack([
                np.arange(months),
                prices,
                np.random.normal(1, 0.1, months),  # Supply factor
                np.random.normal(1, 0.1, months)   # Demand factor
            ])
            
            # Predict next month's price (shifted target)
            y = prices[1:] + [prices[-1]]  # Simple forward shift
            
            model = RandomForestRegressor(n_estimators=50, random_state=42)
            model.fit(X[:-1], y[:-1])
            self.price_prediction_models[material] = model
    
    def _initialize_inventory(self):
        """Set initial inventory levels based on production capacity"""
        for tech in self.production_capacity:
            for region in self.production_capacity[tech]:
                # 30 days of production as initial inventory
                monthly_capacity = self.production_capacity[tech][region] / 12
                initial_inventory = monthly_capacity * 1.0  # 1 month inventory
                
                if tech not in self.battery_data['inventory']:
                    self.battery_data['inventory'][tech] = {}
                if region not in self.battery_data['inventory'][tech]:
                    self.battery_data['inventory'][tech][region] = []
                
                self.battery_data['inventory'][tech][region].append(initial_inventory)

    def update_production(self):
        """Advanced production planning with AI-driven demand forecasting and optimization"""
        current_date = self.simulation_data['current_date']
        current_month = current_date.month
        
        # Step 1: Forecast demand for each technology
        demand_forecasts = self._forecast_demand(current_month)
        
        # Step 2: Assess supply chain constraints
        supply_constraints = self._assess_supply_constraints()
        
        # Step 3: Optimize production allocation
        production_plan = self._optimize_production_allocation(demand_forecasts, supply_constraints)
        
        # Step 4: Execute production and update metrics
        self._execute_production(production_plan, current_month)
        
        # Step 5: Update raw material inventory and procurement
        self._update_raw_materials(production_plan)
        
        # Step 6: Update quality metrics and technology advancement
        self._update_quality_metrics()
        
        # Step 7: Assess and update supply chain risks
        self._update_supply_chain_risks()
        
        print(f"Production updated for {current_date.strftime('%Y-%m')}: Total planned {sum(sum(tech.values()) for tech in production_plan.values()):.1f} GWh")
    
    def _forecast_demand(self, current_month):
        """Use AI models to forecast demand for each battery technology"""
        demand_forecasts = {}
        
        for tech in self.production_capacity:
            # Prepare features for prediction
            time_trend = 1.5  # Assume continued growth
            seasonal = 1 + 0.1 * np.sin(2 * np.pi * current_month / 12)
            economic_factor = np.random.normal(1.05, 0.05)  # Slight economic growth
            competition_factor = np.random.normal(0.85, 0.03)  # Increasing competition
            
            features = np.array([[current_month, time_trend, seasonal, economic_factor, competition_factor]])
            
            # Predict demand using trained model
            base_demand = self.market_models[tech].predict(features)[0]
            
            # Apply market dynamics and customer contracts
            contract_demand = sum(self.customers[customer]['contract_gwh'] for customer in self.customers 
                                if customer != 'Spot_Market') / 12  # Monthly from contracts
            
            spot_demand = base_demand * 0.3  # 30% spot market
            total_demand = contract_demand + spot_demand
            
            # Distribute demand across regions based on market presence
            regional_demand = {}
            for region in self.production_capacity[tech]:
                if region == 'China':
                    regional_demand[region] = total_demand * 0.6
                elif region == 'Europe':
                    regional_demand[region] = total_demand * 0.2
                elif region == 'NorthAmerica':
                    regional_demand[region] = total_demand * 0.15
                else:
                    regional_demand[region] = total_demand * 0.05
            
            demand_forecasts[tech] = regional_demand
        
        return demand_forecasts
    
    def _assess_supply_constraints(self):
        """Assess raw material availability and supply chain constraints"""
        constraints = {}
        
        for material, data in self.raw_materials.items():
            # Calculate months of inventory remaining
            months_remaining = data['inventory_tons'] / data['monthly_consumption']
            
            # Assess supplier reliability impact
            reliability_factor = data['supplier_reliability']
            
            # Calculate constraint severity (0 = no constraint, 1 = severe constraint)
            if months_remaining < 1:
                constraint_severity = 0.8
            elif months_remaining < 2:
                constraint_severity = 0.4
            elif months_remaining < 3:
                constraint_severity = 0.2
            else:
                constraint_severity = 0.0
            
            # Adjust for supplier reliability
            constraint_severity *= (2 - reliability_factor)
            
            constraints[material] = {
                'severity': min(constraint_severity, 1.0),
                'months_remaining': months_remaining,
                'reliability_factor': reliability_factor
            }
        
        return constraints
    
    def _optimize_production_allocation(self, demand_forecasts, supply_constraints):
        """Optimize production allocation considering demand, capacity, and constraints"""
        production_plan = {}
        
        for tech in self.production_capacity:
            production_plan[tech] = {}
            
            for region in self.production_capacity[tech]:
                # Base capacity (monthly)
                base_capacity = self.production_capacity[tech][region] / 12
                
                # Apply supply chain constraints
                constraint_factor = 1.0
                for material, constraint in supply_constraints.items():
                    constraint_factor *= (1 - constraint['severity'] * 0.3)  # Max 30% reduction per material
                
                # Calculate available capacity
                available_capacity = base_capacity * constraint_factor
                
                # Get demand for this tech/region
                regional_demand = demand_forecasts[tech][region]
                
                # Allocate production (min of demand and available capacity)
                allocated_production = min(regional_demand, available_capacity)
                
                # Apply efficiency factors
                efficiency = np.random.normal(0.92, 0.02)  # 92% average efficiency
                actual_production = allocated_production * max(efficiency, 0.8)
                
                production_plan[tech][region] = actual_production
        
        return production_plan
    
    def _execute_production(self, production_plan, current_month):
        """Execute the production plan and update tracking data"""
        for tech in production_plan:
            for region in production_plan[tech]:
                production_amount = production_plan[tech][region]
                
                # Update production tracking
                self.battery_data['production'][tech][region].append(production_amount)
                
                # Update inventory
                current_inventory = self.battery_data['inventory'][tech][region][-1] if self.battery_data['inventory'][tech][region] else 0
                new_inventory = current_inventory + production_amount
                self.battery_data['inventory'][tech][region].append(new_inventory)
                
                # Calculate and update capacity utilization
                max_capacity = self.production_capacity[tech][region] / 12
                utilization = production_amount / max_capacity if max_capacity > 0 else 0
                self.battery_data['capacity_utilization'][tech][region].append(utilization)
    
    def _update_raw_materials(self, production_plan):
        """Update raw material inventory based on production and procurement"""
        # Calculate total production
        total_production = sum(sum(tech.values()) for tech in production_plan.values())
        
        # Material consumption ratios (tons per GWh)
        consumption_ratios = {
            'lithium': 0.8,
            'cobalt': 0.3,
            'nickel': 1.2,
            'graphite': 0.6
        }
        
        for material, ratio in consumption_ratios.items():
            consumption = total_production * ratio
            
            # Update inventory
            self.raw_materials[material]['inventory_tons'] -= consumption
            
            # Trigger procurement if inventory is low
            if self.raw_materials[material]['inventory_tons'] < self.raw_materials[material]['monthly_consumption'] * 2:
                procurement_amount = self.raw_materials[material]['monthly_consumption'] * 4
                self.raw_materials[material]['inventory_tons'] += procurement_amount
                
                # Update price based on market conditions
                price_change = np.random.normal(0, self.raw_materials[material]['price_volatility'] * 0.1)
                self.raw_materials[material]['current_price'] *= (1 + price_change)
    
    def _update_quality_metrics(self):
        """Update quality metrics and technology advancement"""
        # Simulate quality metrics
        defect_rate = max(0, np.random.normal(0.02, 0.005))  # 2% average defect rate
        cycle_life = np.random.normal(0.95, 0.02)  # 95% of target cycle life
        energy_density = np.random.normal(0.98, 0.01)  # 98% of target energy density
        safety_incidents = np.random.poisson(0.1)  # Very low incident rate
        customer_satisfaction = np.random.normal(0.88, 0.03)  # 88% satisfaction
        
        # Update tracking
        self.battery_data['quality_metrics']['defect_rate'].append(defect_rate)
        self.battery_data['quality_metrics']['cycle_life_performance'].append(cycle_life)
        self.battery_data['quality_metrics']['energy_density_achievement'].append(energy_density)
        self.battery_data['quality_metrics']['safety_incidents'].append(safety_incidents)
        self.battery_data['quality_metrics']['customer_satisfaction'].append(customer_satisfaction)
        
        # Update technology advancement
        for tech, roadmap in self.technology_roadmap.items():
            # Gradual technology readiness improvement
            if roadmap['readiness'] < 1.0:
                improvement = np.random.normal(0.02, 0.005)  # 2% monthly improvement
                roadmap['readiness'] = min(1.0, roadmap['readiness'] + improvement)
    
    def _update_supply_chain_risks(self):
        """Assess and update supply chain risk metrics"""
        # Material shortage risk
        shortage_risk = 0
        for material, data in self.raw_materials.items():
            if data['inventory_tons'] < data['monthly_consumption'] * 1.5:
                shortage_risk += 0.25
        
        # Price volatility impact
        price_volatility = np.mean([data['price_volatility'] for data in self.raw_materials.values()])
        
        # Supplier performance (based on reliability)
        supplier_performance = np.mean([data['supplier_reliability'] for data in self.raw_materials.values()])
        
        # Logistics disruption (random events)
        logistics_disruption = np.random.exponential(0.1)  # Low probability events
        
        # Geopolitical risk (simplified)
        geopolitical_risk = np.random.normal(0.15, 0.05)  # 15% base risk
        
        # Update tracking
        self.battery_data['supply_chain_risk']['material_shortage_risk'].append(min(shortage_risk, 1.0))
        self.battery_data['supply_chain_risk']['price_volatility_impact'].append(price_volatility)
        self.battery_data['supply_chain_risk']['supplier_performance'].append(supplier_performance)
        self.battery_data['supply_chain_risk']['logistics_disruption'].append(min(logistics_disruption, 1.0))
        self.battery_data['supply_chain_risk']['geopolitical_risk'].append(max(0, min(geopolitical_risk, 1.0)))

    def update_sales(self):
        """Update battery sales based on customer contracts and market demand"""
        current_date = self.simulation_data['current_date']
        
        for tech in self.production_capacity:
            for region in self.production_capacity[tech]:
                # Get current inventory
                current_inventory = self.battery_data['inventory'][tech][region][-1] if self.battery_data['inventory'][tech][region] else 0
                
                # Calculate sales based on customer priorities and contracts
                total_sales = 0
                
                # Sort customers by priority
                sorted_customers = sorted(self.customers.items(), key=lambda x: x[1]['priority'])
                
                for customer_name, customer_data in sorted_customers:
                    if current_inventory <= 0:
                        break
                    
                    # Calculate monthly contract amount
                    monthly_contract = customer_data['contract_gwh'] / 12
                    
                    # Apply regional distribution
                    if region == 'China':
                        regional_factor = 0.6
                    elif region == 'Europe':
                        regional_factor = 0.2
                    elif region == 'NorthAmerica':
                        regional_factor = 0.15
                    else:
                        regional_factor = 0.05
                    
                    regional_demand = monthly_contract * regional_factor
                    
                    # Technology preference (LFP_Blade preferred for most customers)
                    if tech == 'LFP_Blade':
                        tech_preference = 0.8
                    elif tech == 'NMC':
                        tech_preference = 0.15
                    else:  # SolidState
                        tech_preference = 0.05
                    
                    customer_demand = regional_demand * tech_preference
                    
                    # Fulfill demand up to available inventory
                    sales_amount = min(customer_demand, current_inventory)
                    total_sales += sales_amount
                    current_inventory -= sales_amount
                
                # Update sales tracking
                self.battery_data['sales'][tech][region].append(total_sales)
                
                # Update inventory after sales
                self.battery_data['inventory'][tech][region][-1] = current_inventory
    
    def update_raw_material_inventory(self):
        """Legacy method - functionality moved to _update_raw_materials"""
        pass
    
    def get_production_metrics(self):
        """Get comprehensive production metrics for reporting"""
        metrics = {
            'total_production_gwh': 0,
            'capacity_utilization': {},
            'technology_mix': {},
            'regional_distribution': {},
            'quality_summary': {},
            'supply_chain_status': {}
        }
        
        # Calculate total production
        for tech in self.battery_data['production']:
            for region in self.battery_data['production'][tech]:
                if self.battery_data['production'][tech][region]:
                    metrics['total_production_gwh'] += sum(self.battery_data['production'][tech][region])
        
        # Calculate average capacity utilization
        for tech in self.battery_data['capacity_utilization']:
            tech_utilization = []
            for region in self.battery_data['capacity_utilization'][tech]:
                if self.battery_data['capacity_utilization'][tech][region]:
                    tech_utilization.extend(self.battery_data['capacity_utilization'][tech][region])
            
            if tech_utilization:
                metrics['capacity_utilization'][tech] = np.mean(tech_utilization)
        
        # Calculate technology mix
        tech_totals = {}
        for tech in self.battery_data['production']:
            tech_total = 0
            for region in self.battery_data['production'][tech]:
                if self.battery_data['production'][tech][region]:
                    tech_total += sum(self.battery_data['production'][tech][region])
            tech_totals[tech] = tech_total
        
        total_all_tech = sum(tech_totals.values())
        if total_all_tech > 0:
            for tech, total in tech_totals.items():
                metrics['technology_mix'][tech] = total / total_all_tech
        
        # Quality summary
        if self.battery_data['quality_metrics']['defect_rate']:
            metrics['quality_summary'] = {
                'avg_defect_rate': np.mean(self.battery_data['quality_metrics']['defect_rate']),
                'avg_customer_satisfaction': np.mean(self.battery_data['quality_metrics']['customer_satisfaction']),
                'avg_cycle_life_performance': np.mean(self.battery_data['quality_metrics']['cycle_life_performance'])
            }
        
        # Supply chain status
        if self.battery_data['supply_chain_risk']['material_shortage_risk']:
            metrics['supply_chain_status'] = {
                'material_shortage_risk': self.battery_data['supply_chain_risk']['material_shortage_risk'][-1],
                'supplier_performance': self.battery_data['supply_chain_risk']['supplier_performance'][-1],
                'price_volatility': self.battery_data['supply_chain_risk']['price_volatility_impact'][-1]
            }
        
        return metrics
    
    def get_financial_metrics(self):
        """Calculate financial metrics for the battery division"""
        metrics = {
            'revenue': 0,
            'raw_material_costs': 0,
            'gross_margin': 0,
            'inventory_value': 0
        }
        
        # Calculate revenue from sales
        base_price_per_gwh = 800000  # CNY per GWh
        
        for tech in self.battery_data['sales']:
            tech_price_multiplier = {
                'LFP_Blade': 1.0,
                'NMC': 1.2,
                'SolidState': 2.5
            }.get(tech, 1.0)
            
            for region in self.battery_data['sales'][tech]:
                if self.battery_data['sales'][tech][region]:
                    total_sales = sum(self.battery_data['sales'][tech][region])
                    metrics['revenue'] += total_sales * base_price_per_gwh * tech_price_multiplier
        
        # Calculate raw material costs
        for material, data in self.raw_materials.items():
            monthly_cost = data['monthly_consumption'] * data['current_price']
            metrics['raw_material_costs'] += monthly_cost
        
        # Calculate gross margin
        if metrics['revenue'] > 0:
            metrics['gross_margin'] = (metrics['revenue'] - metrics['raw_material_costs']) / metrics['revenue']
        
        # Calculate inventory value
        for tech in self.battery_data['inventory']:
            tech_price_multiplier = {
                'LFP_Blade': 1.0,
                'NMC': 1.2,
                'SolidState': 2.5
            }.get(tech, 1.0)
            
            for region in self.battery_data['inventory'][tech]:
                if self.battery_data['inventory'][tech][region]:
                    current_inventory = self.battery_data['inventory'][tech][region][-1]
                    metrics['inventory_value'] += current_inventory * base_price_per_gwh * tech_price_multiplier * 0.7  # 70% of selling price
        
        return metrics
    
    def get_performance_metrics(self):
        """Get comprehensive performance metrics for integration with finance module"""
        financial_metrics = self.get_financial_metrics()
        production_metrics = self.get_production_metrics()
        
        return {
            'financial': {
                'total_revenue': financial_metrics['revenue'],
                'raw_material_costs': financial_metrics['raw_material_costs'],
                'gross_margin': financial_metrics['gross_margin'],
                'inventory_value': financial_metrics['inventory_value']
            },
            'production': production_metrics,
            'operational': {
                'capacity_utilization': self.battery_data['capacity_utilization'],
                'quality_metrics': self.battery_data['quality_metrics']
            }
        }
    
    def log_data(self):
        """Enhanced data logging with comprehensive metrics"""
        current_date = self.simulation_data['current_date']
        
        log_entry = {
            'date': current_date.isoformat(),
            'type': 'BatteryModule_Comprehensive',
            'production_data': self.battery_data['production'],
            'sales_data': self.battery_data['sales'],
            'inventory_data': self.battery_data['inventory'],
            'capacity_utilization': self.battery_data['capacity_utilization'],
            'quality_metrics': self.battery_data['quality_metrics'],
            'supply_chain_risk': self.battery_data['supply_chain_risk'],
            'raw_materials': self.raw_materials,
            'customer_contracts': self.customers,
            'technology_roadmap': self.technology_roadmap,
            'production_metrics': self.get_production_metrics(),
            'financial_metrics': self.get_financial_metrics()
        }
        
        # Save monthly detailed log
        log_path = f"data/battery_comprehensive_{current_date.strftime('%Y%m')}.json"
        with open(log_path, 'w') as f:
            json.dump(log_entry, f, indent=2, default=str)
        
        # Save summary for main simulation
        summary_log = {
            'date': current_date.isoformat(),
            'total_production_gwh': self.get_production_metrics()['total_production_gwh'],
            'total_revenue_cny': self.get_financial_metrics()['revenue'],
            'capacity_utilization_avg': np.mean(list(self.get_production_metrics()['capacity_utilization'].values())) if self.get_production_metrics()['capacity_utilization'] else 0,
            'supply_chain_risk_score': self.get_production_metrics()['supply_chain_status'].get('material_shortage_risk', 0)
        }
        
        summary_path = f"data/battery_summary_{current_date.strftime('%Y%m')}.json"
        with open(summary_path, 'w') as f:
            json.dump(summary_log, f, indent=2)

    def get_production(self, battery_type=None, region=None):
        if battery_type and region:
            return self.battery_data['production'][battery_type][region]
        elif battery_type:
            return self.battery_data['production'][battery_type]
        return self.battery_data['production']
