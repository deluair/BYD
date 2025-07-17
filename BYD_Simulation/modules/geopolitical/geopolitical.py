import json
import random
import numpy as np
from datetime import datetime, timedelta

class GeopoliticalModule:
    def __init__(self, simulation_data):
        self.simulation_data = simulation_data
        self.config = simulation_data['config']
        self.geopolitical_data = {
            'regional_markets': {
                'China': {
                    'market_access': 1.0,
                    'regulatory_compliance': 0.95,
                    'local_content_requirement': 0.40,
                    'government_support': 0.85,
                    'political_stability': 0.88,
                    'trade_barriers': 0.15,
                    'ev_incentives': 0.75,
                    'manufacturing_restrictions': 0.20
                },
                'United_States': {
                    'market_access': 0.65,
                    'regulatory_compliance': 0.78,
                    'local_content_requirement': 0.50,
                    'government_support': 0.35,
                    'political_stability': 0.82,
                    'trade_barriers': 0.45,
                    'ev_incentives': 0.60,
                    'manufacturing_restrictions': 0.35
                },
                'Europe': {
                    'market_access': 0.80,
                    'regulatory_compliance': 0.85,
                    'local_content_requirement': 0.30,
                    'government_support': 0.70,
                    'political_stability': 0.90,
                    'trade_barriers': 0.25,
                    'ev_incentives': 0.85,
                    'manufacturing_restrictions': 0.15
                },
                'Southeast_Asia': {
                    'market_access': 0.90,
                    'regulatory_compliance': 0.82,
                    'local_content_requirement': 0.25,
                    'government_support': 0.75,
                    'political_stability': 0.75,
                    'trade_barriers': 0.20,
                    'ev_incentives': 0.65,
                    'manufacturing_restrictions': 0.10
                },
                'Latin_America': {
                    'market_access': 0.85,
                    'regulatory_compliance': 0.70,
                    'local_content_requirement': 0.35,
                    'government_support': 0.60,
                    'political_stability': 0.65,
                    'trade_barriers': 0.30,
                    'ev_incentives': 0.45,
                    'manufacturing_restrictions': 0.25
                },
                'Middle_East_Africa': {
                    'market_access': 0.75,
                    'regulatory_compliance': 0.65,
                    'local_content_requirement': 0.20,
                    'government_support': 0.55,
                    'political_stability': 0.60,
                    'trade_barriers': 0.35,
                    'ev_incentives': 0.30,
                    'manufacturing_restrictions': 0.15
                }
            },
            'trade_policies': {
                'tariffs': {
                    'US_Import': 0.25,
                    'EU_Import': 0.10,
                    'ASEAN_Import': 0.05,
                    'RCEP_Benefit': -0.08,
                    'Belt_Road_Benefit': -0.12
                },
                'trade_agreements': {
                    'RCEP': {
                        'status': 'active',
                        'benefit_level': 0.15,
                        'coverage': ['Southeast_Asia', 'China'],
                        'expiry_risk': 0.05
                    },
                    'Belt_Road_Initiative': {
                        'status': 'expanding',
                        'benefit_level': 0.20,
                        'coverage': ['Middle_East_Africa', 'Latin_America', 'Southeast_Asia'],
                        'expiry_risk': 0.10
                    },
                    'CPTPP_Application': {
                        'status': 'pending',
                        'benefit_level': 0.25,
                        'coverage': ['Latin_America', 'Southeast_Asia'],
                        'approval_probability': 0.35
                    }
                },
                'export_controls': {
                    'battery_technology': 0.15,
                    'semiconductor_chips': 0.25,
                    'rare_earth_materials': 0.20,
                    'manufacturing_equipment': 0.10
                }
            },
            'regulatory_environment': {
                'emissions_standards': {
                    'China_NEV': {'compliance_cost': 0.08, 'timeline_pressure': 0.70},
                    'EU_Green_Deal': {'compliance_cost': 0.12, 'timeline_pressure': 0.85},
                    'US_CAFE': {'compliance_cost': 0.10, 'timeline_pressure': 0.60},
                    'Global_Paris_Accord': {'compliance_cost': 0.15, 'timeline_pressure': 0.75}
                },
                'safety_standards': {
                    'UN_ECE': {'compliance_level': 0.92, 'certification_cost': 0.05},
                    'NHTSA': {'compliance_level': 0.88, 'certification_cost': 0.08},
                    'Euro_NCAP': {'compliance_level': 0.90, 'certification_cost': 0.06},
                    'China_CNCAP': {'compliance_level': 0.95, 'certification_cost': 0.04}
                },
                'data_privacy': {
                    'GDPR_Europe': {'compliance_cost': 0.06, 'risk_level': 0.30},
                    'CCPA_California': {'compliance_cost': 0.04, 'risk_level': 0.25},
                    'China_PIPL': {'compliance_cost': 0.05, 'risk_level': 0.20}
                }
            },
            'geopolitical_risks': {
                'trade_war_escalation': {
                    'probability': 0.25,
                    'impact_severity': 0.40,
                    'affected_regions': ['United_States', 'Europe'],
                    'mitigation_strategies': ['supply_chain_diversification', 'local_partnerships']
                },
                'technology_decoupling': {
                    'probability': 0.35,
                    'impact_severity': 0.50,
                    'affected_regions': ['United_States'],
                    'mitigation_strategies': ['indigenous_innovation', 'alternative_suppliers']
                },
                'sanctions_risk': {
                    'probability': 0.15,
                    'impact_severity': 0.60,
                    'affected_regions': ['United_States', 'Europe'],
                    'mitigation_strategies': ['compliance_enhancement', 'legal_structuring']
                },
                'supply_chain_disruption': {
                    'probability': 0.30,
                    'impact_severity': 0.35,
                    'affected_regions': ['Global'],
                    'mitigation_strategies': ['inventory_buffering', 'supplier_diversification']
                }
            },
            'diplomatic_relations': {
                'China_US': {
                    'relationship_score': 0.35,
                    'trend': 'deteriorating',
                    'key_issues': ['trade_deficit', 'technology_transfer', 'market_access'],
                    'dialogue_frequency': 'quarterly'
                },
                'China_EU': {
                    'relationship_score': 0.65,
                    'trend': 'stable',
                    'key_issues': ['market_reciprocity', 'human_rights', 'climate_cooperation'],
                    'dialogue_frequency': 'monthly'
                },
                'China_ASEAN': {
                    'relationship_score': 0.80,
                    'trend': 'improving',
                    'key_issues': ['trade_facilitation', 'infrastructure_development'],
                    'dialogue_frequency': 'weekly'
                }
            },
            'policy_monitoring': {
                'upcoming_elections': {
                    'US_Presidential_2024': {'impact_probability': 0.70, 'policy_change_risk': 0.60},
                    'EU_Parliament_2024': {'impact_probability': 0.40, 'policy_change_risk': 0.30},
                    'Taiwan_Presidential_2024': {'impact_probability': 0.80, 'policy_change_risk': 0.50}
                },
                'legislative_changes': {
                    'US_CHIPS_Act': {'implementation_stage': 0.60, 'impact_level': 0.45},
                    'EU_Critical_Raw_Materials_Act': {'implementation_stage': 0.40, 'impact_level': 0.35},
                    'China_NEV_Policy_Update': {'implementation_stage': 0.80, 'impact_level': 0.25}
                }
            }
        }
        self.initialize()

    def initialize(self):
        print("Geopolitical module initialized with comprehensive policy tracking.")
        self._initialize_risk_monitoring()
        self._setup_compliance_tracking()

    def _initialize_risk_monitoring(self):
        """Initialize geopolitical risk monitoring systems"""
        self.risk_history = {
            'monthly_risk_scores': [],
            'policy_changes': [],
            'trade_disruptions': [],
            'compliance_incidents': []
        }

    def _setup_compliance_tracking(self):
        """Setup regulatory compliance tracking"""
        self.compliance_status = {
            'regional_compliance_scores': {},
            'certification_timeline': {},
            'regulatory_gaps': {},
            'compliance_costs': {}
        }

    def update(self):
        """Comprehensive monthly update of geopolitical landscape"""
        self._update_regional_markets()
        self._monitor_trade_policies()
        self._assess_regulatory_changes()
        self._evaluate_geopolitical_risks()
        self._track_diplomatic_relations()
        self._monitor_policy_developments()
        self._calculate_compliance_metrics()
        
        self.log_data()

    def _update_regional_markets(self):
        """Update regional market conditions and access"""
        for region, metrics in self.geopolitical_data['regional_markets'].items():
            # Market access fluctuations
            access_change = random.uniform(-0.05, 0.03)
            metrics['market_access'] = max(0.1, min(1.0, metrics['market_access'] + access_change))
            
            # Regulatory compliance adjustments
            compliance_change = random.uniform(-0.02, 0.04)
            metrics['regulatory_compliance'] = max(0.5, min(1.0, metrics['regulatory_compliance'] + compliance_change))
            
            # Government support variations
            support_change = random.uniform(-0.08, 0.05)
            metrics['government_support'] = max(0.1, min(1.0, metrics['government_support'] + support_change))
            
            # Political stability assessment
            stability_change = random.uniform(-0.03, 0.02)
            metrics['political_stability'] = max(0.3, min(1.0, metrics['political_stability'] + stability_change))
            
            # Trade barriers evolution
            barrier_change = random.uniform(-0.02, 0.06)
            metrics['trade_barriers'] = max(0.0, min(0.8, metrics['trade_barriers'] + barrier_change))
            
            # EV incentives policy changes
            incentive_change = random.uniform(-0.05, 0.08)
            metrics['ev_incentives'] = max(0.0, min(1.0, metrics['ev_incentives'] + incentive_change))

    def _monitor_trade_policies(self):
        """Monitor and update trade policy changes"""
        # Tariff adjustments
        for tariff_type, rate in self.geopolitical_data['trade_policies']['tariffs'].items():
            if random.random() < 0.08:  # 8% chance of tariff change
                change = random.uniform(-0.05, 0.10)
                new_rate = max(-0.20, min(0.50, rate + change))
                self.geopolitical_data['trade_policies']['tariffs'][tariff_type] = new_rate
                print(f"Trade Policy Update: {tariff_type} tariff changed by {change:+.2%} to {new_rate:.2%}")
        
        # Trade agreement status updates
        for agreement, details in self.geopolitical_data['trade_policies']['trade_agreements'].items():
            # Status progression
            if details['status'] == 'pending' and random.random() < details.get('approval_probability', 0.1) / 12:
                details['status'] = 'active'
                print(f"Trade Agreement Update: {agreement} has been activated")
            
            # Benefit level adjustments
            benefit_change = random.uniform(-0.02, 0.03)
            details['benefit_level'] = max(0.0, min(0.50, details['benefit_level'] + benefit_change))
            
            # Expiry risk assessment
            if details['status'] == 'active' and 'expiry_risk' in details:
                risk_change = random.uniform(-0.01, 0.02)
                details['expiry_risk'] = max(0.0, min(0.30, details['expiry_risk'] + risk_change))
        
        # Export control updates
        for control_type, level in self.geopolitical_data['trade_policies']['export_controls'].items():
            if random.random() < 0.05:  # 5% chance of export control change
                change = random.uniform(-0.03, 0.08)
                new_level = max(0.0, min(0.50, level + change))
                self.geopolitical_data['trade_policies']['export_controls'][control_type] = new_level

    def _assess_regulatory_changes(self):
        """Assess changes in regulatory environment"""
        # Emissions standards updates
        for standard, details in self.geopolitical_data['regulatory_environment']['emissions_standards'].items():
            # Compliance cost fluctuations
            cost_change = random.uniform(-0.01, 0.03)
            details['compliance_cost'] = max(0.02, min(0.25, details['compliance_cost'] + cost_change))
            
            # Timeline pressure adjustments
            pressure_change = random.uniform(-0.05, 0.08)
            details['timeline_pressure'] = max(0.3, min(1.0, details['timeline_pressure'] + pressure_change))
        
        # Safety standards compliance
        for standard, details in self.geopolitical_data['regulatory_environment']['safety_standards'].items():
            # Compliance level improvements
            compliance_change = random.uniform(-0.01, 0.02)
            details['compliance_level'] = max(0.7, min(1.0, details['compliance_level'] + compliance_change))
            
            # Certification cost variations
            cert_cost_change = random.uniform(-0.005, 0.015)
            details['certification_cost'] = max(0.02, min(0.15, details['certification_cost'] + cert_cost_change))
        
        # Data privacy regulation updates
        for regulation, details in self.geopolitical_data['regulatory_environment']['data_privacy'].items():
            # Compliance cost adjustments
            cost_change = random.uniform(-0.01, 0.02)
            details['compliance_cost'] = max(0.02, min(0.12, details['compliance_cost'] + cost_change))
            
            # Risk level fluctuations
            risk_change = random.uniform(-0.03, 0.05)
            details['risk_level'] = max(0.1, min(0.6, details['risk_level'] + risk_change))

    def _evaluate_geopolitical_risks(self):
        """Evaluate and update geopolitical risk assessments"""
        for risk_type, details in self.geopolitical_data['geopolitical_risks'].items():
            # Probability adjustments based on current events
            prob_change = random.uniform(-0.05, 0.08)
            details['probability'] = max(0.05, min(0.70, details['probability'] + prob_change))
            
            # Impact severity reassessment
            impact_change = random.uniform(-0.03, 0.05)
            details['impact_severity'] = max(0.20, min(0.80, details['impact_severity'] + impact_change))
            
            # Risk materialization check
            if random.random() < details['probability'] / 12:  # Monthly probability
                print(f"Geopolitical Risk Alert: {risk_type} risk has materialized (Severity: {details['impact_severity']:.1%})")
                self.risk_history['trade_disruptions'].append({
                    'date': self.simulation_data['current_date'].isoformat(),
                    'risk_type': risk_type,
                    'severity': details['impact_severity']
                })

    def _track_diplomatic_relations(self):
        """Track changes in diplomatic relationships"""
        for relationship, details in self.geopolitical_data['diplomatic_relations'].items():
            # Relationship score evolution
            if details['trend'] == 'improving':
                score_change = random.uniform(0.01, 0.05)
            elif details['trend'] == 'deteriorating':
                score_change = random.uniform(-0.05, -0.01)
            else:  # stable
                score_change = random.uniform(-0.02, 0.02)
            
            details['relationship_score'] = max(0.1, min(1.0, details['relationship_score'] + score_change))
            
            # Trend reassessment
            if random.random() < 0.10:  # 10% chance of trend change
                trends = ['improving', 'stable', 'deteriorating']
                current_index = trends.index(details['trend'])
                new_index = max(0, min(len(trends)-1, current_index + random.choice([-1, 0, 1])))
                details['trend'] = trends[new_index]

    def _monitor_policy_developments(self):
        """Monitor upcoming policy developments and elections"""
        # Election impact assessment
        for election, details in self.geopolitical_data['policy_monitoring']['upcoming_elections'].items():
            # Update impact probability as elections approach
            prob_change = random.uniform(-0.02, 0.05)
            details['impact_probability'] = max(0.2, min(1.0, details['impact_probability'] + prob_change))
            
            # Policy change risk evolution
            risk_change = random.uniform(-0.03, 0.04)
            details['policy_change_risk'] = max(0.1, min(0.8, details['policy_change_risk'] + risk_change))
        
        # Legislative implementation progress
        for legislation, details in self.geopolitical_data['policy_monitoring']['legislative_changes'].items():
            # Implementation stage progression
            stage_progress = random.uniform(0.02, 0.08)
            details['implementation_stage'] = min(1.0, details['implementation_stage'] + stage_progress)
            
            # Impact level reassessment
            impact_change = random.uniform(-0.02, 0.03)
            details['impact_level'] = max(0.1, min(0.7, details['impact_level'] + impact_change))
            
            # Implementation completion check
            if details['implementation_stage'] >= 1.0 and random.random() < 0.20:
                print(f"Policy Implementation: {legislation} has been fully implemented (Impact: {details['impact_level']:.1%})")

    def _calculate_compliance_metrics(self):
        """Calculate comprehensive compliance metrics"""
        # Regional compliance scores
        for region in self.geopolitical_data['regional_markets'].keys():
            market_data = self.geopolitical_data['regional_markets'][region]
            compliance_score = (
                market_data['regulatory_compliance'] * 0.4 +
                market_data['market_access'] * 0.3 +
                (1 - market_data['trade_barriers']) * 0.3
            )
            self.compliance_status['regional_compliance_scores'][region] = compliance_score
        
        # Overall compliance costs
        total_compliance_cost = 0
        for category in self.geopolitical_data['regulatory_environment'].values():
            for standard, details in category.items():
                if 'compliance_cost' in details:
                    total_compliance_cost += details['compliance_cost']
                if 'certification_cost' in details:
                    total_compliance_cost += details['certification_cost']
        
        self.compliance_status['total_compliance_cost'] = total_compliance_cost
        
        # Risk-adjusted market access score
        risk_weighted_access = 0
        total_weight = 0
        for region, market_data in self.geopolitical_data['regional_markets'].items():
            weight = market_data['market_access'] * market_data['political_stability']
            risk_weighted_access += weight * (1 - market_data['trade_barriers'])
            total_weight += weight
        
        self.compliance_status['risk_adjusted_market_access'] = risk_weighted_access / total_weight if total_weight > 0 else 0

    def get_performance_metrics(self):
        """Get comprehensive geopolitical performance metrics"""
        # Calculate average regional scores
        avg_market_access = np.mean([data['market_access'] for data in self.geopolitical_data['regional_markets'].values()])
        avg_compliance = np.mean([data['regulatory_compliance'] for data in self.geopolitical_data['regional_markets'].values()])
        avg_political_stability = np.mean([data['political_stability'] for data in self.geopolitical_data['regional_markets'].values()])
        avg_trade_barriers = np.mean([data['trade_barriers'] for data in self.geopolitical_data['regional_markets'].values()])
        
        # Calculate risk exposure
        total_risk_exposure = sum([
            risk['probability'] * risk['impact_severity'] 
            for risk in self.geopolitical_data['geopolitical_risks'].values()
        ])
        
        # Calculate diplomatic strength
        diplomatic_strength = np.mean([
            rel['relationship_score'] for rel in self.geopolitical_data['diplomatic_relations'].values()
        ])
        
        return {
            'market_access': {
                'average_access_score': avg_market_access,
                'compliance_score': avg_compliance,
                'political_stability': avg_political_stability,
                'trade_barrier_level': avg_trade_barriers
            },
            'trade_policy': {
                'average_tariff_rate': np.mean(list(self.geopolitical_data['trade_policies']['tariffs'].values())),
                'active_agreements': len([a for a in self.geopolitical_data['trade_policies']['trade_agreements'].values() if a['status'] == 'active']),
                'export_control_intensity': np.mean(list(self.geopolitical_data['trade_policies']['export_controls'].values()))
            },
            'regulatory_burden': {
                'total_compliance_cost': self.compliance_status.get('total_compliance_cost', 0),
                'regulatory_complexity': len(self.geopolitical_data['regulatory_environment']),
                'certification_requirements': sum([len(cat) for cat in self.geopolitical_data['regulatory_environment'].values()])
            },
            'risk_assessment': {
                'total_risk_exposure': total_risk_exposure,
                'high_probability_risks': len([r for r in self.geopolitical_data['geopolitical_risks'].values() if r['probability'] > 0.4]),
                'diplomatic_strength': diplomatic_strength
            },
            'compliance_status': self.compliance_status
        }

    def log_data(self):
        """Enhanced logging with comprehensive geopolitical data"""
        log_entry = {
            'timestamp': self.simulation_data['current_date'].isoformat(),
            'type': 'Geopolitical',
            'data': self.geopolitical_data,
            'performance_metrics': self.get_performance_metrics(),
            'risk_history': self.risk_history,
            'compliance_status': self.compliance_status
        }
        log_path = f"data/geopolitical_{self.simulation_data['current_date'].strftime('%Y%m')}.json"
        with open(log_path, 'w') as f:
            json.dump(log_entry, f, indent=4, default=str)
