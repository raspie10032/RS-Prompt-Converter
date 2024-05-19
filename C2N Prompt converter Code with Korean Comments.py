import tkinter as tk
from tkinter import ttk, messagebox
import re

# 가중치 변환 상수
NOVEL_AI_BRACKET = 0.95
NOVEL_AI_BRACE = 1.05

def convert_comfyui_to_novelai(prompt):
    try:
        # 1. "artist:"를 "artist_"로 변환
        prompt = prompt.replace("artist:", "artist_")

        # 2. 일반 텍스트의 가중치를 변환합니다.
        def replace_match(match):
            text = match.group(1)
            weight = float(match.group(2))
            if weight == 1.0:
                return text
            elif weight < 1.0:
                brackets = int(round((1 - weight) / (1 - NOVEL_AI_BRACKET)))
                return '[' * brackets + text + ']' * brackets
            else:
                braces = int(round((weight - 1) / (NOVEL_AI_BRACE - 1)))
                return '{' * braces + text + '}' * braces

        pattern = re.compile(r'\(([^:]+):([\d.]+)\)')
        prompt = pattern.sub(replace_match, prompt)

        # 3. 연속된 콤마 처리
        prompt = re.sub(r',\s*,', ', ', prompt)

        # 4. 불완전한 소괄호 제거
        prompt = re.sub(r'(?<!\()\(|\)(?!\))', '', prompt)

        # 5. 백슬래시 제거
        prompt = prompt.replace('\\', '')

        # 6. "artist_"를 "artist:"로 변환
        prompt = prompt.replace("artist_", "artist:")

        # 7. "artist:aa_bb" 형식을 "artist:aa_(bb)" 형식으로 변환
        def artist_format(match):
            artist_name, artist_alias = match.groups()
            return f'artist:{artist_name}_({artist_alias})'

        prompt = re.sub(r'artist:([a-zA-Z0-9]+)_([a-zA-Z0-9]+)', artist_format, prompt)

        return prompt
    except Exception as e:
        messagebox.showerror("Conversion Error", f"An error occurred during conversion to Novel AI: {str(e)}")
        return prompt

class WeightConverterApp:
    def __init__(self, root):
        self.root = root
        root.title("Weight Converter")

        self.comfyui_label = ttk.Label(root, text="ComfyUI Prompt:")
        self.comfyui_label.grid(row=0, column=0, padx=10, pady=10)
        self.comfyui_text = tk.Text(root, height=10, width=50)
        self.comfyui_text.grid(row=1, column=0, padx=10, pady=10)

        self.novelai_label = ttk.Label(root, text="Novel AI Prompt:")
        self.novelai_label.grid(row=0, column=1, padx=10, pady=10)
        self.novelai_text = tk.Text(root, height=10, width=50)
        self.novelai_text.grid(row=1, column=1, padx=10, pady=10)

        self.to_novelai_button = ttk.Button(root, text="Convert to Novel AI", command=self.convert_to_novelai)
        self.to_novelai_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def convert_to_novelai(self):
        comfyui_prompt = self.comfyui_text.get("1.0", tk.END).strip()
        if comfyui_prompt:
            novelai_prompt = convert_comfyui_to_novelai(comfyui_prompt)
            self.novelai_text.delete("1.0", tk.END)
            self.novelai_text.insert(tk.END, novelai_prompt)
        else:
            messagebox.showwarning("Input Error", "Please enter a ComfyUI prompt.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeightConverterApp(root)
    root.mainloop()
