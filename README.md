# Prompt Robustness Pilot

**Purpose:** Test whether natural prompt variations (typos, mixed language) degrade GPT-3.5-turbo's response quality for educational tasks.

## Method
- **Topic:** SQL vs NoSQL databases
- **Task:** Explain the difference
- **Prompt variants:** clear, typos, mixed Urdu/English
- **Runs:** 3 per variant (9 total)
- **Model:** gpt-3.5-turbo (temperature 0.7)

## Results
| Variant | Avg Correctness | Avg Clarity |
|---------|----------------|-------------|
| clear   | 4.7            | 4.7         |
| typos   | 3.0            | 2.8         |
| mixed   | 3.3            | 3.2         |

## Conclusion
Both typos and mixed-language prompts reduced response quality, confirming robustness as a real issue requiring further study.
