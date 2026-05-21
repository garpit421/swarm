#!/usr/bin/env python3
"""
Verification script for Global Energy Policy Analysis Task
Evaluates completeness, accuracy, and quality of analysis
"""

import json
import os
import sys
from pathlib import Path
import jsonschema
from jsonschema import validate

def verify_energy_policy_analysis():
    """Main verification function"""
    score = 0.0
    checks = []
    max_score = 1.0
    
    def add_check(name, passed, weight):
        nonlocal score
        checks.append((name, passed, weight))
        if passed:
            score += weight
    
    print("=" * 70)
    print("GLOBAL ENERGY POLICY ANALYSIS VERIFIER")
    print("=" * 70)
    
    # Check 1: Output file exists and is valid JSON (5%)
    output_path = Path("/logs/agent/global_energy_analysis.json")
    if output_path.exists():
        add_check("output_file_exists", True, 0.05)
        print("✓ Output file found")
        
        try:
            with open(output_path, 'r', encoding='utf-8') as f:
                report = json.load(f)
            add_check("valid_json_format", True, 0.05)
            print("✓ Valid JSON format")
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            report = None
            add_check("valid_json_format", False, 0.05)
            print(f"✗ Invalid JSON: {str(e)[:100]}")
    else:
        report = None
        add_check("output_file_exists", False, 0.05)
        print("✗ Output file not found")
    
    if report:
        # Define exact schema for validation
        energy_schema = {
            "type": "object",
            "required": [
                "analysis_metadata",
                "country_summaries",
                "comparative_analysis",
                "global_aggregation",
                "gap_analysis",
                "synthesis_recommendations",
                "methodology_notes"
            ],
            "properties": {
                "analysis_metadata": {"type": "object"},
                "country_summaries": {"type": "object"},
                "comparative_analysis": {"type": "object"},
                "global_aggregation": {"type": "object"},
                "gap_analysis": {"type": "object"},
                "synthesis_recommendations": {"type": "object"},
                "methodology_notes": {"type": "array"}
            }
        }
        
        # Check 2: Schema validation (12%)
        try:
            validate(instance=report, schema=energy_schema)
            add_check("schema_validation", True, 0.12)
            print("✓ Full schema validation passed")
        except jsonschema.ValidationError as e:
            add_check("schema_validation", False, 0.12)
            print(f"✗ Schema validation failed at: {e.path}")
        
        # Check 3: All 10 countries analyzed (15%)
        if "country_summaries" in report:
            country_summaries = report["country_summaries"]
            expected_countries = [
                "japan", "germany", "usa", "china", "india",
                "uk", "france", "brazil", "australia", "south_africa"
            ]
            
            # Check for country presence (case-insensitive)
            actual_countries = [c.lower() for c in country_summaries.keys()]
            countries_present = sum(1 for ec in expected_countries if any(ec in ac for ac in actual_countries))
            
            all_countries_analyzed = countries_present >= 8  # At least 8/10 countries
            add_check("min_countries_analyzed", all_countries_analyzed, 0.15)
            
            if all_countries_analyzed:
                print(f"✓ Country analysis complete: {countries_present}/10 countries")
            else:
                print(f"✗ Insufficient country coverage: {countries_present}/10 countries")
        else:
            add_check("min_countries_analyzed", False, 0.15)
            print("✗ Country summaries missing")
        
        # Check 4: Analysis metadata complete (8%)
        if "analysis_metadata" in report:
            metadata = report["analysis_metadata"]
            required_meta = ["analysis_date", "documents_analyzed", "total_pages_analyzed"]
            meta_complete = all(field in metadata for field in required_meta)
            add_check("metadata_complete", meta_complete, 0.08)
            
            if meta_complete:
                print("✓ Analysis metadata complete")
                # Check reasonable values
                if metadata.get("documents_analyzed", 0) >= 8:
                    add_check("reasonable_document_count", True, 0.02)
                else:
                    add_check("reasonable_document_count", False, 0.02)
            else:
                print(f"✗ Missing metadata: {set(required_meta) - set(metadata.keys())}")
        else:
            add_check("metadata_complete", False, 0.08)
            print("✗ Analysis metadata missing")
        
        # Check 5: Comparative analysis performed (12%)
        if "comparative_analysis" in report:
            comparative = report["comparative_analysis"]
            required_comparisons = ["ambition_ranking", "policy_instrument_frequency", "technology_emphasis"]
            comparisons_present = all(field in comparative for field in required_comparisons)
            
            # Check data quality
            has_data = False
            if "ambition_ranking" in comparative and isinstance(comparative["ambition_ranking"], list):
                has_data = len(comparative["ambition_ranking"]) >= 5
            
            comparative_valid = comparisons_present and has_data
            add_check("comparative_analysis_done", comparative_valid, 0.12)
            
            if comparative_valid:
                print("✓ Comparative analysis completed")
            else:
                print(f"✗ Comparative analysis incomplete")
        else:
            add_check("comparative_analysis_done", False, 0.12)
            print("✗ Comparative analysis missing")
        
        # Check 6: Global aggregation calculated (10%)
        if "global_aggregation" in report:
            aggregation = report["global_aggregation"]
            required_aggregates = [
                "total_renewable_capacity_gw_2030",
                "total_emission_reduction_mtco2_2030",
                "total_investment_usd_trillion"
            ]
            aggregates_present = all(field in aggregation for field in required_aggregates)
            
            # Check for reasonable values
            reasonable = True
            if aggregates_present:
                capacity = aggregation.get("total_renewable_capacity_gw_2030", 0)
                investment = aggregation.get("total_investment_usd_trillion", 0)
                reasonable = (1000 <= capacity <= 20000) and (1 <= investment <= 50)
            
            aggregation_valid = aggregates_present and reasonable
            add_check("global_aggregation_valid", aggregation_valid, 0.10)
            
            if aggregation_valid:
                print("✓ Global aggregation calculated")
            else:
                print("✗ Global aggregation invalid or unreasonable")
        else:
            add_check("global_aggregation_valid", False, 0.10)
            print("✗ Global aggregation missing")
        
        # Check 7: Gap analysis performed (10%)
        if "gap_analysis" in report:
            gap = report["gap_analysis"]
            has_gap_analysis = "vs_ipcc_15c_pathway" in gap and "critical_gaps_by_sector" in gap
            
            # Check for meaningful gap identification
            meaningful = False
            if has_gap_analysis and "vs_ipcc_15c_pathway" in gap:
                ipcc_pathway = gap["vs_ipcc_15c_pathway"]
                meaningful = any(isinstance(ipcc_pathway.get(k), (int, float)) for k in ["emissions_gap_mtco2", "renewable_capacity_gap_gw"])
            
            gap_valid = has_gap_analysis and meaningful
            add_check("gap_analysis_performed", gap_valid, 0.10)
            
            if gap_valid:
                print("✓ Gap analysis completed")
            else:
                print("✗ Gap analysis incomplete")
        else:
            add_check("gap_analysis_performed", False, 0.10)
            print("✗ Gap analysis missing")
        
        # Check 8: Synthesis recommendations (8%)
        if "synthesis_recommendations" in report:
            synthesis = report["synthesis_recommendations"]
            required_sections = ["key_findings", "policy_priorities", "investment_priorities"]
            synthesis_complete = all(section in synthesis for section in required_sections)
            
            # Check for non-empty recommendations
            meaningful = False
            if synthesis_complete:
                key_findings = synthesis.get("key_findings", [])
                policy_priorities = synthesis.get("policy_priorities", [])
                meaningful = len(key_findings) >= 3 and len(policy_priorities) >= 3
            
            synthesis_valid = synthesis_complete and meaningful
            add_check("synthesis_quality", synthesis_valid, 0.08)
            
            if synthesis_valid:
                print("✓ Synthesis recommendations complete")
            else:
                print("✗ Synthesis recommendations insufficient")
        else:
            add_check("synthesis_quality", False, 0.08)
            print("✗ Synthesis recommendations missing")
        
        # Check 9: Methodology notes (5%)
        if "methodology_notes" in report:
            notes = report["methodology_notes"]
            has_methodology = isinstance(notes, list) and len(notes) >= 3
            add_check("methodology_documented", has_methodology, 0.05)
            
            if has_methodology:
                print(f"✓ Methodology documented: {len(notes)} notes")
            else:
                print("✗ Insufficient methodology documentation")
        else:
            add_check("methodology_documented", False, 0.05)
            print("✗ Methodology notes missing")
        
        # Check 10: Intermediate files (5%)
        intermediate_dir = Path("/logs/agent/intermediate")
        if intermediate_dir.exists():
            country_files = list(intermediate_dir.glob("*_analysis.json"))
            has_intermediate = len(country_files) >= 5
            add_check("intermediate_files_present", has_intermediate, 0.05)
            
            if has_intermediate:
                print(f"✓ Intermediate analysis files: {len(country_files)} found")
            else:
                print(f"✗ Insufficient intermediate files: {len(country_files)}")
        else:
            add_check("intermediate_files_present", False, 0.05)
            print("✗ Intermediate directory missing")
    
    # Calculate final score
    final_score = round(min(score, max_score), 4)
    
    # Create output directory and write reward
    Path("/logs/verifier").mkdir(parents=True, exist_ok=True)
    with open("/logs/verifier/reward.txt", "w") as f:
        f.write(str(final_score))
    
    # Print comprehensive results
    print("\n" + "=" * 70)
    print("VERIFICATION RESULTS SUMMARY")
    print("=" * 70)
    
    for name, passed, weight in checks:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{name:40} {status:8} ({weight:.2f})")
    
    print("-" * 70)
    print(f"TOTAL SCORE: {final_score:.4f}/{max_score:.1f}")
    print(f"PERCENTAGE: {(final_score/max_score)*100:.1f}%")
    print("=" * 70)
    
    return 0 if final_score > 0.99 else 1

if __name__ == "__main__":
    try:
        sys.exit(verify_energy_policy_analysis())
    except Exception as e:
        print(f"Verification error: {e}")
        Path("/logs/verifier").mkdir(parents=True, exist_ok=True)
        with open("/logs/verifier/reward.txt", "w") as f:
            f.write("0.0")
        sys.exit(1)
