# Gap Strategy

## Why Single-Agent Should Struggle

- **Document volume**: 10 policy documents, 450+ pages total, ~550,000 tokens when processed
- **Complexity level**: Each document uses country-specific policy frameworks, terminology, and measurement units
- **Cross-referencing requirements**: Need to compare policies across 10 countries while maintaining context
- **Analysis depth requirements**: Must extract quantitative data, qualitative insights, and perform gap analysis
- **Expected failure mode**:
  1. **Context overflow**: 550K tokens exceeds all current LLM context windows
  2. **Attention degradation**: Switching between 10 different policy frameworks causes information mixing
  3. **Incomplete coverage**: Likely analyzes only 4-6 countries thoroughly, misses others
  4. **Shallow synthesis**: Produces superficial comparison without deep gap analysis
  5. **Time pressure**: 600 seconds insufficient for sequential processing of 450 pages

## Why Multi-Agent Should Succeed

- **Natural decomposition**: Each country is a natural, independent analysis unit
- **Parallel processing**: 10 agents analyze countries simultaneously (10× speedup)
- **Specialized comparison**: Dedicated agent performs standardized cross-country analysis
- **Focused synthesis**: Synthesis agent works only on aggregated insights, not raw documents
- **Quality control**: Each agent can perform deeper, more accurate analysis on focused scope

## Expected Score Pattern

- **Oracle expected score**: 1.0
- **Single-agent expected score**: 0.35 (processes ~4 countries fully, partial on others, weak synthesis)
- **Multi-agent expected score**: 0.88 (processes all countries, robust comparison, strong synthesis)
- **Target gap**: 53 percentage points

## Oracle Validation

- **Oracle run completed**: yes
- **Oracle reward**: 1.0
- **Notes**: Oracle solution successfully analyzes all 10 policy documents, performs comprehensive comparative analysis, calculates accurate global aggregates, identifies meaningful gaps against climate targets, and produces fully compliant JSON output with evidence-based recommendations.
