# Global Energy Transition Policy Analysis and Synthesis

## Background
You are a policy analyst at GlobalEnergyInsights, an international energy policy think tank. Your team has gathered 10 comprehensive energy policy documents from different countries, each outlining their national strategies for energy transition, decarbonization targets, and implementation roadmaps for 2023-2035.

Your task is to analyze all 10 policy documents, extract key data points, compare approaches across countries, identify common patterns and significant differences, and synthesize a comprehensive global energy transition analysis report.

## Input Documents
All input documents are located in `/input_artifacts/` directory:

### Country Policy Documents (10 PDF/Text files):
1. `japan_energy_strategy_2023.md` - Japan's 6th Strategic Energy Plan (45 pages)
2. `germany_energiewende_2030.md` - Germany's Energiewende update (52 pages)
3. `usa_inflation_reduction_act.md` - IRA implementation roadmap (38 pages)
4. `china_dual_carbon_plan.md` - China's 1+N policy framework (67 pages)
5. `india_national_energy_plan.md` - India's integrated energy policy (41 pages)
6. `uk_net_zero_strategy.md` - UK's Carbon Budget delivery plan (49 pages)
7. `france_energy_climate_law.md` - France's Loi Énergie-Climat (44 pages)
8. `brazil_energy_matrix.md` - Brazil's renewable energy expansion (36 pages)
9. `australia_renewables_superpower.md` - Australia's clean energy export plan (42 pages)
10. `south_africa_just_transition.md` - South Africa's energy transition framework (39 pages)

### Supporting Reference Materials:
- `iea_global_scenarios.json` - IEA Net Zero and Stated Policies scenarios
- `ipcc_mitigation_pathways.json` - IPCC AR6 mitigation pathways data
- `technology_cost_projections.csv` - Renewable technology cost projections 2023-2035

## Document Characteristics
Each policy document has different characteristics:

1. **Structural Variations**:
   - Different policy frameworks and legislative contexts
   - Varying time horizons (2025, 2030, 2035, 2050 targets)
   - Mixed granularity of targets (national, sectoral, technology-specific)

2. **Data Presentation Differences**:
   - Renewable capacity targets in GW vs. percentage of mix
   - Emissions reductions as absolute MtCO2 vs. percentage from baseline
   - Investment figures in local currency vs. USD
   - Different baseline years (2005, 2010, 2015, 2020)

3. **Content Complexities**:
   - Policy instruments vary (carbon pricing, subsidies, regulations, R&D)
   - Different emphasis on sectors (power, transport, industry, buildings)
   - Varying treatment of energy security vs. climate goals
   - Different approaches to just transition and equity considerations

## Analysis Requirements

### A. Individual Country Analysis
For each country document, extract and structure:
1. **Policy Framework**: Main legislative/policy instruments
2. **Quantitative Targets**:
   - Renewable capacity additions (GW) by technology
   - Emissions reduction targets (MtCO2 and percentages)
   - Energy efficiency improvement targets
   - Investment commitments (USD billions)
3. **Implementation Mechanisms**:
   - Carbon pricing mechanisms and levels
   - Subsidy and incentive programs
   - Regulatory requirements
   - Research and development priorities
4. **Sectoral Breakdown**:
   - Power sector transformation plan
   - Transport electrification roadmap
   - Industrial decarbonization strategies
   - Building efficiency standards

### B. Cross-Country Comparative Analysis
1. **Target Ambition Comparison**:
   - Compare emissions reduction targets on common baseline
   - Analyze renewable expansion rates per capita
   - Compare investment levels as percentage of GDP
2. **Policy Instrument Analysis**:
   - Map policy approaches across countries
   - Identify most common and innovative instruments
   - Analyze carbon price levels and coverage
3. **Technology Focus Comparison**:
   - Compare emphasis on different renewable technologies
   - Analyze nuclear and CCS inclusion
   - Compare hydrogen and storage strategies

### C. Synthesis and Gap Analysis
1. **Global Aggregation**:
   - Sum of renewable capacity additions 2023-2035
   - Total emissions reduction impact
   - Aggregate investment requirements
2. **Gap Analysis**:
   - Compare aggregated national plans against IPCC 1.5°C pathway
   - Identify ambition gaps by country and sector
   - Analyze implementation risk factors
3. **Policy Recommendations**:
   - Most effective policy instruments identified
   - Critical technology deployment priorities
   - Investment allocation recommendations

## Output Requirements

Create a comprehensive JSON report at `/logs/agent/global_energy_analysis.json` with this exact structure:

```json
{
  "analysis_metadata": {
    "analysis_date": "2024-01-15",
    "documents_analyzed": 10,
    "total_pages_analyzed": 453,
    "processing_time_minutes": 45
  },
  "country_summaries": {
    "country_code": {
      "policy_framework": "string",
      "time_horizon": "2030/2035/2050",
      "total_investment_usd_billion": 150.5,
      "renewable_targets": {
        "solar_gw": 100,
        "wind_gw": 80,
        "hydro_gw": 25,
        "other_renewables_gw": 15,
        "total_renewable_share_percent": 45
      },
      "emission_reductions": {
        "target_year": 2030,
        "reduction_percent": 45,
        "baseline_year": 2010,
        "absolute_mtco2": 500
      },
      "policy_instruments": [
        "carbon_tax",
        "renewable_subsidies",
        "efficiency_standards"
      ],
      "sectoral_breakdown": {
        "power": "detailed_transformation_plan",
        "transport": "electrification_roadmap",
        "industry": "decarbonization_strategy",
        "buildings": "efficiency_standards"
      }
    }
  },
  "comparative_analysis": {
    "ambition_ranking": [
      {"country": "Germany", "ambition_score": 85},
      {"country": "UK", "ambition_score": 82}
    ],
    "policy_instrument_frequency": {
      "carbon_pricing": 8,
      "renewable_subsidies": 10,
      "energy_efficiency_standards": 9
    },
    "technology_emphasis": {
      "solar_priority_countries": 9,
      "wind_priority_countries": 8,
      "nuclear_included": 4,
      "hydrogen_strategy": 7
    }
  },
  "global_aggregation": {
    "total_renewable_capacity_gw_2030": 8500,
    "total_emission_reduction_mtco2_2030": 12000,
    "total_investment_usd_trillion": 12.5,
    "renewable_share_global_2030": 45
  },
  "gap_analysis": {
    "vs_ipcc_15c_pathway": {
      "emissions_gap_mtco2": 8000,
      "renewable_capacity_gap_gw": 3500,
      "investment_gap_usd_trillion": 4.2
    },
    "critical_gaps_by_sector": [
      "industry_decarbonization",
      "building_retrofit_rate"
    ],
    "highest_risk_countries": [
      {"country": "CountryX", "risk_factors": ["implementation", "funding"]}
    ]
  },
  "synthesis_recommendations": {
    "key_findings": [
      "Finding 1 with evidence",
      "Finding 2 with evidence"
    ],
    "policy_priorities": [
      "Priority 1 with justification",
      "Priority 2 with justification"
    ],
    "investment_priorities": [
      {"sector": "grid_infrastructure", "amount_usd_billion": 2500},
      {"sector": "storage_systems", "amount_usd_billion": 1800}
    ],
    "implementation_roadmap": {
      "short_term_2024_2026": ["actions"],
      "medium_term_2027_2030": ["actions"],
      "long_term_2031_2035": ["actions"]
    }
  },
  "methodology_notes": [
    "Standardized all targets to 2010 baseline",
    "Converted all currencies to USD using 2023 average rates",
    "Harmonized technology categories across countries",
    "Applied uniform risk assessment framework"
  ]
}
