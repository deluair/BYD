import json
import random
import numpy as np
from datetime import datetime, timedelta

class SupplyChainModule:
    def __init__(self, simulation_data):
        self.simulation_data = simulation_data
        self.config = simulation_data['config']
        self.supply_chain_data = {
            'supplier_network': {
                'tier_1_suppliers': {
                    'CATL': {
                        'category': 'Battery_Cells',
                        'reliability_score': 0.95,
                        'cost_competitiveness': 0.88,
                        'delivery_performance': 0.92,
                        'quality_rating': 0.94,
                        'capacity_utilization': 0.85,
                        'contract_value_billion_cny': 45.2,
                        'risk_level': 'low',
                        'geographic_location': 'China',
                        'backup_suppliers': ['BYD_Internal', 'EVE_Energy']
                    },
                    'Bosch': {
                        'category': 'Electronic_Components',
                        'reliability_score': 0.92,
                        'cost_competitiveness': 0.75,
                        'delivery_performance': 0.89,
                        'quality_rating': 0.96,
                        'capacity_utilization': 0.78,
                        'contract_value_billion_cny': 12.8,
                        'risk_level': 'medium',
                        'geographic_location': 'Germany',
                        'backup_suppliers': ['Continental', 'Denso']
                    },
                    'Ganfeng_Lithium': {
                        'category': 'Raw_Materials',
                        'reliability_score': 0.87,
                        'cost_competitiveness': 0.82,
                        'delivery_performance': 0.85,
                        'quality_rating': 0.90,
                        'capacity_utilization': 0.92,
                        'contract_value_billion_cny': 8.5,
                        'risk_level': 'high',
                        'geographic_location': 'China',
                        'backup_suppliers': ['Albemarle', 'SQM']
                    },
                    'Magna_International': {
                        'category': 'Automotive_Parts',
                        'reliability_score': 0.90,
                        'cost_competitiveness': 0.78,
                        'delivery_performance': 0.88,
                        'quality_rating': 0.93,
                        'capacity_utilization': 0.82,
                        'contract_value_billion_cny': 15.6,
                        'risk_level': 'low',
                        'geographic_location': 'Canada',
                        'backup_suppliers': ['Aptiv', 'ZF_Friedrichshafen']
                    }
                },
                'tier_2_suppliers': {
                    'semiconductor_suppliers': {
                        'count': 25,
                        'avg_reliability': 0.82,
                        'geographic_diversity': 0.65,
                        'total_value_billion_cny': 6.8
                    },
                    'metal_processing': {
                        'count': 18,
                        'avg_reliability': 0.88,
                        'geographic_diversity': 0.70,
                        'total_value_billion_cny': 4.2
                    },
                    'chemical_suppliers': {
                        'count': 12,
                        'avg_reliability': 0.85,
                        'geographic_diversity': 0.55,
                        'total_value_billion_cny': 3.1
                    }
                }
            },
            'logistics_operations': {
                'transportation': {
                    'road_freight': {
                        'cost_per_km_cny': 2.8,
                        'reliability': 0.88,
                        'capacity_utilization': 0.82,
                        'carbon_intensity': 0.75
                    },
                    'rail_freight': {
                        'cost_per_km_cny': 1.2,
                        'reliability': 0.92,
                        'capacity_utilization': 0.75,
                        'carbon_intensity': 0.35
                    },
                    'sea_freight': {
                        'cost_per_km_cny': 0.15,
                        'reliability': 0.85,
                        'capacity_utilization': 0.88,
                        'carbon_intensity': 0.20
                    },
                    'air_freight': {
                        'cost_per_km_cny': 8.5,
                        'reliability': 0.95,
                        'capacity_utilization': 0.65,
                        'carbon_intensity': 1.50
                    }
                },
                'warehousing': {
                    'total_facilities': 45,
                    'total_capacity_million_m3': 2.8,
                    'utilization_rate': 0.78,
                    'automation_level': 0.65,
                    'cost_per_m3_monthly_cny': 25,
                    'inventory_turnover': 8.2
                },
                'distribution_centers': {
                    'domestic_centers': 28,
                    'international_centers': 12,
                    'avg_processing_time_hours': 18,
                    'order_accuracy': 0.96,
                    'cost_efficiency_index': 0.82
                }
            },
            'inventory_management': {
                'raw_materials': {
                    'lithium_carbonate': {
                        'current_stock_tons': 15000,
                        'safety_stock_days': 45,
                        'reorder_point_tons': 8000,
                        'cost_per_ton_cny': 485000,
                        'price_volatility': 0.35
                    },
                    'steel': {
                        'current_stock_tons': 85000,
                        'safety_stock_days': 30,
                        'reorder_point_tons': 45000,
                        'cost_per_ton_cny': 4200,
                        'price_volatility': 0.15
                    },
                    'aluminum': {
                        'current_stock_tons': 25000,
                        'safety_stock_days': 35,
                        'reorder_point_tons': 12000,
                        'cost_per_ton_cny': 18500,
                        'price_volatility': 0.20
                    }
                },
                'work_in_progress': {
                    'battery_modules': {
                        'units': 125000,
                        'value_billion_cny': 2.8,
                        'cycle_time_days': 12
                    },
                    'vehicle_chassis': {
                        'units': 45000,
                        'value_billion_cny': 1.2,
                        'cycle_time_days': 8
                    }
                },
                'finished_goods': {
                    'vehicles_ready_for_delivery': 28000,
                    'battery_packs_inventory': 85000,
                    'total_value_billion_cny': 15.6,
                    'avg_holding_time_days': 22
                }
            },
            'risk_management': {
                'supply_disruption_risks': {
                    'natural_disasters': {
                        'probability': 0.15,
                        'impact_severity': 0.40,
                        'affected_suppliers': ['Ganfeng_Lithium', 'CATL'],
                        'mitigation_cost_million_cny': 125
                    },
                    'geopolitical_tensions': {
                        'probability': 0.25,
                        'impact_severity': 0.60,
                        'affected_suppliers': ['Bosch', 'Magna_International'],
                        'mitigation_cost_million_cny': 280
                    },
                    'cyber_attacks': {
                        'probability': 0.20,
                        'impact_severity': 0.35,
                        'affected_systems': ['logistics_tracking', 'supplier_portals'],
                        'mitigation_cost_million_cny': 85
                    },
                    'pandemic_disruptions': {
                        'probability': 0.10,
                        'impact_severity': 0.50,
                        'affected_operations': ['manufacturing', 'logistics'],
                        'mitigation_cost_million_cny': 350
                    }
                },
                'contingency_plans': {
                    'supplier_diversification': {
                        'implementation_level': 0.75,
                        'effectiveness': 0.68,
                        'cost_premium': 0.08
                    },
                    'inventory_buffering': {
                        'implementation_level': 0.82,
                        'effectiveness': 0.72,
                        'cost_premium': 0.12
                    },
                    'alternative_logistics': {
                        'implementation_level': 0.65,
                        'effectiveness': 0.60,
                        'cost_premium': 0.15
                    }
                }
            },
            'sustainability_metrics': {
                'carbon_footprint': {
                    'total_co2_tons_annually': 285000,
                    'reduction_target': 0.30,
                    'current_progress': 0.18,
                    'green_logistics_adoption': 0.45
                },
                'circular_economy': {
                    'material_recycling_rate': 0.68,
                    'waste_reduction': 0.25,
                    'supplier_sustainability_score': 0.72
                },
                'social_responsibility': {
                    'supplier_labor_standards': 0.85,
                    'local_sourcing_percentage': 0.62,
                    'community_impact_score': 0.78
                }
            },
            'performance_kpis': {
                'cost_efficiency': {
                    'total_supply_chain_cost_billion_cny': 95.2,
                    'cost_as_percentage_of_revenue': 0.42,
                    'year_over_year_cost_reduction': 0.08
                },
                'operational_excellence': {
                    'on_time_delivery_rate': 0.94,
                    'quality_defect_rate': 0.002,
                    'supplier_performance_index': 0.87,
                    'inventory_turnover_ratio': 8.2
                },
                'resilience_metrics': {
                    'supply_chain_flexibility': 0.78,
                    'risk_mitigation_effectiveness': 0.72,
                    'recovery_time_days': 12
                }
            }
        }
        self.initialize()

    def initialize(self):
        print("Supply chain module initialized with comprehensive logistics management.")
        self._initialize_performance_tracking()
        self._setup_risk_monitoring()

    def _initialize_performance_tracking(self):
        """Initialize supply chain performance tracking"""
        self.performance_history = {
            'monthly_costs': [],
            'delivery_performance': [],
            'supplier_ratings': [],
            'disruption_events': []
        }

    def _setup_risk_monitoring(self):
        """Setup supply chain risk monitoring systems"""
        self.risk_alerts = {
            'active_risks': [],
            'mitigation_actions': [],
            'supplier_warnings': []
        }

    def update(self):
        """Comprehensive monthly update of supply chain operations"""
        self._update_supplier_performance()
        self._manage_logistics_operations()
        self._optimize_inventory_levels()
        self._assess_supply_risks()
        self._track_sustainability_metrics()
        self._calculate_performance_kpis()
        
        self.log_data()

    def _update_supplier_performance(self):
        """Update supplier performance metrics and relationships"""
        for supplier, data in self.supply_chain_data['supplier_network']['tier_1_suppliers'].items():
            # Reliability score fluctuations
            reliability_change = random.uniform(-0.03, 0.05)
            data['reliability_score'] = max(0.6, min(1.0, data['reliability_score'] + reliability_change))
            
            # Cost competitiveness adjustments
            cost_change = random.uniform(-0.05, 0.08)
            data['cost_competitiveness'] = max(0.5, min(1.0, data['cost_competitiveness'] + cost_change))
            
            # Delivery performance variations
            delivery_change = random.uniform(-0.04, 0.06)
            data['delivery_performance'] = max(0.7, min(1.0, data['delivery_performance'] + delivery_change))
            
            # Quality rating updates
            quality_change = random.uniform(-0.02, 0.03)
            data['quality_rating'] = max(0.8, min(1.0, data['quality_rating'] + quality_change))
            
            # Capacity utilization adjustments
            capacity_change = random.uniform(-0.08, 0.10)
            data['capacity_utilization'] = max(0.5, min(1.0, data['capacity_utilization'] + capacity_change))
            
            # Risk level assessment
            if data['reliability_score'] < 0.75 or data['delivery_performance'] < 0.80:
                data['risk_level'] = 'high'
            elif data['reliability_score'] > 0.90 and data['delivery_performance'] > 0.90:
                data['risk_level'] = 'low'
            else:
                data['risk_level'] = 'medium'
            
            # Contract value adjustments
            value_change = random.uniform(-0.05, 0.12)
            data['contract_value_billion_cny'] *= (1 + value_change)
        
        # Update tier 2 suppliers
        for category, data in self.supply_chain_data['supplier_network']['tier_2_suppliers'].items():
            reliability_change = random.uniform(-0.02, 0.04)
            data['avg_reliability'] = max(0.7, min(1.0, data['avg_reliability'] + reliability_change))
            
            diversity_change = random.uniform(-0.03, 0.05)
            data['geographic_diversity'] = max(0.4, min(1.0, data['geographic_diversity'] + diversity_change))

    def _manage_logistics_operations(self):
        """Manage and optimize logistics operations"""
        # Transportation mode optimization
        for mode, data in self.supply_chain_data['logistics_operations']['transportation'].items():
            # Cost fluctuations
            cost_change = random.uniform(-0.08, 0.15)
            data['cost_per_km_cny'] *= (1 + cost_change)
            
            # Reliability adjustments
            reliability_change = random.uniform(-0.03, 0.05)
            data['reliability'] = max(0.7, min(1.0, data['reliability'] + reliability_change))
            
            # Capacity utilization optimization
            utilization_change = random.uniform(-0.05, 0.08)
            data['capacity_utilization'] = max(0.5, min(1.0, data['capacity_utilization'] + utilization_change))
        
        # Warehousing efficiency improvements
        warehouse_data = self.supply_chain_data['logistics_operations']['warehousing']
        
        # Utilization rate optimization
        utilization_change = random.uniform(-0.03, 0.06)
        warehouse_data['utilization_rate'] = max(0.6, min(0.95, warehouse_data['utilization_rate'] + utilization_change))
        
        # Automation level progression
        automation_change = random.uniform(0.01, 0.04)
        warehouse_data['automation_level'] = min(1.0, warehouse_data['automation_level'] + automation_change)
        
        # Inventory turnover improvements
        turnover_change = random.uniform(-0.2, 0.5)
        warehouse_data['inventory_turnover'] = max(6.0, warehouse_data['inventory_turnover'] + turnover_change)
        
        # Distribution center performance
        dc_data = self.supply_chain_data['logistics_operations']['distribution_centers']
        
        # Processing time optimization
        time_change = random.uniform(-2, 1)
        dc_data['avg_processing_time_hours'] = max(12, dc_data['avg_processing_time_hours'] + time_change)
        
        # Order accuracy improvements
        accuracy_change = random.uniform(-0.01, 0.02)
        dc_data['order_accuracy'] = max(0.90, min(1.0, dc_data['order_accuracy'] + accuracy_change))

    def _optimize_inventory_levels(self):
        """Optimize inventory levels across all categories"""
        # Raw materials inventory management
        for material, data in self.supply_chain_data['inventory_management']['raw_materials'].items():
            # Stock level adjustments based on demand and supply
            consumption_rate = random.uniform(0.8, 1.2)  # Monthly consumption multiplier
            data['current_stock_tons'] *= (1 - consumption_rate * 0.1)  # Consume inventory
            
            # Reorder logic
            if data['current_stock_tons'] <= data['reorder_point_tons']:
                reorder_quantity = data['safety_stock_days'] * 100  # Simplified reorder calculation
                data['current_stock_tons'] += reorder_quantity
                print(f"Inventory Reorder: {material} - {reorder_quantity} tons ordered")
            
            # Price volatility impact
            price_change = random.uniform(-data['price_volatility'], data['price_volatility'])
            data['cost_per_ton_cny'] *= (1 + price_change)
        
        # Work in progress optimization
        for item, data in self.supply_chain_data['inventory_management']['work_in_progress'].items():
            # Production flow adjustments
            flow_change = random.uniform(-0.1, 0.15)
            data['units'] = int(data['units'] * (1 + flow_change))
            
            # Cycle time improvements
            cycle_improvement = random.uniform(-0.5, 0.2)
            data['cycle_time_days'] = max(5, data['cycle_time_days'] + cycle_improvement)
        
        # Finished goods inventory
        fg_data = self.supply_chain_data['inventory_management']['finished_goods']
        
        # Inventory level adjustments
        demand_change = random.uniform(0.9, 1.1)
        fg_data['vehicles_ready_for_delivery'] = int(fg_data['vehicles_ready_for_delivery'] * demand_change)
        fg_data['battery_packs_inventory'] = int(fg_data['battery_packs_inventory'] * demand_change)
        
        # Holding time optimization
        holding_change = random.uniform(-2, 1)
        fg_data['avg_holding_time_days'] = max(15, fg_data['avg_holding_time_days'] + holding_change)

    def _assess_supply_risks(self):
        """Assess and manage supply chain risks"""
        for risk_type, details in self.supply_chain_data['risk_management']['supply_disruption_risks'].items():
            # Risk probability evolution
            prob_change = random.uniform(-0.02, 0.05)
            details['probability'] = max(0.05, min(0.50, details['probability'] + prob_change))
            
            # Impact severity reassessment
            impact_change = random.uniform(-0.05, 0.08)
            details['impact_severity'] = max(0.20, min(0.80, details['impact_severity'] + impact_change))
            
            # Risk materialization check
            if random.random() < details['probability'] / 12:  # Monthly probability
                print(f"Supply Chain Risk Alert: {risk_type} has occurred (Impact: {details['impact_severity']:.1%})")
                self.performance_history['disruption_events'].append({
                    'date': self.simulation_data['current_date'].isoformat(),
                    'risk_type': risk_type,
                    'impact': details['impact_severity']
                })
                
                # Apply impact to operations
                self._apply_disruption_impact(risk_type, details['impact_severity'])
        
        # Update contingency plan effectiveness
        for plan, details in self.supply_chain_data['risk_management']['contingency_plans'].items():
            # Implementation level progression
            impl_change = random.uniform(0.01, 0.03)
            details['implementation_level'] = min(1.0, details['implementation_level'] + impl_change)
            
            # Effectiveness improvements
            eff_change = random.uniform(-0.02, 0.04)
            details['effectiveness'] = max(0.4, min(0.9, details['effectiveness'] + eff_change))

    def _apply_disruption_impact(self, risk_type, severity):
        """Apply disruption impact to supply chain operations"""
        if risk_type == 'natural_disasters':
            # Impact on raw material suppliers
            for material in ['lithium_carbonate']:
                if material in self.supply_chain_data['inventory_management']['raw_materials']:
                    stock_reduction = severity * 0.3
                    current_stock = self.supply_chain_data['inventory_management']['raw_materials'][material]['current_stock_tons']
                    self.supply_chain_data['inventory_management']['raw_materials'][material]['current_stock_tons'] *= (1 - stock_reduction)
        
        elif risk_type == 'geopolitical_tensions':
            # Impact on international suppliers
            for supplier in ['Bosch', 'Magna_International']:
                if supplier in self.supply_chain_data['supplier_network']['tier_1_suppliers']:
                    reliability_impact = severity * 0.4
                    current_reliability = self.supply_chain_data['supplier_network']['tier_1_suppliers'][supplier]['reliability_score']
                    self.supply_chain_data['supplier_network']['tier_1_suppliers'][supplier]['reliability_score'] *= (1 - reliability_impact)

    def _track_sustainability_metrics(self):
        """Track and update sustainability metrics"""
        sustainability = self.supply_chain_data['sustainability_metrics']
        
        # Carbon footprint reduction progress
        carbon_data = sustainability['carbon_footprint']
        reduction_progress = random.uniform(0.005, 0.02)
        carbon_data['current_progress'] = min(carbon_data['reduction_target'], carbon_data['current_progress'] + reduction_progress)
        
        # Green logistics adoption
        green_adoption_change = random.uniform(0.01, 0.04)
        carbon_data['green_logistics_adoption'] = min(1.0, carbon_data['green_logistics_adoption'] + green_adoption_change)
        
        # Circular economy improvements
        circular_data = sustainability['circular_economy']
        recycling_improvement = random.uniform(0.005, 0.02)
        circular_data['material_recycling_rate'] = min(0.95, circular_data['material_recycling_rate'] + recycling_improvement)
        
        waste_reduction_improvement = random.uniform(0.01, 0.03)
        circular_data['waste_reduction'] = min(0.60, circular_data['waste_reduction'] + waste_reduction_improvement)
        
        # Social responsibility enhancements
        social_data = sustainability['social_responsibility']
        labor_standards_improvement = random.uniform(0.005, 0.02)
        social_data['supplier_labor_standards'] = min(1.0, social_data['supplier_labor_standards'] + labor_standards_improvement)
        
        local_sourcing_change = random.uniform(-0.02, 0.03)
        social_data['local_sourcing_percentage'] = max(0.4, min(0.8, social_data['local_sourcing_percentage'] + local_sourcing_change))

    def _calculate_performance_kpis(self):
        """Calculate comprehensive supply chain performance KPIs"""
        kpis = self.supply_chain_data['performance_kpis']
        
        # Cost efficiency metrics
        cost_data = kpis['cost_efficiency']
        cost_change = random.uniform(-0.03, 0.08)
        cost_data['total_supply_chain_cost_billion_cny'] *= (1 + cost_change)
        
        # Operational excellence metrics
        ops_data = kpis['operational_excellence']
        
        # On-time delivery rate
        delivery_change = random.uniform(-0.02, 0.03)
        ops_data['on_time_delivery_rate'] = max(0.85, min(1.0, ops_data['on_time_delivery_rate'] + delivery_change))
        
        # Quality defect rate
        defect_change = random.uniform(-0.0005, 0.001)
        ops_data['quality_defect_rate'] = max(0.001, min(0.01, ops_data['quality_defect_rate'] + defect_change))
        
        # Supplier performance index
        avg_supplier_performance = np.mean([
            supplier['reliability_score'] * 0.3 + 
            supplier['delivery_performance'] * 0.3 + 
            supplier['quality_rating'] * 0.4
            for supplier in self.supply_chain_data['supplier_network']['tier_1_suppliers'].values()
        ])
        ops_data['supplier_performance_index'] = avg_supplier_performance
        
        # Resilience metrics
        resilience_data = kpis['resilience_metrics']
        
        # Supply chain flexibility
        flexibility_change = random.uniform(-0.02, 0.04)
        resilience_data['supply_chain_flexibility'] = max(0.5, min(1.0, resilience_data['supply_chain_flexibility'] + flexibility_change))
        
        # Risk mitigation effectiveness
        avg_mitigation_effectiveness = np.mean([
            plan['effectiveness'] for plan in self.supply_chain_data['risk_management']['contingency_plans'].values()
        ])
        resilience_data['risk_mitigation_effectiveness'] = avg_mitigation_effectiveness

    def get_performance_metrics(self):
        """Get comprehensive supply chain performance metrics"""
        # Calculate supplier diversity
        tier1_suppliers = len(self.supply_chain_data['supplier_network']['tier_1_suppliers'])
        tier2_suppliers = sum([data['count'] for data in self.supply_chain_data['supplier_network']['tier_2_suppliers'].values()])
        
        # Calculate average supplier performance
        avg_supplier_score = np.mean([
            (supplier['reliability_score'] + supplier['delivery_performance'] + supplier['quality_rating']) / 3
            for supplier in self.supply_chain_data['supplier_network']['tier_1_suppliers'].values()
        ])
        
        # Calculate total inventory value
        raw_materials_value = sum([
            data['current_stock_tons'] * data['cost_per_ton_cny'] / 1000000  # Convert to millions
            for data in self.supply_chain_data['inventory_management']['raw_materials'].values()
        ])
        
        wip_value = sum([
            data['value_billion_cny'] for data in self.supply_chain_data['inventory_management']['work_in_progress'].values()
        ])
        
        fg_value = self.supply_chain_data['inventory_management']['finished_goods']['total_value_billion_cny']
        
        return {
            'supplier_network': {
                'tier1_supplier_count': tier1_suppliers,
                'tier2_supplier_count': tier2_suppliers,
                'average_supplier_performance': avg_supplier_score,
                'high_risk_suppliers': len([s for s in self.supply_chain_data['supplier_network']['tier_1_suppliers'].values() if s['risk_level'] == 'high'])
            },
            'logistics_efficiency': {
                'warehouse_utilization': self.supply_chain_data['logistics_operations']['warehousing']['utilization_rate'],
                'automation_level': self.supply_chain_data['logistics_operations']['warehousing']['automation_level'],
                'order_accuracy': self.supply_chain_data['logistics_operations']['distribution_centers']['order_accuracy'],
                'avg_processing_time': self.supply_chain_data['logistics_operations']['distribution_centers']['avg_processing_time_hours']
            },
            'inventory_management': {
                'total_inventory_value_billion_cny': raw_materials_value + wip_value + fg_value,
                'inventory_turnover': self.supply_chain_data['logistics_operations']['warehousing']['inventory_turnover'],
                'raw_materials_value_million_cny': raw_materials_value,
                'finished_goods_holding_days': self.supply_chain_data['inventory_management']['finished_goods']['avg_holding_time_days']
            },
            'risk_management': {
                'total_risk_exposure': sum([r['probability'] * r['impact_severity'] for r in self.supply_chain_data['risk_management']['supply_disruption_risks'].values()]),
                'mitigation_readiness': np.mean([p['implementation_level'] for p in self.supply_chain_data['risk_management']['contingency_plans'].values()]),
                'disruption_events_count': len(self.performance_history['disruption_events'])
            },
            'sustainability': {
                'carbon_reduction_progress': self.supply_chain_data['sustainability_metrics']['carbon_footprint']['current_progress'],
                'recycling_rate': self.supply_chain_data['sustainability_metrics']['circular_economy']['material_recycling_rate'],
                'local_sourcing_percentage': self.supply_chain_data['sustainability_metrics']['social_responsibility']['local_sourcing_percentage']
            },
            'overall_performance': self.supply_chain_data['performance_kpis']
        }

    def log_data(self):
        """Enhanced logging with comprehensive supply chain data"""
        log_entry = {
            'timestamp': self.simulation_data['current_date'].isoformat(),
            'type': 'SupplyChain',
            'data': self.supply_chain_data,
            'performance_metrics': self.get_performance_metrics(),
            'performance_history': self.performance_history,
            'risk_alerts': self.risk_alerts
        }
        log_path = f"data/supply_chain_{self.simulation_data['current_date'].strftime('%Y%m')}.json"
        with open(log_path, 'w') as f:
            json.dump(log_entry, f, indent=4, default=str)
