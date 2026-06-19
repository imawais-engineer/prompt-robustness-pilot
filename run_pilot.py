import openai
import pandas as pd
import time

openai.api_key = "YOUR_API_KEY_HERE"

prompts = {
    "clear": "Explain the difference between SQL and NoSQL databases. Be concise.",
    "typos": "Exxplain differance betwen SQL and NoSQL data bases. Be consise.",
    "mixed": "SQL aur NoSQL databases mein kya farq hai? Explain the difference in simple English."
}

results = []
for variant, prompt in prompts.items():
    for run in range(1, 4):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=200
            )
            results.append({"variant": variant, "run": run, "prompt": prompt, "response": response.choices[0].message.content})
            print(f"Done: {variant} run {run}")
            time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")

pd.DataFrame(results).to_csv("raw_responses.csv", index=False)
print("Saved raw_responses.csv")
