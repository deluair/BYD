# BYD Global Mobility Simulation

A comprehensive simulation of BYD's global electric mobility business, modeling automotive production, battery manufacturing, financial performance, and market dynamics.

## Project Structure

```
BYD_Simulation/
├── config/                    # Configuration files
│   └── simulation_config.json # Main simulation configuration
├── data/                     # Generated simulation data (auto-created)
├── modules/                  # Simulation modules
│   ├── automotive/           # Vehicle production and sales
│   ├── battery/              # Battery production and supply chain
│   ├── electronics/          # Electronics manufacturing
│   ├── energy_storage/       # Energy storage systems
│   ├── finance/              # Financial modeling
│   ├── geopolitical/         # Trade and policy impacts
│   ├── supply_chain/         # Supply chain management
│   └── technology/           # R&D and innovation
├── reports/                  # Generated reports (auto-created)
├── scripts/                  # Utility scripts
├── tests/                    # Test scripts
├── main.py                   # Main simulation entry point
└── requirements.txt          # Python dependencies
```

## Prerequisites

- Python 3.8+
- Git (optional, for cloning and contributing)

## Getting Started

1. Clone this repository
2. Navigate to the project directory
3. (Optional) Create a virtual environment and activate it
4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the simulation:

```bash
python main.py
```

## Key Features

- **Automotive Business**: Models BYD's vehicle production and sales across global markets
- **Battery Production**: Simulates battery manufacturing and supply chain dynamics
- **Financial Modeling**: Tracks revenue, costs, and profitability metrics
- **Geopolitical Factors**: Accounts for tariffs, trade policies, and regional regulations
- **Scenario Analysis**: Baseline implementation with hooks for optimistic / pessimistic scenarios

## Configuration

Edit `config/simulation_config.json` to adjust simulation parameters:
- Simulation period
- Geographic regions
- Vehicle models
- Battery technologies
- Scenarios

## Data & Reports

The simulation generates:
- Monthly production reports in `data/`
- Financial reports in `reports/`
- Console output with key metrics

## License

This project is for educational and research purposes only.

## Disclaimer

This is a simulation and does not represent actual BYD business operations or financials.
