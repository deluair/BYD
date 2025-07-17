import json
import math
import random
import numpy as np
from datetime import datetime, timedelta

class FinanceModule:
    def __init__(self, simulation_data, automotive_module, battery_module, electronics_module, energy_storage_module, technology_module=None, geopolitical_module=None, supply_chain_module=None):
        self.simulation_data = simulation_data
        self.config = simulation_data['config']
        self.automotive_module = automotive_module
        self.battery_module = battery_module
        self.electronics_module = electronics_module
        self.energy_storage_module = energy_storage_module
        self.technology_module = technology_module
        self.geopolitical_module = geopolitical_module
        self.supply_chain_module = supply_chain_module
        
        self.finance_data = {
            'revenue_streams': {
                'automotive': {
                    'vehicle_sales': 0,
                    'after_sales_service': 0,
                    'financing_income': 0,
                    'leasing_income': 0,
                    'total': 0
                },
                'battery': {
                    'oem_sales': 0,
                    'replacement_market': 0,
                    'energy_storage_systems': 0,
                    'recycling_revenue': 0,
                    'total': 0
                },
                'electronics': {
                    'semiconductor_sales': 0,
                    'igbt_modules': 0,
                    'power_management': 0,
                    'sensors_iot': 0,
                    'total': 0
                },
                'energy_storage': {
                    'utility_scale': 0,
                    'commercial_industrial': 0,
                    'residential': 0,
                    'grid_services': 0,
                    'total': 0
                },
                'other_business': {
                    'rail_transit': 15200,  # Million CNY
                    'electronics_manufacturing': 8500,
                    'real_estate': 3200,
                    'total': 26900
                }
            },
            'cost_structure': {
                'cost_of_goods_sold': {
                    'raw_materials': 0,
                    'direct_labor': 0,
                    'manufacturing_overhead': 0,
                    'logistics_distribution': 0,
                    'total': 0
                },
                'operating_expenses': {
                    'research_development': 0,
                    'sales_marketing': 0,
                    'general_administrative': 0,
                    'warranty_provisions': 0,
                    'total': 0
                },
                'financial_costs': {
                    'interest_expense': 0,
                    'foreign_exchange_loss': 0,
                    'other_financial_costs': 0,
                    'total': 0
                }
            },
            'profitability_metrics': {
                'gross_profit': 0,
                'gross_margin': 0,
                'operating_profit': 0,
                'operating_margin': 0,
                'net_profit': 0,
                'net_margin': 0,
                'ebitda': 0,
                'ebitda_margin': 0
            },
            'cash_flow': {
                'operating_cash_flow': {
                    'net_income': 0,
                    'depreciation_amortization': 0,
                    'working_capital_change': 0,
                    'other_operating_items': 0,
                    'total': 0
                },
                'investing_cash_flow': {
                    'capex': 0,
                    'rd_investments': 0,
                    'acquisitions': 0,
                    'asset_disposals': 0,
                    'total': 0
                },
                'financing_cash_flow': {
                    'debt_issuance': 0,
                    'debt_repayment': 0,
                    'equity_issuance': 0,
                    'dividends_paid': 0,
                    'total': 0
                },
                'net_cash_flow': 0,
                'cash_balance': 154900  # Million CNY
            },
            'balance_sheet': {
                'assets': {
                    'current_assets': {
                        'cash_equivalents': 154900,
                        'accounts_receivable': 45200,
                        'inventory': 38500,
                        'other_current': 12800,
                        'total': 251400
                    },
                    'non_current_assets': {
                        'property_plant_equipment': 285600,
                        'intangible_assets': 45200,
                        'investments': 28500,
                        'other_non_current': 15800,
                        'total': 375100
                    },
                    'total_assets': 626500
                },
                'liabilities': {
                    'current_liabilities': {
                        'accounts_payable': 52800,
                        'short_term_debt': 28500,
                        'accrued_expenses': 18200,
                        'other_current': 9500,
                        'total': 109000
                    },
                    'non_current_liabilities': {
                        'long_term_debt': 125600,
                        'deferred_tax': 15800,
                        'other_non_current': 8200,
                        'total': 149600
                    },
                    'total_liabilities': 258600
                },
                'equity': {
                    'share_capital': 29100,
                    'retained_earnings': 285400,
                    'other_equity': 53400,
                    'total_equity': 367900
                }
            },
            'financial_ratios': {
                'liquidity_ratios': {
                    'current_ratio': 0,
                    'quick_ratio': 0,
                    'cash_ratio': 0
                },
                'efficiency_ratios': {
                    'asset_turnover': 0,
                    'inventory_turnover': 0,
                    'receivables_turnover': 0,
                    'working_capital_turnover': 0
                },
                'profitability_ratios': {
                    'return_on_assets': 0,
                    'return_on_equity': 0,
                    'return_on_invested_capital': 0
                },
                'leverage_ratios': {
                    'debt_to_equity': 0,
                    'debt_to_assets': 0,
                    'interest_coverage': 0
                }
            },
            'market_data': {
                'exchange_rates': {
                    'CNY_USD': 0.1385,
                    'CNY_EUR': 0.1275,
                    'CNY_JPY': 20.85,
                    'CNY_GBP': 0.1095
                },
                'commodity_prices': {
                    'lithium_carbonate_cny_per_ton': 485000,
                    'nickel_cny_per_ton': 128500,
                    'cobalt_cny_per_ton': 385000,
                    'steel_cny_per_ton': 4200,
                    'aluminum_cny_per_ton': 18500
                },
                'interest_rates': {
                    'china_base_rate': 0.0385,
                    'us_fed_rate': 0.0525,
                    'ecb_rate': 0.045,
                    'corporate_bond_yield': 0.048
                }
            },
            'forecasting': {
                'revenue_forecast': {
                    'next_quarter': 0,
                    'next_year': 0,
                    'growth_rate_projection': 0
                },
                'cost_forecast': {
                    'next_quarter': 0,
                    'next_year': 0,
                    'efficiency_improvement': 0
                },
                'investment_pipeline': {
                    'planned_capex': 45200,
                    'rd_budget': 28500,
                    'expansion_projects': 15800
                }
            },
            'risk_metrics': {
                'financial_risks': {
                    'currency_exposure': 0.25,
                    'commodity_price_risk': 0.35,
                    'interest_rate_risk': 0.15,
                    'credit_risk': 0.08
                },
                'operational_risks': {
                    'supply_chain_disruption': 0.20,
                    'regulatory_changes': 0.18,
                    'technology_obsolescence': 0.12,
                    'competitive_pressure': 0.22
                }
            }
        }
        self.initialize()

    def initialize(self):
        """Initialize financial tracking and performance metrics"""
        print("Finance module initialized with comprehensive financial management.")
        self._initialize_financial_tracking()
        self._setup_risk_monitoring()
        self._calculate_initial_ratios()

    def _initialize_financial_tracking(self):
        """Initialize financial performance tracking"""
        self.financial_history = {
            'monthly_revenue': [],
            'monthly_profit': [],
            'cash_flow_history': [],
            'ratio_trends': []
        }

    def _setup_risk_monitoring(self):
        """Setup financial risk monitoring systems"""
        self.risk_alerts = {
            'liquidity_warnings': [],
            'profitability_alerts': [],
            'market_risks': []
        }

    def _calculate_initial_ratios(self):
        """Calculate initial financial ratios"""
        self._update_financial_ratios()

    def update_financials(self):
        """Comprehensive monthly financial update"""
        self._update_revenue_streams()
        self._update_cost_structure()
        self._calculate_profitability_metrics()
        self._update_cash_flow()
        self._update_balance_sheet()
        self._update_financial_ratios()
        self._update_market_data()
        self._generate_forecasts()
        self._assess_financial_risks()
        
        self.log_data()

    def _update_revenue_streams(self):
        """Update all revenue streams from business modules"""
        # Automotive revenue
        automotive_metrics = self.automotive_module.get_performance_metrics()
        self.finance_data['revenue_streams']['automotive']['vehicle_sales'] = automotive_metrics['financial']['total_revenue']
        self.finance_data['revenue_streams']['automotive']['after_sales_service'] = automotive_metrics['financial']['total_revenue'] * 0.15
        self.finance_data['revenue_streams']['automotive']['financing_income'] = automotive_metrics['financial']['total_revenue'] * 0.08
        self.finance_data['revenue_streams']['automotive']['leasing_income'] = automotive_metrics['financial']['total_revenue'] * 0.05
        self.finance_data['revenue_streams']['automotive']['total'] = sum([
            self.finance_data['revenue_streams']['automotive'][key] 
            for key in ['vehicle_sales', 'after_sales_service', 'financing_income', 'leasing_income']
        ])

        # Battery revenue
        battery_metrics = self.battery_module.get_performance_metrics()
        total_battery_revenue = battery_metrics['financial']['total_revenue']
        self.finance_data['revenue_streams']['battery']['oem_sales'] = total_battery_revenue * 0.70
        self.finance_data['revenue_streams']['battery']['replacement_market'] = total_battery_revenue * 0.15
        self.finance_data['revenue_streams']['battery']['energy_storage_systems'] = total_battery_revenue * 0.12
        self.finance_data['revenue_streams']['battery']['recycling_revenue'] = total_battery_revenue * 0.03
        self.finance_data['revenue_streams']['battery']['total'] = total_battery_revenue

        # Electronics revenue
        electronics_metrics = self.electronics_module.get_performance_metrics()
        total_electronics_revenue = electronics_metrics['financial']['total_revenue']
        self.finance_data['revenue_streams']['electronics']['semiconductor_sales'] = total_electronics_revenue * 0.35
        self.finance_data['revenue_streams']['electronics']['igbt_modules'] = total_electronics_revenue * 0.28
        self.finance_data['revenue_streams']['electronics']['power_management'] = total_electronics_revenue * 0.22
        self.finance_data['revenue_streams']['electronics']['sensors_iot'] = total_electronics_revenue * 0.15
        self.finance_data['revenue_streams']['electronics']['total'] = total_electronics_revenue

        # Energy storage revenue
        energy_storage_metrics = self.energy_storage_module.get_performance_metrics()
        total_energy_storage_revenue = energy_storage_metrics['financial']['total_revenue']
        self.finance_data['revenue_streams']['energy_storage']['utility_scale'] = total_energy_storage_revenue * 0.45
        self.finance_data['revenue_streams']['energy_storage']['commercial_industrial'] = total_energy_storage_revenue * 0.35
        self.finance_data['revenue_streams']['energy_storage']['residential'] = total_energy_storage_revenue * 0.15
        self.finance_data['revenue_streams']['energy_storage']['grid_services'] = total_energy_storage_revenue * 0.05
        self.finance_data['revenue_streams']['energy_storage']['total'] = total_energy_storage_revenue

        # Other business revenue fluctuations
        other_change = random.uniform(-0.05, 0.12)
        for segment in self.finance_data['revenue_streams']['other_business']:
            if segment != 'total':
                self.finance_data['revenue_streams']['other_business'][segment] *= (1 + other_change)
        
        self.finance_data['revenue_streams']['other_business']['total'] = sum([
            self.finance_data['revenue_streams']['other_business'][key] 
            for key in ['rail_transit', 'electronics_manufacturing', 'real_estate']
        ])

    def _update_cost_structure(self):
        """Update comprehensive cost structure"""
        total_revenue = sum([stream['total'] for stream in self.finance_data['revenue_streams'].values()])
        
        # Cost of Goods Sold
        cogs = self.finance_data['cost_structure']['cost_of_goods_sold']
        
        # Raw materials cost (integrate with supply chain if available)
        if self.supply_chain_module:
            supply_metrics = self.supply_chain_module.get_performance_metrics()
            raw_materials_cost_base = supply_metrics['inventory_management']['raw_materials_value_million_cny']
            cogs['raw_materials'] = raw_materials_cost_base * random.uniform(1.8, 2.5)  # Monthly consumption
        else:
            cogs['raw_materials'] = total_revenue * random.uniform(0.25, 0.35)
        
        # Direct labor
        cogs['direct_labor'] = total_revenue * random.uniform(0.12, 0.18)
        
        # Manufacturing overhead
        cogs['manufacturing_overhead'] = total_revenue * random.uniform(0.08, 0.15)
        
        # Logistics and distribution
        if self.supply_chain_module:
            supply_metrics = self.supply_chain_module.get_performance_metrics()
            logistics_efficiency = supply_metrics['logistics_efficiency']['warehouse_utilization']
            logistics_cost_factor = (2.0 - logistics_efficiency) * 0.05  # Better efficiency = lower costs
            cogs['logistics_distribution'] = total_revenue * logistics_cost_factor
        else:
            cogs['logistics_distribution'] = total_revenue * random.uniform(0.04, 0.08)
        
        cogs['total'] = sum(cogs[key] for key in ['raw_materials', 'direct_labor', 'manufacturing_overhead', 'logistics_distribution'])
        
        # Operating Expenses
        opex = self.finance_data['cost_structure']['operating_expenses']
        
        # R&D expenses (integrate with technology module if available)
        if self.technology_module:
            tech_metrics = self.technology_module.get_performance_metrics()
            rd_investment = tech_metrics['innovation_metrics']['rd_investment_million_cny']
            opex['research_development'] = rd_investment
        else:
            opex['research_development'] = total_revenue * random.uniform(0.06, 0.10)
        
        # Sales and marketing
        opex['sales_marketing'] = total_revenue * random.uniform(0.08, 0.12)
        
        # General and administrative
        opex['general_administrative'] = total_revenue * random.uniform(0.05, 0.08)
        
        # Warranty provisions
        opex['warranty_provisions'] = self.finance_data['revenue_streams']['automotive']['total'] * random.uniform(0.02, 0.04)
        
        opex['total'] = sum(opex.values())
        
        # Financial Costs
        fin_costs = self.finance_data['cost_structure']['financial_costs']
        
        # Interest expense
        total_debt = (self.finance_data['balance_sheet']['liabilities']['current_liabilities']['short_term_debt'] + 
                     self.finance_data['balance_sheet']['liabilities']['non_current_liabilities']['long_term_debt'])
        avg_interest_rate = self.finance_data['market_data']['interest_rates']['corporate_bond_yield']
        fin_costs['interest_expense'] = total_debt * avg_interest_rate / 12  # Monthly interest
        
        # Foreign exchange impact (integrate with geopolitical module if available)
        if self.geopolitical_module:
            geo_metrics = self.geopolitical_module.get_performance_metrics()
            fx_volatility = 1.0 - geo_metrics['market_access']['weighted_average_score']
            fx_impact = total_revenue * 0.15 * fx_volatility * random.uniform(-0.05, 0.05)
            fin_costs['foreign_exchange_loss'] = max(0, fx_impact)
        else:
            fin_costs['foreign_exchange_loss'] = total_revenue * random.uniform(0.001, 0.008)
        
        # Other financial costs
        fin_costs['other_financial_costs'] = total_revenue * random.uniform(0.002, 0.005)
        
        fin_costs['total'] = sum(fin_costs.values())

    def _calculate_profitability_metrics(self):
        """Calculate comprehensive profitability metrics"""
        total_revenue = sum([stream['total'] for stream in self.finance_data['revenue_streams'].values()])
        cogs_total = self.finance_data['cost_structure']['cost_of_goods_sold']['total']
        opex_total = self.finance_data['cost_structure']['operating_expenses']['total']
        fin_costs_total = self.finance_data['cost_structure']['financial_costs']['total']
        
        metrics = self.finance_data['profitability_metrics']
        
        # Gross profit and margin
        metrics['gross_profit'] = total_revenue - cogs_total
        metrics['gross_margin'] = metrics['gross_profit'] / total_revenue if total_revenue > 0 else 0
        
        # Operating profit and margin
        metrics['operating_profit'] = metrics['gross_profit'] - opex_total
        metrics['operating_margin'] = metrics['operating_profit'] / total_revenue if total_revenue > 0 else 0
        
        # Net profit and margin
        metrics['net_profit'] = metrics['operating_profit'] - fin_costs_total
        metrics['net_margin'] = metrics['net_profit'] / total_revenue if total_revenue > 0 else 0
        
        # EBITDA (assuming depreciation is 3% of PPE annually)
        annual_depreciation = self.finance_data['balance_sheet']['assets']['non_current_assets']['property_plant_equipment'] * 0.03
        monthly_depreciation = annual_depreciation / 12
        metrics['ebitda'] = metrics['operating_profit'] + monthly_depreciation
        metrics['ebitda_margin'] = metrics['ebitda'] / total_revenue if total_revenue > 0 else 0

    def _update_cash_flow(self):
        """Update comprehensive cash flow statement"""
        cash_flow = self.finance_data['cash_flow']
        
        # Operating Cash Flow
        ocf = cash_flow['operating_cash_flow']
        ocf['net_income'] = self.finance_data['profitability_metrics']['net_profit']
        
        # Depreciation and amortization
        annual_depreciation = self.finance_data['balance_sheet']['assets']['non_current_assets']['property_plant_equipment'] * 0.03
        ocf['depreciation_amortization'] = annual_depreciation / 12
        
        # Working capital change (simplified)
        working_capital_change = random.uniform(-5000, 8000)  # Million CNY
        ocf['working_capital_change'] = working_capital_change
        
        # Other operating items
        ocf['other_operating_items'] = random.uniform(-2000, 3000)
        
        ocf['total'] = sum(ocf.values())
        
        # Investing Cash Flow
        icf = cash_flow['investing_cash_flow']
        
        # Capital expenditures
        if self.technology_module:
            tech_metrics = self.technology_module.get_performance_metrics()
            monthly_capex = self.finance_data['forecasting']['investment_pipeline']['planned_capex'] / 12
            icf['capex'] = -monthly_capex  # Negative because it's an outflow
        else:
            icf['capex'] = -random.uniform(3000, 8000)
        
        # R&D investments
        icf['rd_investments'] = -self.finance_data['cost_structure']['operating_expenses']['research_development'] * 0.3
        
        # Acquisitions and disposals
        icf['acquisitions'] = random.uniform(-5000, 0) if random.random() < 0.1 else 0
        icf['asset_disposals'] = random.uniform(0, 2000) if random.random() < 0.05 else 0
        
        icf['total'] = sum(icf.values())
        
        # Financing Cash Flow
        fcf = cash_flow['financing_cash_flow']
        
        # Debt activities
        fcf['debt_issuance'] = random.uniform(0, 10000) if random.random() < 0.08 else 0
        fcf['debt_repayment'] = -random.uniform(0, 5000) if random.random() < 0.12 else 0
        
        # Equity activities
        fcf['equity_issuance'] = random.uniform(0, 15000) if random.random() < 0.03 else 0
        fcf['dividends_paid'] = -self.finance_data['profitability_metrics']['net_profit'] * 0.25 if self.finance_data['profitability_metrics']['net_profit'] > 0 else 0
        
        fcf['total'] = sum(fcf.values())
        
        # Net cash flow and cash balance update
        cash_flow['net_cash_flow'] = ocf['total'] + icf['total'] + fcf['total']
        cash_flow['cash_balance'] += cash_flow['net_cash_flow']
        
        # Update balance sheet cash
        self.finance_data['balance_sheet']['assets']['current_assets']['cash_equivalents'] = cash_flow['cash_balance']

    def _update_balance_sheet(self):
        """Update balance sheet items"""
        # Update current assets totals
        current_assets = self.finance_data['balance_sheet']['assets']['current_assets']
        current_assets['total'] = sum([current_assets[key] for key in ['cash_equivalents', 'accounts_receivable', 'inventory', 'other_current']])
        
        # Update non-current assets (add monthly capex to PPE)
        non_current_assets = self.finance_data['balance_sheet']['assets']['non_current_assets']
        monthly_capex = abs(self.finance_data['cash_flow']['investing_cash_flow']['capex'])
        monthly_depreciation = self.finance_data['cash_flow']['operating_cash_flow']['depreciation_amortization']
        non_current_assets['property_plant_equipment'] += monthly_capex - monthly_depreciation
        
        non_current_assets['total'] = sum([non_current_assets[key] for key in ['property_plant_equipment', 'intangible_assets', 'investments', 'other_non_current']])
        
        # Update total assets
        self.finance_data['balance_sheet']['assets']['total_assets'] = current_assets['total'] + non_current_assets['total']
        
        # Update liabilities (simplified)
        current_liabilities = self.finance_data['balance_sheet']['liabilities']['current_liabilities']
        current_liabilities['total'] = sum([current_liabilities[key] for key in ['accounts_payable', 'short_term_debt', 'accrued_expenses', 'other_current']])
        
        non_current_liabilities = self.finance_data['balance_sheet']['liabilities']['non_current_liabilities']
        non_current_liabilities['total'] = sum([non_current_liabilities[key] for key in ['long_term_debt', 'deferred_tax', 'other_non_current']])
        
        self.finance_data['balance_sheet']['liabilities']['total_liabilities'] = current_liabilities['total'] + non_current_liabilities['total']
        
        # Update equity (add retained earnings)
        equity = self.finance_data['balance_sheet']['equity']
        equity['retained_earnings'] += self.finance_data['profitability_metrics']['net_profit']
        equity['total_equity'] = sum([equity[key] for key in ['share_capital', 'retained_earnings', 'other_equity']])

    def _update_financial_ratios(self):
        """Calculate comprehensive financial ratios"""
        ratios = self.finance_data['financial_ratios']
        balance_sheet = self.finance_data['balance_sheet']
        
        # Liquidity ratios
        current_assets = balance_sheet['assets']['current_assets']['total']
        current_liabilities = balance_sheet['liabilities']['current_liabilities']['total']
        cash = balance_sheet['assets']['current_assets']['cash_equivalents']
        
        ratios['liquidity_ratios']['current_ratio'] = current_assets / current_liabilities if current_liabilities > 0 else 0
        ratios['liquidity_ratios']['quick_ratio'] = (current_assets - balance_sheet['assets']['current_assets']['inventory']) / current_liabilities if current_liabilities > 0 else 0
        ratios['liquidity_ratios']['cash_ratio'] = cash / current_liabilities if current_liabilities > 0 else 0
        
        # Efficiency ratios
        total_revenue = sum([stream['total'] for stream in self.finance_data['revenue_streams'].values()])
        total_assets = balance_sheet['assets']['total_assets']
        inventory = balance_sheet['assets']['current_assets']['inventory']
        receivables = balance_sheet['assets']['current_assets']['accounts_receivable']
        
        ratios['efficiency_ratios']['asset_turnover'] = (total_revenue * 12) / total_assets if total_assets > 0 else 0  # Annualized
        ratios['efficiency_ratios']['inventory_turnover'] = (self.finance_data['cost_structure']['cost_of_goods_sold']['total'] * 12) / inventory if inventory > 0 else 0
        ratios['efficiency_ratios']['receivables_turnover'] = (total_revenue * 12) / receivables if receivables > 0 else 0
        
        # Profitability ratios
        net_profit = self.finance_data['profitability_metrics']['net_profit']
        total_equity = balance_sheet['equity']['total_equity']
        
        ratios['profitability_ratios']['return_on_assets'] = (net_profit * 12) / total_assets if total_assets > 0 else 0  # Annualized
        ratios['profitability_ratios']['return_on_equity'] = (net_profit * 12) / total_equity if total_equity > 0 else 0
        
        # Leverage ratios
        total_debt = balance_sheet['liabilities']['current_liabilities']['short_term_debt'] + balance_sheet['liabilities']['non_current_liabilities']['long_term_debt']
        total_liabilities = balance_sheet['liabilities']['total_liabilities']
        
        ratios['leverage_ratios']['debt_to_equity'] = total_debt / total_equity if total_equity > 0 else 0
        ratios['leverage_ratios']['debt_to_assets'] = total_liabilities / total_assets if total_assets > 0 else 0
        
        operating_profit = self.finance_data['profitability_metrics']['operating_profit']
        interest_expense = self.finance_data['cost_structure']['financial_costs']['interest_expense']
        ratios['leverage_ratios']['interest_coverage'] = operating_profit / interest_expense if interest_expense > 0 else 0

    def _update_market_data(self):
        """Update market data including exchange rates and commodity prices"""
        market_data = self.finance_data['market_data']
        
        # Exchange rate fluctuations
        for currency, rate in market_data['exchange_rates'].items():
            rate_change = random.uniform(-0.05, 0.05)
            market_data['exchange_rates'][currency] *= (1 + rate_change)
        
        # Commodity price fluctuations
        for commodity, price in market_data['commodity_prices'].items():
            if 'lithium' in commodity:
                price_change = random.uniform(-0.15, 0.20)  # Higher volatility for lithium
            else:
                price_change = random.uniform(-0.08, 0.12)
            market_data['commodity_prices'][commodity] *= (1 + price_change)
        
        # Interest rate adjustments
        for rate_type, rate in market_data['interest_rates'].items():
            rate_change = random.uniform(-0.002, 0.003)
            market_data['interest_rates'][rate_type] = max(0.01, market_data['interest_rates'][rate_type] + rate_change)

    def _generate_forecasts(self):
        """Generate financial forecasts"""
        forecasting = self.finance_data['forecasting']
        
        # Revenue forecast
        current_revenue = sum([stream['total'] for stream in self.finance_data['revenue_streams'].values()])
        growth_rate = random.uniform(0.08, 0.25)  # 8-25% growth
        
        forecasting['revenue_forecast']['next_quarter'] = current_revenue * 3 * (1 + growth_rate / 4)
        forecasting['revenue_forecast']['next_year'] = current_revenue * 12 * (1 + growth_rate)
        forecasting['revenue_forecast']['growth_rate_projection'] = growth_rate
        
        # Cost forecast
        current_costs = (self.finance_data['cost_structure']['cost_of_goods_sold']['total'] + 
                        self.finance_data['cost_structure']['operating_expenses']['total'])
        efficiency_improvement = random.uniform(0.02, 0.08)
        
        forecasting['cost_forecast']['next_quarter'] = current_costs * 3 * (1 - efficiency_improvement / 4)
        forecasting['cost_forecast']['next_year'] = current_costs * 12 * (1 - efficiency_improvement)
        forecasting['cost_forecast']['efficiency_improvement'] = efficiency_improvement

    def _assess_financial_risks(self):
        """Assess comprehensive financial risks"""
        # Update risk metrics based on current financial position
        ratios = self.finance_data['financial_ratios']
        
        # Liquidity risk assessment
        if ratios['liquidity_ratios']['current_ratio'] < 1.2:
            self.risk_alerts['liquidity_warnings'].append({
                'date': self.simulation_data['current_date'].isoformat(),
                'type': 'Low Current Ratio',
                'value': ratios['liquidity_ratios']['current_ratio']
            })
        
        # Profitability risk assessment
        if self.finance_data['profitability_metrics']['net_margin'] < 0.05:
            self.risk_alerts['profitability_alerts'].append({
                'date': self.simulation_data['current_date'].isoformat(),
                'type': 'Low Net Margin',
                'value': self.finance_data['profitability_metrics']['net_margin']
            })

    def get_performance_metrics(self):
        """Get comprehensive financial performance metrics"""
        total_revenue = sum([stream['total'] for stream in self.finance_data['revenue_streams'].values()])
        
        return {
            'revenue_performance': {
                'total_revenue_million_cny': total_revenue,
                'automotive_revenue_share': self.finance_data['revenue_streams']['automotive']['total'] / total_revenue if total_revenue > 0 else 0,
                'battery_revenue_share': self.finance_data['revenue_streams']['battery']['total'] / total_revenue if total_revenue > 0 else 0,
                'revenue_growth_rate': self.finance_data['forecasting']['revenue_forecast']['growth_rate_projection']
            },
            'profitability_performance': {
                'gross_margin': self.finance_data['profitability_metrics']['gross_margin'],
                'operating_margin': self.finance_data['profitability_metrics']['operating_margin'],
                'net_margin': self.finance_data['profitability_metrics']['net_margin'],
                'ebitda_margin': self.finance_data['profitability_metrics']['ebitda_margin']
            },
            'financial_health': {
                'current_ratio': self.finance_data['financial_ratios']['liquidity_ratios']['current_ratio'],
                'debt_to_equity': self.finance_data['financial_ratios']['leverage_ratios']['debt_to_equity'],
                'return_on_equity': self.finance_data['financial_ratios']['profitability_ratios']['return_on_equity'],
                'cash_balance_million_cny': self.finance_data['cash_flow']['cash_balance']
            },
            'operational_efficiency': {
                'asset_turnover': self.finance_data['financial_ratios']['efficiency_ratios']['asset_turnover'],
                'inventory_turnover': self.finance_data['financial_ratios']['efficiency_ratios']['inventory_turnover'],
                'cost_efficiency_improvement': self.finance_data['forecasting']['cost_forecast']['efficiency_improvement']
            }
        }

    def get_financial_summary(self):
        """Get financial summary for main simulation tracking"""
        total_revenue = sum([stream['total'] for stream in self.finance_data['revenue_streams'].values()])
        
        return {
            'total_revenue': total_revenue,
            'net_profit': self.finance_data['profitability_metrics']['net_profit'],
            'gross_profit': self.finance_data['profitability_metrics']['gross_profit'],
            'operating_profit': self.finance_data['profitability_metrics']['operating_profit'],
            'cash_balance': self.finance_data['balance_sheet']['assets']['current_assets']['cash_equivalents'],
            'total_assets': self.finance_data['balance_sheet']['assets']['total_assets'],
            'market_cap_estimate': total_revenue * 2.5  # Simple market cap estimation
        }

    def get_vehicle_price(self, model, region):
        """Calculate vehicle pricing with enhanced regional and market factors"""
        base_prices = {
            'Seagull': 80000, 'Dolphin': 120000, 'Seal': 180000, 'Han': 250000,
            'Tang': 300000, 'Yuan': 150000, 'Song': 200000
        }
        regional_multipliers = {
            'China': 1.0, 'Europe': 1.4, 'NorthAmerica': 1.5, 'SoutheastAsia': 1.1,
            'LatinAmerica': 1.2, 'MiddleEast': 1.3
        }
        
        base_price = base_prices.get(model, 0)
        multiplier = regional_multipliers.get(region, 1.0)
        
        # Apply geopolitical factors if available
        if self.geopolitical_module and region != 'China':
            geo_metrics = self.geopolitical_module.get_performance_metrics()
            market_access = geo_metrics['market_access']['weighted_average_score']
            multiplier *= (0.8 + 0.4 * market_access)  # Adjust pricing based on market access
        
        price = base_price * multiplier
        
        # Apply exchange rate
        if region != 'China':
            price *= self.finance_data['market_data']['exchange_rates']['CNY_USD']
        
        return round(price / 1000) * 1000

    def log_data(self):
        """Enhanced logging with comprehensive financial data"""
        log_entry = {
            'timestamp': self.simulation_data['current_date'].isoformat(),
            'type': 'Financials',
            'data': self.finance_data,
            'performance_metrics': self.get_performance_metrics(),
            'financial_history': self.financial_history,
            'risk_alerts': self.risk_alerts
        }
        
        # Add to financial history
        total_revenue = sum([stream['total'] for stream in self.finance_data['revenue_streams'].values()])
        self.financial_history['monthly_revenue'].append({
            'date': self.simulation_data['current_date'].isoformat(),
            'revenue': total_revenue
        })
        
        self.financial_history['monthly_profit'].append({
            'date': self.simulation_data['current_date'].isoformat(),
            'profit': self.finance_data['profitability_metrics']['net_profit']
        })
        
        log_path = f"data/financials_{self.simulation_data['current_date'].strftime('%Y%m')}.json"
        with open(log_path, 'w') as f:
            json.dump(log_entry, f, indent=4, default=str)
