import g4f
import re

def extract_excel_formula(text):
    match = re.search(r'(=.+)', text)
    return match.group(1).strip() if match else text.strip()

def generate_excel_formula(user_input, explanation=False):
    prompt = (
        f"You are a spreadsheet assistant. {user_input} "
        "Write a valid Excel formula only. Do not explain unless asked."
    )

    response = g4f.ChatCompletion.create(
        model=g4f.models.deepseek_r1_distill_qwen_32b,  # Or a more concise one like phi_3_5_mini
        messages=[{"role": "user", "content": prompt}]
    )

    return response if explanation else extract_excel_formula(response)
