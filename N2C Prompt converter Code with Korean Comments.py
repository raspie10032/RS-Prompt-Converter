import tkinter as tk
from tkinter import ttk, messagebox
import re

# 가중치 변환 상수
NOVEL_AI_BRACKET = 0.95
NOVEL_AI_BRACE = 1.05

def convert_novelai_to_comfyui(prompt):
    try:
        # 1. 일반 텍스트의 가중치를 변환합니다.
        def replace_weights(match):
            text = match.group(1)
            weight = 1.0

            # 가중치 적용
            for char in match.group(0):
                if char == '[':
                    weight *= NOVEL_AI_BRACKET
                elif char == '{':
                    weight *= NOVEL_AI_BRACE

            weight = round(weight, 1)
            return f'({text}:{weight:.1f})'

        # 중첩된 대괄호와 중괄호 변환
        prompt = re.sub(r'[\[\{]+([^\]\}]+)[\]\}]+', replace_weights, prompt)

        return prompt
    except Exception as e:
        messagebox.showerror("Conversion Error", f"An error occurred during conversion to ComfyUI: {str(e)}")
        return prompt

class WeightConverterApp:
    def __init__(self, root):
        self.root = root
        root.title("Weight Converter")

        self.novelai_label = ttk.Label(root, text="Novel AI Prompt:")
        self.novelai_label.grid(row=0, column=0, padx=10, pady=10)
        self.novelai_text = tk.Text(root, height=10, width=50)
        self.novelai_text.grid(row=1, column=0, padx=10, pady=10)

        self.comfyui_label = ttk.Label(root, text="ComfyUI Prompt:")
        self.comfyui_label.grid(row=0, column=1, padx=10, pady=10)
        self.comfyui_text = tk.Text(root, height=10, width=50)
        self.comfyui_text.grid(row=1, column=1, padx=10, pady=10)

        self.to_comfyui_button = ttk.Button(root, text="Convert to ComfyUI", command=self.convert_to_comfyui)
        self.to_comfyui_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def convert_to_comfyui(self):
        novelai_prompt = self.novelai_text.get("1.0", tk.END).strip()
        if novelai_prompt:
            comfyui_prompt = convert_novelai_to_comfyui(novelai_prompt)
            self.comfyui_text.delete("1.0", tk.END)
            self.comfyui_text.insert(tk.END, comfyui_prompt)
        else:
            messagebox.showwarning("Input Error", "Please enter a Novel AI prompt.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeightConverterApp(root)
    root.mainloop()
