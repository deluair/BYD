import json
import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
from dateutil.relativedelta import relativedelta

from modules.automotive.automotive import AutomotiveModule
from modules.battery.battery import BatteryModule
from modules.finance.finance import FinanceModule
from modules.electronics.electronics import ElectronicsModule
from modules.energy_storage.energy_storage import EnergyStorageModule
from modules.geopolitical.geopolitical import GeopoliticalModule
from modules.supply_chain.supply_chain import SupplyChainModule
from modules.technology.technology import TechnologyModule

class Simulation:
    def __init__(self, config_path='config/simulation_config.json'):
        with open(config_path) as f:
            self.config = json.load(f)
        
        self.simulation_data = {
            'config': self.config,
            'current_date': datetime.strptime(self.config['simulation']['start_date'], '%Y-%m-%d'),
            'end_date': datetime.strptime(self.config['simulation']['end_date'], '%Y-%m-%d'),
            'time_step': self.config['simulation']['time_step'],
            'results': [],
            'kpis': [],
            'alerts': [],
            'scenarios': []
        }

        # Create enhanced directory structure
        self._create_directories()
        
        # Initialize enhanced modules
        print("Initializing BYD Global Mobility Simulation...")
        print(f"Simulation period: {self.config['simulation']['start_date']} to {self.config['simulation']['end_date']}")
        print(f"Base currency: {self.config.get('base_currency', 'CNY')}")
        
        self.automotive = AutomotiveModule(self.simulation_data)
        self.battery = BatteryModule(self.simulation_data)
        self.electronics = ElectronicsModule(self.simulation_data)
        self.energy_storage = EnergyStorageModule(self.simulation_data)
        self.geopolitical = GeopoliticalModule(self.simulation_data)
        self.supply_chain = SupplyChainModule(self.simulation_data)
        self.technology = TechnologyModule(self.simulation_data)
        
        # Initialize finance module with all business units
        self.finance = FinanceModule(
            self.simulation_data, 
            self.automotive, 
            self.battery, 
            self.electronics, 
            self.energy_storage
        )
        
        # Initialize performance tracking
        self.performance_metrics = {
            'monthly_revenue': [],
            'monthly_profit': [],
            'monthly_production': [],
            'market_share': [],
            'customer_satisfaction': [],
            'supply_chain_efficiency': [],
            'innovation_index': []
        }
        
        print("✅ All modules initialized successfully!")
    
    def _create_directories(self):
        """Create enhanced directory structure for simulation outputs"""
        directories = [
            'data',
            'data/automotive',
            'data/battery', 
            'data/financial',
            'data/supply_chain',
            'data/technology',
            'reports',
            'reports/monthly',
            'reports/quarterly',
            'reports/annual',
            'visualizations',
            'exports'
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
    
    def _update_performance_metrics(self):
        """Update key performance indicators"""
        # Get latest financial data
        financial_metrics = self.finance.get_financial_summary()
        
        # Get automotive metrics
        auto_metrics = self.automotive.get_financial_metrics()
        
        # Get battery metrics
        battery_metrics = self.battery.get_financial_metrics()
        
        # Update tracking
        self.performance_metrics['monthly_revenue'].append(financial_metrics.get('total_revenue', 0))
        self.performance_metrics['monthly_profit'].append(financial_metrics.get('net_profit', 0))
        
        # Calculate total production (vehicles + batteries)
        total_vehicle_production = sum(sum(model.values()) for model in auto_metrics.get('production_by_model', {}).values())
        total_battery_production = battery_metrics.get('total_production_gwh', 0)
        
        self.performance_metrics['monthly_production'].append({
            'vehicles': total_vehicle_production,
            'batteries_gwh': total_battery_production
        })
        
        # Market share and satisfaction from automotive
        market_metrics = self.automotive.get_market_metrics()
        self.performance_metrics['market_share'].append(market_metrics.get('market_share', 0))
        self.performance_metrics['customer_satisfaction'].append(market_metrics.get('customer_satisfaction', 0))
        
        # Supply chain efficiency (simplified)
        supply_efficiency = 1 - battery_metrics.get('supply_chain_risk_score', 0)
        self.performance_metrics['supply_chain_efficiency'].append(supply_efficiency)
        
        # Innovation index based on technology advancement
        tech_data = self.technology.get_technology_metrics()
        innovation_score = tech_data.get('innovation_index', 0.5)
        self.performance_metrics['innovation_index'].append(innovation_score)
    
    def _generate_alerts(self):
        """Generate business alerts based on performance thresholds"""
        alerts = []
        current_date = self.simulation_data['current_date']
        
        # Financial alerts
        if self.performance_metrics['monthly_profit']:
            latest_profit = self.performance_metrics['monthly_profit'][-1]
            if len(self.performance_metrics['monthly_profit']) > 1:
                previous_profit = self.performance_metrics['monthly_profit'][-2]
                profit_change = (latest_profit - previous_profit) / previous_profit if previous_profit != 0 else 0
                
                if profit_change < -0.1:  # 10% decline
                    alerts.append({
                        'type': 'FINANCIAL_WARNING',
                        'message': f'Profit declined by {profit_change*100:.1f}% this month',
                        'severity': 'HIGH',
                        'date': current_date.isoformat()
                    })
        
        # Market share alerts
        if self.performance_metrics['market_share']:
            latest_share = self.performance_metrics['market_share'][-1]
            if latest_share < 0.15:  # Below 15% market share
                alerts.append({
                    'type': 'MARKET_WARNING',
                    'message': f'Market share dropped to {latest_share*100:.1f}%',
                    'severity': 'MEDIUM',
                    'date': current_date.isoformat()
                })
        
        # Supply chain alerts
        if self.performance_metrics['supply_chain_efficiency']:
            latest_efficiency = self.performance_metrics['supply_chain_efficiency'][-1]
            if latest_efficiency < 0.8:  # Below 80% efficiency
                alerts.append({
                    'type': 'SUPPLY_CHAIN_WARNING',
                    'message': f'Supply chain efficiency at {latest_efficiency*100:.1f}%',
                    'severity': 'HIGH',
                    'date': current_date.isoformat()
                })
        
        # Customer satisfaction alerts
        if self.performance_metrics['customer_satisfaction']:
            latest_satisfaction = self.performance_metrics['customer_satisfaction'][-1]
            if latest_satisfaction < 0.8:  # Below 80% satisfaction
                alerts.append({
                    'type': 'CUSTOMER_WARNING',
                    'message': f'Customer satisfaction at {latest_satisfaction*100:.1f}%',
                    'severity': 'MEDIUM',
                    'date': current_date.isoformat()
                })
        
        self.simulation_data['alerts'].extend(alerts)
        
        # Print critical alerts
        for alert in alerts:
            if alert['severity'] == 'HIGH':
                print(f"🚨 {alert['type']}: {alert['message']}")
    
    def _save_monthly_snapshot(self):
        """Save comprehensive monthly snapshot"""
        current_date = self.simulation_data['current_date']
        
        snapshot = {
            'date': current_date.isoformat(),
            'automotive_metrics': self.automotive.get_financial_metrics(),
            'battery_metrics': self.battery.get_financial_metrics(),
            'financial_summary': self.finance.get_financial_summary(),
            'market_metrics': self.automotive.get_market_metrics(),
            'technology_metrics': self.technology.get_technology_metrics(),
            'performance_kpis': {
                'revenue': self.performance_metrics['monthly_revenue'][-1] if self.performance_metrics['monthly_revenue'] else 0,
                'profit': self.performance_metrics['monthly_profit'][-1] if self.performance_metrics['monthly_profit'] else 0,
                'market_share': self.performance_metrics['market_share'][-1] if self.performance_metrics['market_share'] else 0,
                'customer_satisfaction': self.performance_metrics['customer_satisfaction'][-1] if self.performance_metrics['customer_satisfaction'] else 0
            },
            'alerts': [alert for alert in self.simulation_data['alerts'] if alert['date'] == current_date.isoformat()]
        }
        
        # Save to file
        filename = f"data/monthly_snapshot_{current_date.strftime('%Y%m')}.json"
        with open(filename, 'w') as f:
            json.dump(snapshot, f, indent=2, default=str)
        
        return snapshot

    def run(self, scenario='baseline'):
        """Run the enhanced simulation with comprehensive analytics"""
        print(f"\n🚀 Starting BYD Business Simulation - {scenario.upper()} scenario")
        print(f"📅 Simulation period: {self.simulation_data['current_date'].date()} to {self.simulation_data['end_date'].date()}")
        print("="*60)
        
        # Set scenario parameters
        self.simulation_data['scenarios'].append({
            'name': scenario,
            'market_growth_rate': 0.15 if scenario == 'optimistic' else 0.08 if scenario == 'baseline' else 0.03,
            'competition_intensity': 0.6 if scenario == 'optimistic' else 0.8 if scenario == 'baseline' else 1.0,
            'supply_chain_stability': 0.9 if scenario == 'optimistic' else 0.8 if scenario == 'baseline' else 0.6,
            'regulatory_support': 0.8 if scenario == 'optimistic' else 0.6 if scenario == 'baseline' else 0.4
        })
        
        month_count = 0
        quarterly_snapshots = []
        
        while self.simulation_data['current_date'] <= self.simulation_data['end_date']:
            month_count += 1
            print(f"\n📊 Month {month_count}: {self.simulation_data['current_date'].strftime('%B %Y')}")
            print("-" * 40)
            
            # Update each module with enhanced logic
            print("🔄 Updating modules...")
            
            # Technology updates (affects other modules)
            self.technology.update()
            
            # Production updates with capacity optimization
            self.automotive.update_production()
            self.battery.update_production()
            self.electronics.update()
            self.energy_storage.update()
            
            # Market and supply chain updates
            self.geopolitical.update()
            self.supply_chain.update()
            
            # Financial consolidation with enhanced metrics
            self.finance.update_financials()
            
            # Update performance metrics and generate alerts
            self._update_performance_metrics()
            self._generate_alerts()
            
            # Save monthly snapshot
            monthly_snapshot = self._save_monthly_snapshot()
            
            # Quarterly reporting
            if month_count % 3 == 0:
                quarterly_data = self._generate_quarterly_report(month_count // 3)
                quarterly_snapshots.append(quarterly_data)
                print(f"📋 Quarterly report Q{month_count // 3} generated")
            
            # Annual reporting
            if month_count % 12 == 0:
                annual_data = self._generate_annual_report(month_count // 12)
                print(f"📊 Annual report Year {month_count // 12} generated")
            
            # Advance time
            if self.simulation_data['time_step'] == 'month':
                self.simulation_data['current_date'] += relativedelta(months=1)
        
        print("\n✅ Simulation completed successfully!")
        print(f"📈 Generated {month_count} months of comprehensive data")
        print(f"🚨 Generated {len(self.simulation_data['alerts'])} business alerts")
        
        # Generate final comprehensive report
        self.generate_report()
        
        return {
            'scenario': scenario,
            'months_simulated': month_count,
            'alerts_generated': len(self.simulation_data['alerts']),
            'performance_summary': {
                'final_revenue': self.performance_metrics['monthly_revenue'][-1] if self.performance_metrics['monthly_revenue'] else 0,
                'final_profit': self.performance_metrics['monthly_profit'][-1] if self.performance_metrics['monthly_profit'] else 0,
                'final_market_share': self.performance_metrics['market_share'][-1] if self.performance_metrics['market_share'] else 0
            }
        }

    def _generate_quarterly_report(self, quarter):
        """Generate detailed quarterly report"""
        current_date = self.simulation_data['current_date']
        
        # Calculate quarterly metrics
        quarterly_data = {
            'quarter': quarter,
            'year': current_date.year,
            'period': f"Q{quarter} {current_date.year}",
            'automotive_performance': self.automotive.get_financial_metrics(),
            'battery_performance': self.battery.get_financial_metrics(),
            'financial_summary': self.finance.get_financial_summary(),
            'market_analysis': self.automotive.get_market_metrics(),
            'technology_progress': self.technology.get_technology_metrics(),
            'kpi_trends': {
                'revenue_growth': self._calculate_growth_rate(self.performance_metrics['monthly_revenue'], 3),
                'profit_growth': self._calculate_growth_rate(self.performance_metrics['monthly_profit'], 3),
                'market_share_change': self._calculate_change(self.performance_metrics['market_share'], 3)
            }
        }
        
        # Save quarterly report
        filename = f"reports/quarterly/Q{quarter}_{current_date.year}_report.json"
        with open(filename, 'w') as f:
            json.dump(quarterly_data, f, indent=2, default=str)
        
        return quarterly_data
    
    def _generate_annual_report(self, year):
        """Generate comprehensive annual report"""
        annual_data = {
            'year': year + self.simulation_data['current_date'].year - 1,
            'summary': {
                'total_revenue': sum(self.performance_metrics['monthly_revenue'][-12:]) if len(self.performance_metrics['monthly_revenue']) >= 12 else sum(self.performance_metrics['monthly_revenue']),
                'total_profit': sum(self.performance_metrics['monthly_profit'][-12:]) if len(self.performance_metrics['monthly_profit']) >= 12 else sum(self.performance_metrics['monthly_profit']),
                'avg_market_share': np.mean(self.performance_metrics['market_share'][-12:]) if len(self.performance_metrics['market_share']) >= 12 else np.mean(self.performance_metrics['market_share']) if self.performance_metrics['market_share'] else 0,
                'avg_customer_satisfaction': np.mean(self.performance_metrics['customer_satisfaction'][-12:]) if len(self.performance_metrics['customer_satisfaction']) >= 12 else np.mean(self.performance_metrics['customer_satisfaction']) if self.performance_metrics['customer_satisfaction'] else 0
            },
            'growth_metrics': {
                'revenue_growth_rate': self._calculate_annual_growth_rate('monthly_revenue'),
                'profit_growth_rate': self._calculate_annual_growth_rate('monthly_profit'),
                'production_growth': self._calculate_production_growth()
            },
            'risk_assessment': self._assess_annual_risks(),
            'strategic_recommendations': self._generate_strategic_recommendations()
        }
        
        # Save annual report
        filename = f"reports/annual/Year_{year + self.simulation_data['current_date'].year - 1}_report.json"
        with open(filename, 'w') as f:
            json.dump(annual_data, f, indent=2, default=str)
        
        return annual_data
    
    def _calculate_growth_rate(self, data_series, periods):
        """Calculate growth rate over specified periods"""
        if len(data_series) < periods + 1:
            return 0
        
        current_avg = np.mean(data_series[-periods:])
        previous_avg = np.mean(data_series[-2*periods:-periods])
        
        if previous_avg == 0:
            return 0
        
        return (current_avg - previous_avg) / previous_avg
    
    def _calculate_change(self, data_series, periods):
        """Calculate absolute change over specified periods"""
        if len(data_series) < periods + 1:
            return 0
        
        current_avg = np.mean(data_series[-periods:])
        previous_avg = np.mean(data_series[-2*periods:-periods])
        
        return current_avg - previous_avg
    
    def _calculate_annual_growth_rate(self, metric):
        """Calculate year-over-year growth rate"""
        data = self.performance_metrics[metric]
        if len(data) < 24:  # Need at least 2 years of data
            return 0
        
        current_year_avg = np.mean(data[-12:])
        previous_year_avg = np.mean(data[-24:-12])
        
        if previous_year_avg == 0:
            return 0
        
        return (current_year_avg - previous_year_avg) / previous_year_avg
    
    def _calculate_production_growth(self):
        """Calculate production growth metrics"""
        production_data = self.performance_metrics['monthly_production']
        if len(production_data) < 12:
            return {'vehicles': 0, 'batteries': 0}
        
        current_vehicles = np.mean([p['vehicles'] for p in production_data[-12:]])
        current_batteries = np.mean([p['batteries_gwh'] for p in production_data[-12:]])
        
        if len(production_data) >= 24:
            previous_vehicles = np.mean([p['vehicles'] for p in production_data[-24:-12]])
            previous_batteries = np.mean([p['batteries_gwh'] for p in production_data[-24:-12]])
            
            vehicle_growth = (current_vehicles - previous_vehicles) / previous_vehicles if previous_vehicles > 0 else 0
            battery_growth = (current_batteries - previous_batteries) / previous_batteries if previous_batteries > 0 else 0
        else:
            vehicle_growth = 0
            battery_growth = 0
        
        return {
            'vehicles': vehicle_growth,
            'batteries': battery_growth
        }
    
    def _assess_annual_risks(self):
        """Assess key business risks"""
        risks = []
        
        # Supply chain risk
        if self.performance_metrics['supply_chain_efficiency']:
            avg_efficiency = np.mean(self.performance_metrics['supply_chain_efficiency'][-12:])
            if avg_efficiency < 0.8:
                risks.append({
                    'type': 'Supply Chain',
                    'severity': 'High' if avg_efficiency < 0.7 else 'Medium',
                    'description': f'Average supply chain efficiency: {avg_efficiency*100:.1f}%'
                })
        
        # Market share risk
        if self.performance_metrics['market_share']:
            current_share = self.performance_metrics['market_share'][-1]
            if current_share < 0.15:
                risks.append({
                    'type': 'Market Position',
                    'severity': 'High' if current_share < 0.1 else 'Medium',
                    'description': f'Market share below target: {current_share*100:.1f}%'
                })
        
        # Profitability risk
        if len(self.performance_metrics['monthly_profit']) >= 6:
            recent_profits = self.performance_metrics['monthly_profit'][-6:]
            if any(p < 0 for p in recent_profits):
                risks.append({
                    'type': 'Profitability',
                    'severity': 'High',
                    'description': 'Negative profits detected in recent months'
                })
        
        return risks
    
    def _generate_strategic_recommendations(self):
        """Generate strategic recommendations based on performance"""
        recommendations = []
        
        # Market share recommendations
        if self.performance_metrics['market_share']:
            current_share = self.performance_metrics['market_share'][-1]
            if current_share < 0.2:
                recommendations.append({
                    'area': 'Market Expansion',
                    'priority': 'High',
                    'action': 'Increase marketing investment and expand product portfolio',
                    'expected_impact': 'Improve market share by 3-5%'
                })
        
        # Innovation recommendations
        if self.performance_metrics['innovation_index']:
            avg_innovation = np.mean(self.performance_metrics['innovation_index'][-6:])
            if avg_innovation < 0.7:
                recommendations.append({
                    'area': 'Technology Innovation',
                    'priority': 'High',
                    'action': 'Increase R&D investment and accelerate technology development',
                    'expected_impact': 'Improve competitive position and product differentiation'
                })
        
        # Supply chain recommendations
        if self.performance_metrics['supply_chain_efficiency']:
            avg_efficiency = np.mean(self.performance_metrics['supply_chain_efficiency'][-6:])
            if avg_efficiency < 0.85:
                recommendations.append({
                    'area': 'Supply Chain Optimization',
                    'priority': 'Medium',
                    'action': 'Diversify suppliers and improve inventory management',
                    'expected_impact': 'Reduce supply chain risks and improve efficiency'
                })
        
        return recommendations
    
    def _extract_key_insights(self):
        """Extract key business insights from simulation"""
        insights = []
        
        # Revenue trend insight
        if len(self.performance_metrics['monthly_revenue']) > 6:
            recent_trend = np.polyfit(range(6), self.performance_metrics['monthly_revenue'][-6:], 1)[0]
            if recent_trend > 0:
                insights.append(f"Revenue showing positive trend: +${recent_trend:.1f}M per month")
            else:
                insights.append(f"Revenue showing declining trend: {recent_trend:.1f}M per month")
        
        # Market share insight
        if self.performance_metrics['market_share']:
            max_share = max(self.performance_metrics['market_share'])
            current_share = self.performance_metrics['market_share'][-1]
            if current_share >= max_share * 0.95:
                insights.append(f"Market share at peak performance: {current_share*100:.1f}%")
            else:
                insights.append(f"Market share below peak by {(max_share - current_share)*100:.1f} percentage points")
        
        # Customer satisfaction insight
        if self.performance_metrics['customer_satisfaction']:
            avg_satisfaction = np.mean(self.performance_metrics['customer_satisfaction'])
            if avg_satisfaction > 0.85:
                insights.append(f"Strong customer satisfaction maintained: {avg_satisfaction*100:.1f}%")
            else:
                insights.append(f"Customer satisfaction needs improvement: {avg_satisfaction*100:.1f}%")
        
        return insights
    
    def _summarize_alerts(self):
        """Summarize generated alerts"""
        alert_summary = {
            'total_alerts': len(self.simulation_data['alerts']),
            'by_severity': {},
            'by_type': {},
            'recent_critical': []
        }
        
        for alert in self.simulation_data['alerts']:
            # Count by severity
            severity = alert['severity']
            alert_summary['by_severity'][severity] = alert_summary['by_severity'].get(severity, 0) + 1
            
            # Count by type
            alert_type = alert['type']
            alert_summary['by_type'][alert_type] = alert_summary['by_type'].get(alert_type, 0) + 1
            
            # Collect recent critical alerts
            if severity == 'HIGH':
                alert_summary['recent_critical'].append({
                    'type': alert_type,
                    'message': alert['message'],
                    'date': alert['date']
                })
        
        return alert_summary
    
    def generate_report(self):
        """Generate comprehensive simulation report"""
        print("\n" + "="*50)
        print("📊 BYD SIMULATION REPORT")
        print("="*50)
        
        # Financial Summary
        financial_summary = self.finance.get_financial_summary()
        print(f"\n💰 FINANCIAL PERFORMANCE:")
        print(f"Total Revenue: ${financial_summary.get('total_revenue', 0):,.2f}M")
        print(f"Net Profit: ${financial_summary.get('net_profit', 0):,.2f}M")
        print(f"Profit Margin: {financial_summary.get('profit_margin', 0)*100:.1f}%")
        
        # Performance Trends
        if self.performance_metrics['monthly_revenue']:
            print(f"\n📈 PERFORMANCE TRENDS:")
            print(f"Average Monthly Revenue: ${np.mean(self.performance_metrics['monthly_revenue']):,.1f}M")
            print(f"Peak Monthly Revenue: ${max(self.performance_metrics['monthly_revenue']):,.1f}M")
            
            if len(self.performance_metrics['monthly_revenue']) > 1:
                revenue_growth = self._calculate_growth_rate(self.performance_metrics['monthly_revenue'], 3)
                print(f"Recent Revenue Growth: {revenue_growth*100:.1f}%")
        
        # Automotive Performance
        auto_metrics = self.automotive.get_financial_metrics()
        print(f"\n🚗 AUTOMOTIVE DIVISION:")
        print(f"Total Vehicle Sales: {auto_metrics.get('total_units_sold', 0):,} units")
        print(f"Revenue: ${auto_metrics.get('total_revenue', 0):,.2f}M")
        
        # Battery Performance
        battery_metrics = self.battery.get_financial_metrics()
        print(f"\n🔋 BATTERY DIVISION:")
        print(f"Total Battery Production: {battery_metrics.get('total_production_gwh', 0):.1f} GWh")
        print(f"Revenue: ${battery_metrics.get('total_revenue', 0):,.2f}M")
        
        # Market Metrics
        market_metrics = self.automotive.get_market_metrics()
        print(f"\n📈 MARKET PERFORMANCE:")
        print(f"Market Share: {market_metrics.get('market_share', 0)*100:.1f}%")
        print(f"Customer Satisfaction: {market_metrics.get('customer_satisfaction', 0)*100:.1f}%")
        
        # Key Insights
        insights = self._extract_key_insights()
        if insights:
            print(f"\n🔍 KEY INSIGHTS:")
            for i, insight in enumerate(insights, 1):
                print(f"{i}. {insight}")
        
        # Alert Summary
        alert_summary = self._summarize_alerts()
        print(f"\n🚨 ALERTS SUMMARY:")
        print(f"Total Alerts Generated: {alert_summary['total_alerts']}")
        if alert_summary['recent_critical']:
            print(f"Critical Alerts: {len(alert_summary['recent_critical'])}")
        
        print("\n" + "="*50)
        
        return {
            'financial_summary': financial_summary,
            'automotive_metrics': auto_metrics,
            'battery_metrics': battery_metrics,
            'market_metrics': market_metrics,
            'performance_trends': {
                'revenue_trend': self.performance_metrics['monthly_revenue'][-6:] if len(self.performance_metrics['monthly_revenue']) >= 6 else self.performance_metrics['monthly_revenue'],
                'profit_trend': self.performance_metrics['monthly_profit'][-6:] if len(self.performance_metrics['monthly_profit']) >= 6 else self.performance_metrics['monthly_profit']
            },
            'key_insights': insights,
            'alert_summary': alert_summary
        }

    def _count_generated_files(self):
        """Count the number of data files generated"""
        file_count = 0
        try:
            for root, dirs, files in os.walk('data'):
                file_count += len([f for f in files if f.endswith('.json')])
            for root, dirs, files in os.walk('reports'):
                file_count += len([f for f in files if f.endswith('.json')])
        except:
            pass
        return file_count
    
    def _save_simulation_summary(self, scenario, final_report):
        """Save overall simulation summary"""
        summary = {
            'simulation_metadata': {
                'scenario': scenario,
                'start_date': self.simulation_data['current_date'].isoformat(),
                'end_date': self.simulation_data['end_date'].isoformat(),
                'total_months': len(self.performance_metrics['monthly_revenue']),
                'completion_date': datetime.now().isoformat()
            },
            'final_performance': final_report,
            'key_insights': self._extract_key_insights(),
            'data_files_generated': self._count_generated_files(),
            'alerts_summary': self._summarize_alerts()
        }
        
        filename = f"simulation_summary_{scenario}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(summary, f, indent=2, default=str)
        
        print(f"📄 Simulation summary saved: {filename}")
        return summary

if __name__ == '__main__':
    print("🚀 BYD Business Simulation Suite")
    print("=" * 50)
    
    # Create and run baseline simulation
    print("\n🎯 Running Baseline Scenario...")
    sim_baseline = Simulation()
    baseline_results = sim_baseline.run('baseline')
    
    # Run optimistic scenario
    print("\n" + "="*60)
    print("🌟 Running Optimistic Scenario...")
    sim_optimistic = Simulation()
    optimistic_results = sim_optimistic.run('optimistic')
    
    # Run pessimistic scenario
    print("\n" + "="*60)
    print("⚠️ Running Pessimistic Scenario...")
    sim_pessimistic = Simulation()
    pessimistic_results = sim_pessimistic.run('pessimistic')
    
    # Compare scenarios
    print("\n" + "="*60)
    print("📊 SCENARIO COMPARISON")
    print("="*60)
    
    scenarios = {
        'Baseline': baseline_results,
        'Optimistic': optimistic_results,
        'Pessimistic': pessimistic_results
    }
    
    for scenario_name, results in scenarios.items():
        print(f"\n{scenario_name} Scenario:")
        print(f"  Months Simulated: {results['months_simulated']}")
        print(f"  Alerts Generated: {results['alerts_generated']}")
        if 'performance_summary' in results:
            perf = results['performance_summary']
            print(f"  Final Revenue: ${perf.get('final_revenue', 0):,.1f}M")
            print(f"  Final Profit: ${perf.get('final_profit', 0):,.1f}M")
            print(f"  Final Market Share: {perf.get('final_market_share', 0)*100:.1f}%")
    
    print("\n✅ All simulations completed successfully!")
    print("📁 Check the 'data' and 'reports' folders for detailed outputs")
    print("📊 Run 'streamlit run dashboard.py' to view interactive dashboard")
