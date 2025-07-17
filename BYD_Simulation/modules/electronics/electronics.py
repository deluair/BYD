import json
import random
import numpy as np
from datetime import datetime, timedelta

class ElectronicsModule:
    def __init__(self, simulation_data):
        self.simulation_data = simulation_data
        self.config = simulation_data['config']
        self.electronics_data = {
            'revenue': 159.6,  # Billion CNY, initial
            'product_lines': {
                'Semiconductors': {
                    'revenue': 65.0,
                    'market_share': 0.12,
                    'capacity_utilization': 0.85,
                    'technology_node': '28nm',
                    'r_and_d_investment': 8.5
                },
                'IGBT_Modules': {
                    'revenue': 35.2,
                    'market_share': 0.25,
                    'capacity_utilization': 0.92,
                    'efficiency_rating': 0.98,
                    'automotive_share': 0.75
                },
                'Power_Management': {
                    'revenue': 28.8,
                    'market_share': 0.18,
                    'capacity_utilization': 0.88,
                    'product_portfolio': ['DC-DC', 'AC-DC', 'Wireless_Charging'],
                    'efficiency_improvement': 0.03
                },
                'Sensors_IoT': {
                    'revenue': 30.6,
                    'market_share': 0.15,
                    'capacity_utilization': 0.82,
                    'ai_integration': 0.45,
                    'automotive_grade': 0.68
                }
            },
            'manufacturing': {
                'facilities': {
                    'Shenzhen': {'capacity': 100, 'utilization': 0.85, 'technology': 'Advanced'},
                    'Xian': {'capacity': 80, 'utilization': 0.90, 'technology': 'Standard'},
                    'Changsha': {'capacity': 60, 'utilization': 0.78, 'technology': 'Emerging'}
                },
                'quality_metrics': {
                    'defect_rate': 0.0012,
                    'yield_rate': 0.94,
                    'customer_satisfaction': 0.89
                }
            },
            'innovation': {
                'patents_filed': 2850,
                'r_and_d_staff': 12500,
                'technology_roadmap': {
                    'next_gen_semiconductors': 0.65,
                    'ai_chips': 0.40,
                    'quantum_sensors': 0.15
                }
            },
            'market_dynamics': {
                'competition_intensity': 0.75,
                'price_pressure': 0.68,
                'demand_growth': 0.12,
                'supply_chain_stability': 0.82
            }
        }
        self.initialize()

    def initialize(self):
        print("Electronics module initialized with advanced capabilities.")
        self._initialize_market_trends()
        self._setup_customer_segments()

    def _initialize_market_trends(self):
        """Initialize market trend tracking"""
        self.market_trends = {
            'ev_electronics_demand': 1.0,
            'industrial_automation': 1.0,
            'consumer_electronics': 1.0,
            'renewable_energy': 1.0
        }

    def _setup_customer_segments(self):
        """Setup customer segment analysis"""
        self.customer_segments = {
            'Automotive_OEMs': {'share': 0.45, 'growth': 0.15, 'margin': 0.22},
            'Industrial': {'share': 0.25, 'growth': 0.08, 'margin': 0.18},
            'Consumer': {'share': 0.20, 'growth': 0.05, 'margin': 0.12},
            'Renewable_Energy': {'share': 0.10, 'growth': 0.25, 'margin': 0.28}
        }

    def update(self):
        """Comprehensive monthly update of electronics operations"""
        self._update_market_dynamics()
        self._update_product_lines()
        self._update_manufacturing()
        self._update_innovation()
        self._calculate_financial_performance()
        self._assess_competitive_position()
        
        self.log_data()

    def _update_market_dynamics(self):
        """Update market conditions and trends"""
        # EV market driving electronics demand
        ev_growth = random.uniform(0.08, 0.18)
        self.market_trends['ev_electronics_demand'] *= (1 + ev_growth)
        
        # Industrial automation growth
        industrial_growth = random.uniform(0.03, 0.12)
        self.market_trends['industrial_automation'] *= (1 + industrial_growth)
        
        # Consumer electronics volatility
        consumer_change = random.uniform(-0.05, 0.08)
        self.market_trends['consumer_electronics'] *= (1 + consumer_change)
        
        # Renewable energy sector growth
        renewable_growth = random.uniform(0.10, 0.22)
        self.market_trends['renewable_energy'] *= (1 + renewable_growth)
        
        # Update overall market dynamics
        self.electronics_data['market_dynamics']['demand_growth'] = np.mean([
            ev_growth, industrial_growth, max(0, consumer_change), renewable_growth
        ])
        
        # Competition and pricing pressure
        self.electronics_data['market_dynamics']['competition_intensity'] += random.uniform(-0.02, 0.03)
        self.electronics_data['market_dynamics']['price_pressure'] += random.uniform(-0.03, 0.02)
        
        # Supply chain stability
        supply_change = random.uniform(-0.05, 0.03)
        self.electronics_data['market_dynamics']['supply_chain_stability'] = max(0.5, 
            min(1.0, self.electronics_data['market_dynamics']['supply_chain_stability'] + supply_change))

    def _update_product_lines(self):
        """Update each product line performance"""
        for product, data in self.electronics_data['product_lines'].items():
            # Market-driven revenue growth
            if product == 'Semiconductors':
                growth = self.market_trends['ev_electronics_demand'] * 0.05 + random.uniform(-0.02, 0.08)
            elif product == 'IGBT_Modules':
                growth = self.market_trends['ev_electronics_demand'] * 0.08 + random.uniform(-0.01, 0.12)
            elif product == 'Power_Management':
                growth = (self.market_trends['renewable_energy'] * 0.06 + 
                         self.market_trends['ev_electronics_demand'] * 0.04 + random.uniform(-0.02, 0.06))
            else:  # Sensors_IoT
                growth = (self.market_trends['industrial_automation'] * 0.07 + 
                         self.market_trends['ev_electronics_demand'] * 0.05 + random.uniform(-0.03, 0.10))
            
            # Apply growth with market constraints
            price_impact = 1 - (self.electronics_data['market_dynamics']['price_pressure'] * 0.1)
            data['revenue'] *= (1 + growth) * price_impact
            
            # Update capacity utilization
            demand_factor = 1 + self.electronics_data['market_dynamics']['demand_growth']
            data['capacity_utilization'] = min(0.98, data['capacity_utilization'] * demand_factor * random.uniform(0.98, 1.02))
            
            # Market share dynamics
            competitive_pressure = self.electronics_data['market_dynamics']['competition_intensity']
            share_change = random.uniform(-0.01, 0.02) - (competitive_pressure * 0.01)
            data['market_share'] = max(0.05, min(0.40, data['market_share'] + share_change))

    def _update_manufacturing(self):
        """Update manufacturing operations"""
        for facility, data in self.electronics_data['manufacturing']['facilities'].items():
            # Utilization based on demand
            demand_impact = 1 + self.electronics_data['market_dynamics']['demand_growth']
            supply_impact = self.electronics_data['market_dynamics']['supply_chain_stability']
            
            data['utilization'] = min(0.98, data['utilization'] * demand_impact * supply_impact * random.uniform(0.98, 1.02))
        
        # Quality improvements
        quality = self.electronics_data['manufacturing']['quality_metrics']
        quality['defect_rate'] *= random.uniform(0.95, 1.02)  # Gradual improvement
        quality['yield_rate'] = min(0.98, quality['yield_rate'] * random.uniform(1.00, 1.01))
        quality['customer_satisfaction'] = min(0.95, quality['customer_satisfaction'] * random.uniform(0.99, 1.02))

    def _update_innovation(self):
        """Update R&D and innovation metrics"""
        innovation = self.electronics_data['innovation']
        
        # Patent filing
        monthly_patents = random.randint(15, 45)
        innovation['patents_filed'] += monthly_patents
        
        # Technology roadmap progress
        for tech, progress in innovation['technology_roadmap'].items():
            advancement = random.uniform(0.01, 0.05)
            innovation['technology_roadmap'][tech] = min(1.0, progress + advancement)
        
        # R&D staff growth
        staff_change = random.uniform(-0.01, 0.03)
        innovation['r_and_d_staff'] = int(innovation['r_and_d_staff'] * (1 + staff_change))

    def _calculate_financial_performance(self):
        """Calculate overall financial performance"""
        total_revenue = sum(data['revenue'] for data in self.electronics_data['product_lines'].values())
        self.electronics_data['revenue'] = total_revenue

    def _assess_competitive_position(self):
        """Assess competitive position and strategic opportunities"""
        avg_market_share = np.mean([data['market_share'] for data in self.electronics_data['product_lines'].values()])
        avg_utilization = np.mean([data['capacity_utilization'] for data in self.electronics_data['product_lines'].values()])
        
        # Strategic alerts
        if avg_market_share < 0.15:
            print(f"Electronics Alert: Market share declining to {avg_market_share:.1%}")
        
        if avg_utilization > 0.95:
            print(f"Electronics Alert: High capacity utilization {avg_utilization:.1%} - consider expansion")

    def get_performance_metrics(self):
        """Get comprehensive performance metrics"""
        return {
            'financial': {
                'total_revenue': self.electronics_data['revenue']
            },
            'product_line_performance': self.electronics_data['product_lines'],
            'manufacturing_efficiency': {
                'avg_utilization': np.mean([data['utilization'] for data in self.electronics_data['manufacturing']['facilities'].values()]),
                'quality_score': (1 - self.electronics_data['manufacturing']['quality_metrics']['defect_rate']) * 
                               self.electronics_data['manufacturing']['quality_metrics']['yield_rate']
            },
            'innovation_index': {
                'patents_per_staff': self.electronics_data['innovation']['patents_filed'] / self.electronics_data['innovation']['r_and_d_staff'],
                'technology_readiness': np.mean(list(self.electronics_data['innovation']['technology_roadmap'].values()))
            },
            'market_position': {
                'avg_market_share': np.mean([data['market_share'] for data in self.electronics_data['product_lines'].values()]),
                'competitive_strength': 1 - self.electronics_data['market_dynamics']['competition_intensity']
            }
        }

    def log_data(self):
        """Enhanced logging with comprehensive data"""
        log_entry = {
            'timestamp': self.simulation_data['current_date'].isoformat(),
            'type': 'Electronics',
            'data': self.electronics_data,
            'performance_metrics': self.get_performance_metrics(),
            'market_trends': self.market_trends,
            'customer_segments': self.customer_segments
        }
        log_path = f"data/electronics_{self.simulation_data['current_date'].strftime('%Y%m')}.json"
        with open(log_path, 'w') as f:
            json.dump(log_entry, f, indent=4, default=str)
