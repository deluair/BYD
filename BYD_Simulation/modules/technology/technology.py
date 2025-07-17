import json
import random
import numpy as np
from datetime import datetime, timedelta

class TechnologyModule:
    def __init__(self, simulation_data):
        self.simulation_data = simulation_data
        self.config = simulation_data['config']
        self.technology_data = {
            'rd_staff': 104003,
            'patents': {
                'total': 13000,
                'filed_this_year': 2850,
                'by_category': {
                    'Battery_Technology': 4200,
                    'Automotive_Electronics': 3100,
                    'ADAS_Autonomous': 2800,
                    'Manufacturing_Process': 1900,
                    'Energy_Storage': 1000
                },
                'international': {
                    'US': 2100,
                    'Europe': 1800,
                    'Japan': 950,
                    'Other': 650
                }
            },
            'rd_investment': {
                'total_billion_cny': 18.5,
                'by_division': {
                    'Automotive': 8.2,
                    'Battery': 6.1,
                    'Electronics': 2.8,
                    'Energy_Storage': 1.4
                },
                'by_stage': {
                    'Basic_Research': 0.15,
                    'Applied_Research': 0.35,
                    'Development': 0.40,
                    'Testing_Validation': 0.10
                }
            },
            'research_centers': {
                'Shenzhen_HQ': {
                    'staff': 25000,
                    'focus': ['Battery_Chemistry', 'Power_Electronics'],
                    'budget_billion_cny': 5.2,
                    'breakthrough_probability': 0.08
                },
                'Shanghai_Auto': {
                    'staff': 18500,
                    'focus': ['ADAS', 'Autonomous_Driving', 'Vehicle_Integration'],
                    'budget_billion_cny': 4.1,
                    'breakthrough_probability': 0.06
                },
                'Beijing_AI': {
                    'staff': 12000,
                    'focus': ['AI_Algorithms', 'Machine_Learning', 'Data_Analytics'],
                    'budget_billion_cny': 3.8,
                    'breakthrough_probability': 0.09
                },
                'Xian_Manufacturing': {
                    'staff': 8500,
                    'focus': ['Process_Innovation', 'Automation', 'Quality_Systems'],
                    'budget_billion_cny': 2.1,
                    'breakthrough_probability': 0.05
                },
                'International_Labs': {
                    'staff': 6200,
                    'focus': ['Global_Standards', 'Localization', 'Partnerships'],
                    'budget_billion_cny': 1.8,
                    'breakthrough_probability': 0.04
                }
            },
            'innovation_pipeline': {
                'concept_stage': [
                    {'name': 'Solid_State_Battery_Gen3', 'progress': 0.25, 'potential_impact': 0.35},
                    {'name': 'AI_Predictive_Maintenance', 'progress': 0.40, 'potential_impact': 0.20},
                    {'name': 'Wireless_Charging_Highway', 'progress': 0.15, 'potential_impact': 0.45}
                ],
                'development_stage': [
                    {'name': 'LFP_Energy_Density_Plus', 'progress': 0.75, 'potential_impact': 0.25},
                    {'name': 'Level4_Autonomous_Stack', 'progress': 0.68, 'potential_impact': 0.40},
                    {'name': 'Blade_Battery_2.0', 'progress': 0.82, 'potential_impact': 0.30}
                ],
                'testing_stage': [
                    {'name': 'Cell_to_Pack_Integration', 'progress': 0.92, 'potential_impact': 0.22},
                    {'name': 'Advanced_BMS_AI', 'progress': 0.88, 'potential_impact': 0.18}
                ]
            },
            'technology_partnerships': {
                'Universities': {
                    'Tsinghua': {'projects': 15, 'budget_million_cny': 120},
                    'MIT': {'projects': 8, 'budget_million_cny': 85},
                    'Stanford': {'projects': 6, 'budget_million_cny': 95},
                    'Cambridge': {'projects': 4, 'budget_million_cny': 60}
                },
                'Industry': {
                    'NVIDIA': {'focus': 'AI_Computing', 'investment_million_cny': 250},
                    'Qualcomm': {'focus': 'Automotive_Chips', 'investment_million_cny': 180},
                    'Bosch': {'focus': 'Sensor_Technology', 'investment_million_cny': 150}
                }
            },
            'competitive_intelligence': {
                'Tesla': {'patent_activity': 'high', 'focus_areas': ['FSD', 'Battery_Manufacturing']},
                'Toyota': {'patent_activity': 'medium', 'focus_areas': ['Solid_State', 'Hydrogen']},
                'Volkswagen': {'patent_activity': 'medium', 'focus_areas': ['Platform_Integration', 'Software']},
                'CATL': {'patent_activity': 'high', 'focus_areas': ['Battery_Chemistry', 'Manufacturing']}
            },
            'innovation_metrics': {
                'time_to_market_months': 18,
                'success_rate': 0.68,
                'patent_citation_index': 2.4,
                'technology_transfer_rate': 0.72,
                'rd_efficiency_score': 0.78
            }
        }
        self.initialize()

    def initialize(self):
        print("Technology module initialized with comprehensive R&D capabilities.")
        self._initialize_technology_trends()
        self._setup_innovation_tracking()

    def _initialize_technology_trends(self):
        """Initialize technology trend tracking"""
        self.technology_trends = {
            'battery_energy_density': 1.0,
            'autonomous_driving_capability': 1.0,
            'ai_integration': 1.0,
            'manufacturing_automation': 1.0,
            'sustainability_focus': 1.0
        }

    def _setup_innovation_tracking(self):
        """Setup innovation performance tracking"""
        self.innovation_history = {
            'monthly_patents': [],
            'breakthrough_timeline': [],
            'investment_efficiency': [],
            'competitive_position': []
        }

    def update(self):
        """Comprehensive monthly update of technology operations"""
        self._update_rd_activities()
        self._process_innovation_pipeline()
        self._manage_patent_portfolio()
        self._update_research_centers()
        self._assess_partnerships()
        self._analyze_competitive_landscape()
        self._calculate_innovation_metrics()
        
        self.log_data()

    def _update_rd_activities(self):
        """Update R&D activities and investments"""
        # Adjust R&D investment based on business performance
        revenue_growth = random.uniform(0.05, 0.15)
        investment_adjustment = 1 + (revenue_growth * 0.5)
        
        self.technology_data['rd_investment']['total_billion_cny'] *= investment_adjustment
        
        # Update staff allocation
        staff_change = random.uniform(-0.02, 0.08)
        self.technology_data['rd_staff'] = int(self.technology_data['rd_staff'] * (1 + staff_change))
        
        # Technology trend influence
        for trend, value in self.technology_trends.items():
            trend_growth = random.uniform(0.02, 0.12)
            self.technology_trends[trend] *= (1 + trend_growth)

    def _process_innovation_pipeline(self):
        """Process innovation pipeline and project progression"""
        # Advance projects through pipeline stages
        for stage in ['concept_stage', 'development_stage', 'testing_stage']:
            projects = self.technology_data['innovation_pipeline'][stage]
            
            for project in projects[:]:
                # Progress advancement
                progress_increase = random.uniform(0.02, 0.08)
                project['progress'] = min(1.0, project['progress'] + progress_increase)
                
                # Stage graduation
                if project['progress'] >= 0.95:
                    if stage == 'concept_stage':
                        projects.remove(project)
                        project['progress'] = 0.05
                        self.technology_data['innovation_pipeline']['development_stage'].append(project)
                    elif stage == 'development_stage':
                        projects.remove(project)
                        project['progress'] = 0.05
                        self.technology_data['innovation_pipeline']['testing_stage'].append(project)
                    else:  # testing_stage
                        projects.remove(project)
                        self._commercialize_innovation(project)
        
        # Generate new concept projects
        if random.random() < 0.20:  # 20% chance of new concept
            new_concepts = [
                'Next_Gen_Silicon_Anode',
                'Quantum_Dot_Solar_Integration',
                'Bio_Inspired_Battery_Design',
                'Edge_AI_Vehicle_Computing',
                'Sustainable_Material_Recovery'
            ]
            new_project = {
                'name': random.choice(new_concepts),
                'progress': random.uniform(0.05, 0.20),
                'potential_impact': random.uniform(0.15, 0.50)
            }
            self.technology_data['innovation_pipeline']['concept_stage'].append(new_project)

    def _commercialize_innovation(self, project):
        """Handle commercialization of completed innovations"""
        print(f"Technology Breakthrough: {project['name']} ready for commercialization (Impact: {project['potential_impact']:.1%})")
        
        # Add to breakthrough timeline
        breakthrough = {
            'date': self.simulation_data['current_date'].isoformat(),
            'innovation': project['name'],
            'impact': project['potential_impact'],
            'commercialization_timeline': random.randint(6, 24)  # months
        }
        self.innovation_history['breakthrough_timeline'].append(breakthrough)

    def _manage_patent_portfolio(self):
        """Manage patent filing and portfolio optimization"""
        # Monthly patent filing
        base_patents = 120
        rd_intensity_factor = self.technology_data['rd_investment']['total_billion_cny'] / 18.5
        innovation_factor = len(self.technology_data['innovation_pipeline']['development_stage']) / 3
        
        monthly_patents = int(base_patents * rd_intensity_factor * innovation_factor * random.uniform(0.8, 1.3))
        self.technology_data['patents']['total'] += monthly_patents
        self.technology_data['patents']['filed_this_year'] += monthly_patents
        
        # Update patent categories based on current focus
        categories = list(self.technology_data['patents']['by_category'].keys())
        for category in categories:
            category_patents = int(monthly_patents * random.uniform(0.15, 0.35))
            self.technology_data['patents']['by_category'][category] += category_patents
        
        # International filing strategy
        international_ratio = 0.4
        international_patents = int(monthly_patents * international_ratio)
        regions = list(self.technology_data['patents']['international'].keys())
        for region in regions:
            region_patents = int(international_patents * random.uniform(0.2, 0.4))
            self.technology_data['patents']['international'][region] += region_patents
        
        # Track monthly patent activity
        self.innovation_history['monthly_patents'].append({
            'month': self.simulation_data['current_date'].isoformat(),
            'patents_filed': monthly_patents
        })

    def _update_research_centers(self):
        """Update research center performance and capabilities"""
        for center, data in self.technology_data['research_centers'].items():
            # Staff adjustments
            staff_change = random.uniform(-0.03, 0.08)
            data['staff'] = int(data['staff'] * (1 + staff_change))
            
            # Budget allocation
            budget_change = random.uniform(-0.05, 0.12)
            data['budget_billion_cny'] *= (1 + budget_change)
            
            # Breakthrough probability based on investment and focus
            base_prob = data['breakthrough_probability']
            investment_factor = data['budget_billion_cny'] / 3.0  # Normalized
            data['breakthrough_probability'] = min(0.15, base_prob * investment_factor)
            
            # Check for breakthroughs
            if random.random() < data['breakthrough_probability']:
                focus_area = random.choice(data['focus'])
                print(f"Research Breakthrough at {center}: {focus_area} advancement")

    def _assess_partnerships(self):
        """Assess and update technology partnerships"""
        # University partnerships
        for university, data in self.technology_data['technology_partnerships']['Universities'].items():
            # Project completion and new projects
            if random.random() < 0.15:  # 15% chance of project completion
                data['projects'] = max(1, data['projects'] - 1)
            
            if random.random() < 0.10:  # 10% chance of new project
                data['projects'] += 1
                data['budget_million_cny'] *= random.uniform(1.05, 1.15)
        
        # Industry partnerships
        for partner, data in self.technology_data['technology_partnerships']['Industry'].items():
            # Investment adjustments
            investment_change = random.uniform(-0.10, 0.20)
            data['investment_million_cny'] *= (1 + investment_change)

    def _analyze_competitive_landscape(self):
        """Analyze competitive technology landscape"""
        for competitor, data in self.technology_data['competitive_intelligence'].items():
            # Update patent activity
            activity_levels = ['low', 'medium', 'high', 'very_high']
            if random.random() < 0.15:  # 15% chance of activity change
                current_index = activity_levels.index(data['patent_activity'])
                new_index = max(0, min(len(activity_levels)-1, current_index + random.choice([-1, 0, 1])))
                data['patent_activity'] = activity_levels[new_index]

    def _calculate_innovation_metrics(self):
        """Calculate innovation performance metrics"""
        metrics = self.technology_data['innovation_metrics']
        
        # Time to market improvement
        efficiency_gain = random.uniform(-0.5, 1.0)  # months
        metrics['time_to_market_months'] = max(12, metrics['time_to_market_months'] + efficiency_gain)
        
        # Success rate based on investment and pipeline health
        pipeline_health = len(self.technology_data['innovation_pipeline']['development_stage']) / 5
        investment_factor = self.technology_data['rd_investment']['total_billion_cny'] / 20.0
        metrics['success_rate'] = min(0.85, metrics['success_rate'] * (1 + (pipeline_health + investment_factor) * 0.02))
        
        # Patent citation index
        citation_change = random.uniform(-0.1, 0.2)
        metrics['patent_citation_index'] = max(1.0, metrics['patent_citation_index'] + citation_change)
        
        # Technology transfer rate
        transfer_change = random.uniform(-0.02, 0.05)
        metrics['technology_transfer_rate'] = max(0.5, min(0.9, metrics['technology_transfer_rate'] + transfer_change))
        
        # R&D efficiency score
        patents_per_investment = self.technology_data['patents']['filed_this_year'] / self.technology_data['rd_investment']['total_billion_cny']
        normalized_efficiency = min(1.0, patents_per_investment / 200)  # Normalize to 0-1
        metrics['rd_efficiency_score'] = (metrics['rd_efficiency_score'] * 0.8) + (normalized_efficiency * 0.2)

    def get_performance_metrics(self):
        """Get comprehensive technology performance metrics"""
        total_pipeline_projects = sum(len(projects) for projects in self.technology_data['innovation_pipeline'].values())
        avg_project_progress = np.mean([
            project['progress'] for stage_projects in self.technology_data['innovation_pipeline'].values() 
            for project in stage_projects
        ]) if total_pipeline_projects > 0 else 0
        
        return {
            'rd_investment': self.technology_data['rd_investment']['total_billion_cny'],
            'patent_portfolio': {
                'total_patents': self.technology_data['patents']['total'],
                'annual_filing_rate': self.technology_data['patents']['filed_this_year'],
                'international_coverage': sum(self.technology_data['patents']['international'].values())
            },
            'innovation_pipeline': {
                'total_projects': total_pipeline_projects,
                'avg_progress': avg_project_progress,
                'breakthrough_potential': np.mean([
                    project['potential_impact'] for stage_projects in self.technology_data['innovation_pipeline'].values() 
                    for project in stage_projects
                ]) if total_pipeline_projects > 0 else 0
            },
            'research_capability': {
                'total_rd_staff': self.technology_data['rd_staff'],
                'research_centers': len(self.technology_data['research_centers']),
                'partnership_strength': len(self.technology_data['technology_partnerships']['Universities']) + 
                                      len(self.technology_data['technology_partnerships']['Industry'])
            },
            'innovation_efficiency': self.technology_data['innovation_metrics']
        }

    def get_technology_metrics(self):
        """Get technology-specific metrics for main simulation tracking"""
        total_pipeline_projects = sum(len(projects) for projects in self.technology_data['innovation_pipeline'].values())
        
        return {
            'rd_investment_billion_cny': self.technology_data['rd_investment']['total_billion_cny'],
            'total_patents': self.technology_data['patents']['total'],
            'patents_filed_this_year': self.technology_data['patents']['filed_this_year'],
            'rd_staff_count': self.technology_data['rd_staff'],
            'innovation_pipeline_projects': total_pipeline_projects,
            'innovation_metrics': self.technology_data['innovation_metrics'],
            'research_centers_count': len(self.technology_data['research_centers']),
            'technology_partnerships': {
                'universities': len(self.technology_data['technology_partnerships']['Universities']),
                'industry': len(self.technology_data['technology_partnerships']['Industry'])
            }
        }

    def log_data(self):
        """Enhanced logging with comprehensive technology data"""
        log_entry = {
            'timestamp': self.simulation_data['current_date'].isoformat(),
            'type': 'Technology',
            'data': self.technology_data,
            'performance_metrics': self.get_performance_metrics(),
            'technology_trends': self.technology_trends,
            'innovation_history': self.innovation_history
        }
        log_path = f"data/technology_{self.simulation_data['current_date'].strftime('%Y%m')}.json"
        with open(log_path, 'w') as f:
            json.dump(log_entry, f, indent=4, default=str)
