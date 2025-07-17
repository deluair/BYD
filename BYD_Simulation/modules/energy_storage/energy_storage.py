import json
import random
import numpy as np
from datetime import datetime, timedelta

class EnergyStorageModule:
    def __init__(self, simulation_data):
        self.simulation_data = simulation_data
        self.config = simulation_data['config']
        self.energy_storage_data = {
            'revenue': 5.0,  # Billion CNY, initial
            'business_segments': {
                'Utility_Scale': {
                    'installed_capacity_gwh': 45.2,
                    'pipeline_gwh': 125.8,
                    'revenue': 2.8,
                    'market_share': 0.18,
                    'avg_contract_duration': 15,  # years
                    'technology_mix': {
                        'LFP': 0.75,
                        'NCM': 0.20,
                        'Sodium_Ion': 0.05
                    }
                },
                'Commercial_Industrial': {
                    'installed_capacity_gwh': 18.6,
                    'pipeline_gwh': 42.3,
                    'revenue': 1.5,
                    'market_share': 0.22,
                    'avg_contract_duration': 10,
                    'technology_mix': {
                        'LFP': 0.85,
                        'NCM': 0.15
                    }
                },
                'Residential': {
                    'installed_capacity_gwh': 3.2,
                    'pipeline_gwh': 8.9,
                    'revenue': 0.7,
                    'market_share': 0.15,
                    'avg_contract_duration': 8,
                    'technology_mix': {
                        'LFP': 0.90,
                        'NCM': 0.10
                    }
                }
            },
            'contracts': {
                'active': [
                    {'name': 'Saudi Electricity Co', 'capacity_gwh': 12.5, 'status': 'ongoing', 'region': 'Middle East', 'value_billion_cny': 8.2},
                    {'name': 'California ISO', 'capacity_gwh': 8.3, 'status': 'ongoing', 'region': 'North America', 'value_billion_cny': 6.1},
                    {'name': 'National Grid UK', 'capacity_gwh': 6.7, 'status': 'ongoing', 'region': 'Europe', 'value_billion_cny': 4.8}
                ],
                'pipeline': [
                    {'name': 'Texas Grid Operator', 'capacity_gwh': 15.2, 'status': 'negotiation', 'region': 'North America', 'probability': 0.75},
                    {'name': 'Australian Energy Market', 'capacity_gwh': 9.8, 'status': 'proposal', 'region': 'Asia Pacific', 'probability': 0.60}
                ]
            },
            'manufacturing': {
                'facilities': {
                    'Hefei': {'capacity_gwh': 40, 'utilization': 0.82, 'technology': 'LFP_Advanced'},
                    'Qingdao': {'capacity_gwh': 25, 'utilization': 0.88, 'technology': 'NCM_Premium'},
                    'Changzhou': {'capacity_gwh': 20, 'utilization': 0.75, 'technology': 'Sodium_Ion'}
                },
                'quality_metrics': {
                    'cycle_life': 8500,
                    'round_trip_efficiency': 0.92,
                    'safety_incidents': 0.0001,  # per GWh
                    'warranty_claims': 0.008
                }
            },
            'technology_development': {
                'next_gen_chemistry': {
                    'solid_state': 0.35,
                    'silicon_anode': 0.68,
                    'lithium_metal': 0.25
                },
                'system_integration': {
                    'ai_bms': 0.78,
                    'grid_forming': 0.85,
                    'predictive_maintenance': 0.72
                },
                'cost_reduction_target': 0.15  # 15% cost reduction goal
            },
            'market_dynamics': {
                'renewable_integration_demand': 1.0,
                'grid_stability_requirements': 1.0,
                'policy_support_index': 0.85,
                'competition_intensity': 0.72,
                'pricing_pressure': 0.65
            },
            'regional_presence': {
                'China': {'market_share': 0.28, 'growth_rate': 0.15},
                'North_America': {'market_share': 0.12, 'growth_rate': 0.25},
                'Europe': {'market_share': 0.08, 'growth_rate': 0.22},
                'Asia_Pacific': {'market_share': 0.15, 'growth_rate': 0.30},
                'Middle_East': {'market_share': 0.20, 'growth_rate': 0.18}
            }
        }
        self.initialize()

    def initialize(self):
        print("Energy Storage module initialized with comprehensive capabilities.")
        self._initialize_market_forecasts()
        self._setup_competitive_landscape()
        self._initialize_market_dynamics()

    def _initialize_market_dynamics(self):
        """Initialize market dynamics tracking"""
        self.market_dynamics = {
            'renewable_integration_demand': 100.0,  # Base index
            'grid_stability_requirements': 100.0,  # Base index
            'policy_support_index': 0.75,
            'technology_adoption_rate': 0.28,
            'cost_competitiveness': 0.82
        }

    def _initialize_market_forecasts(self):
        """Initialize market forecast models"""
        self.market_forecasts = {
            'global_demand_gwh': 580.0,  # Current global demand
            'annual_growth_rate': 0.35,
            'renewable_penetration': 0.42,
            'grid_modernization_investment': 1.2  # Trillion USD globally
        }

    def _setup_competitive_landscape(self):
        """Setup competitive analysis"""
        self.competitors = {
            'CATL': {'market_share': 0.32, 'strength': 'cost_leadership'},
            'Tesla': {'market_share': 0.18, 'strength': 'technology_integration'},
            'LG_Energy': {'market_share': 0.15, 'strength': 'manufacturing_scale'},
            'Panasonic': {'market_share': 0.12, 'strength': 'quality_reliability'}
        }

    def update(self):
        """Comprehensive monthly update of energy storage operations"""
        self._update_market_dynamics()
        self._update_business_segments()
        self._process_contract_pipeline()
        self._update_manufacturing()
        self._advance_technology_development()
        self._assess_regional_performance()
        self._calculate_financial_performance()
        
        self.log_data()

    def _update_market_dynamics(self):
        """Update market conditions and demand drivers"""
        # Renewable energy growth driving storage demand
        renewable_growth = random.uniform(0.08, 0.15)
        self.market_dynamics['renewable_integration_demand'] *= (1 + renewable_growth)
        
        # Grid stability requirements
        grid_stability_change = random.uniform(0.02, 0.08)
        self.market_dynamics['grid_stability_requirements'] *= (1 + grid_stability_change)
        
        # Policy support fluctuations
        policy_change = random.uniform(-0.05, 0.10)
        self.market_dynamics['policy_support_index'] = max(0.3, 
            min(1.0, self.market_dynamics['policy_support_index'] + policy_change))
        
        # Technology adoption and cost competitiveness
        adoption_change = random.uniform(-0.02, 0.05)
        self.market_dynamics['technology_adoption_rate'] = max(0.1, 
            min(0.8, self.market_dynamics['technology_adoption_rate'] + adoption_change))
        
        cost_change = random.uniform(-0.03, 0.02)
        self.market_dynamics['cost_competitiveness'] = max(0.5, 
            min(1.0, self.market_dynamics['cost_competitiveness'] + cost_change))

    def _update_business_segments(self):
        """Update performance of each business segment"""
        for segment, data in self.energy_storage_data['business_segments'].items():
            # Segment-specific growth rates
            if segment == 'Utility_Scale':
                growth = self.market_dynamics['renewable_integration_demand'] * 0.08 + random.uniform(0.05, 0.15)
            elif segment == 'Commercial_Industrial':
                growth = self.market_dynamics['grid_stability_requirements'] * 0.06 + random.uniform(0.03, 0.12)
            else:  # Residential
                growth = random.uniform(0.08, 0.20)  # High growth potential
            
            # Apply market constraints
            policy_impact = self.energy_storage_data['market_dynamics']['policy_support_index']
            price_impact = 1 - (self.energy_storage_data['market_dynamics']['pricing_pressure'] * 0.1)
            
            data['revenue'] *= (1 + growth) * policy_impact * price_impact
            
            # Update pipeline
            pipeline_conversion = random.uniform(0.05, 0.15)
            converted_capacity = data['pipeline_gwh'] * pipeline_conversion
            data['installed_capacity_gwh'] += converted_capacity
            data['pipeline_gwh'] *= (1 - pipeline_conversion + random.uniform(0.10, 0.25))  # New pipeline additions
            
            # Market share dynamics
            competitive_pressure = self.energy_storage_data['market_dynamics']['competition_intensity']
            share_change = random.uniform(-0.01, 0.03) - (competitive_pressure * 0.01)
            data['market_share'] = max(0.05, min(0.35, data['market_share'] + share_change))

    def _process_contract_pipeline(self):
        """Process contract negotiations and new opportunities"""
        # Convert pipeline contracts to active
        for contract in self.energy_storage_data['contracts']['pipeline'][:]:
            if random.random() < contract['probability'] * 0.1:  # Monthly conversion probability
                contract['status'] = 'active'
                contract['value_billion_cny'] = contract['capacity_gwh'] * random.uniform(0.6, 0.8)
                self.energy_storage_data['contracts']['active'].append(contract)
                self.energy_storage_data['contracts']['pipeline'].remove(contract)
                print(f"Energy Storage: New contract signed - {contract['name']} ({contract['capacity_gwh']:.1f} GWh)")
        
        # Generate new pipeline opportunities
        if random.random() < 0.15:  # 15% chance of new opportunity
            regions = ['North America', 'Europe', 'Asia Pacific', 'Middle East', 'Latin America']
            new_opportunity = {
                'name': f"Grid Project {self.simulation_data['current_date'].strftime('%Y-%m')}",
                'capacity_gwh': random.uniform(3, 20),
                'status': 'proposal',
                'region': random.choice(regions),
                'probability': random.uniform(0.4, 0.8)
            }
            self.energy_storage_data['contracts']['pipeline'].append(new_opportunity)

    def _update_manufacturing(self):
        """Update manufacturing operations and capabilities"""
        for facility, data in self.energy_storage_data['manufacturing']['facilities'].items():
            # Utilization based on demand
            demand_impact = 1 + (self.market_dynamics['renewable_integration_demand'] * 0.05)
            data['utilization'] = min(0.98, data['utilization'] * demand_impact * random.uniform(0.98, 1.02))
        
        # Quality improvements
        quality = self.energy_storage_data['manufacturing']['quality_metrics']
        quality['cycle_life'] += random.randint(10, 50)
        quality['round_trip_efficiency'] = min(0.96, quality['round_trip_efficiency'] * random.uniform(1.000, 1.002))
        quality['safety_incidents'] *= random.uniform(0.95, 1.01)
        quality['warranty_claims'] *= random.uniform(0.98, 1.02)

    def _advance_technology_development(self):
        """Update technology development progress"""
        tech_dev = self.energy_storage_data['technology_development']
        
        # Next-gen chemistry progress
        for tech, progress in tech_dev['next_gen_chemistry'].items():
            advancement = random.uniform(0.01, 0.04)
            tech_dev['next_gen_chemistry'][tech] = min(1.0, progress + advancement)
        
        # System integration progress
        for tech, progress in tech_dev['system_integration'].items():
            advancement = random.uniform(0.01, 0.03)
            tech_dev['system_integration'][tech] = min(1.0, progress + advancement)
        
        # Cost reduction progress
        cost_reduction = random.uniform(0.002, 0.008)
        tech_dev['cost_reduction_target'] = max(0, tech_dev['cost_reduction_target'] - cost_reduction)

    def _assess_regional_performance(self):
        """Assess and update regional market performance"""
        for region, data in self.energy_storage_data['regional_presence'].items():
            # Regional growth influenced by policy and market conditions
            base_growth = data['growth_rate']
            policy_impact = self.energy_storage_data['market_dynamics']['policy_support_index']
            market_growth = base_growth * policy_impact * random.uniform(0.8, 1.2)
            
            # Update market share
            share_change = random.uniform(-0.005, 0.015)
            data['market_share'] = max(0.02, min(0.40, data['market_share'] + share_change))
            data['growth_rate'] = max(0.05, min(0.50, market_growth))

    def _calculate_financial_performance(self):
        """Calculate overall financial performance"""
        total_revenue = sum(data['revenue'] for data in self.energy_storage_data['business_segments'].values())
        self.energy_storage_data['revenue'] = total_revenue

    def get_performance_metrics(self):
        """Get comprehensive performance metrics"""
        total_installed = sum(data['installed_capacity_gwh'] for data in self.energy_storage_data['business_segments'].values())
        total_pipeline = sum(data['pipeline_gwh'] for data in self.energy_storage_data['business_segments'].values())
        avg_market_share = np.mean([data['market_share'] for data in self.energy_storage_data['business_segments'].values()])
        
        return {
            'financial': {
                'total_revenue': self.energy_storage_data['revenue']
            },
            'capacity_metrics': {
                'total_installed_gwh': total_installed,
                'total_pipeline_gwh': total_pipeline,
                'capacity_utilization': np.mean([data['utilization'] for data in self.energy_storage_data['manufacturing']['facilities'].values()])
            },
            'market_position': {
                'avg_market_share': avg_market_share,
                'active_contracts': len(self.energy_storage_data['contracts']['active']),
                'pipeline_contracts': len(self.energy_storage_data['contracts']['pipeline'])
            },
            'technology_readiness': {
                'next_gen_avg': np.mean(list(self.energy_storage_data['technology_development']['next_gen_chemistry'].values())),
                'system_integration_avg': np.mean(list(self.energy_storage_data['technology_development']['system_integration'].values())),
                'cost_competitiveness': 1 - self.energy_storage_data['technology_development']['cost_reduction_target']
            },
            'quality_score': {
                'cycle_life_index': self.energy_storage_data['manufacturing']['quality_metrics']['cycle_life'] / 10000,
                'efficiency_score': self.energy_storage_data['manufacturing']['quality_metrics']['round_trip_efficiency'],
                'reliability_score': 1 - self.energy_storage_data['manufacturing']['quality_metrics']['warranty_claims']
            }
        }

    def log_data(self):
        """Enhanced logging with comprehensive data"""
        log_entry = {
            'timestamp': self.simulation_data['current_date'].isoformat(),
            'type': 'EnergyStorage',
            'data': self.energy_storage_data,
            'performance_metrics': self.get_performance_metrics(),
            'market_forecasts': self.market_forecasts,
            'competitive_landscape': self.competitors
        }
        log_path = f"data/energy_storage_{self.simulation_data['current_date'].strftime('%Y%m')}.json"
        with open(log_path, 'w') as f:
            json.dump(log_entry, f, indent=4, default=str)
