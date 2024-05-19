import tkinter as tk
from tkinter import ttk, messagebox
import re

# 가중치 변환 상수
NOVEL_AI_BRACKET = 0.95
NOVEL_AI_BRACE = 1.05

# Novel AI -> ComfyUI 변환 함수
def convert_novelai_to_comfyui(prompt):
    try:
        # 대괄호와 중괄호를 찾아서 가중치를 계산하는 함수
        def replace_weights(match):
            text = match.group(1)
            weight = 1.0

            # 가중치 적용
            for char in match.group(0):
                if char == '[':
                    weight *= NOVEL_AI_BRACKET
                elif char == '{':
                    weight *= NOVEL_AI_BRACE

            # 소수점 첫 번째 자리까지만 반올림
            weight = round(weight, 1)
            return f'({text}:{weight:.1f})'

        # 대괄호와 중괄호를 포함한 패턴을 찾아서 가중치를 변환
        prompt = re.sub(r'[\[\{]+([^\]\}]+)[\]\}]+', replace_weights, prompt)
        return prompt
    except Exception as e:
        messagebox.showerror("Conversion Error", f"An error occurred during conversion to ComfyUI: {str(e)}")
        return prompt

# ComfyUI -> Novel AI 변환 함수
def convert_comfyui_to_novelai(prompt):
    try:
        # "artist:"를 "artist_"로 변환
        prompt = prompt.replace("artist:", "artist_")

        # 일반 텍스트의 가중치를 변환하는 함수
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

        # 텍스트와 가중치의 패턴을 찾아서 변환
        pattern = re.compile(r'\(([^:]+):([\d.]+)\)')
        prompt = pattern.sub(replace_match, prompt)

        # 연속된 콤마 처리
        prompt = re.sub(r',\s*,', ', ', prompt)

        # 불완전한 소괄호 제거
        prompt = re.sub(r'(?<!\()\(|\)(?!\))', '', prompt)

        # 백슬래시 제거
        prompt = prompt.replace('\\', '')

        # "artist_"를 "artist:"로 변환
        prompt = prompt.replace("artist_", "artist:")

        # "artist:aa_bb" 형식을 "artist:aa_(bb)" 형식으로 변환
        def artist_format(match):
            artist_name, artist_alias = match.groups()
            return f'artist:{artist_name}_({artist_alias})'
        
        prompt = re.sub(r'artist:([a-zA-Z0-9]+)_([a-zA-Z0-9]+)', artist_format, prompt)

        return prompt
    except Exception as e:
        messagebox.showerror("Conversion Error", f"An error occurred during conversion to Novel AI: {str(e)}")
        return prompt

# GUI 클래스
class WeightConverterApp:
    def __init__(self, root):
        self.root = root
        root.title("Prompt Converter")

        # 변환 유형 선택 라디오 버튼
        self.conversion_type = tk.StringVar(value="N2C")
        self.type_frame = ttk.Frame(root)
        self.type_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.n2c_radio = ttk.Radiobutton(self.type_frame, text="Novel AI to ComfyUI", variable=self.conversion_type, value="N2C")
        self.n2c_radio.grid(row=0, column=0)
        self.c2n_radio = ttk.Radiobutton(self.type_frame, text="ComfyUI to Novel AI", variable=self.conversion_type, value="C2N")
        self.c2n_radio.grid(row=0, column=1)

        # 입력 프롬프트 텍스트 상자
        self.input_label = ttk.Label(root, text="Input Prompt:")
        self.input_label.grid(row=1, column=0, padx=10, pady=10)
        self.input_text = tk.Text(root, height=10, width=50)
        self.input_text.grid(row=2, column=0, padx=10, pady=10)

        # 출력 프롬프트 텍스트 상자
        self.output_label = ttk.Label(root, text="Output Prompt:")
        self.output_label.grid(row=1, column=1, padx=10, pady=10)
        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.grid(row=2, column=1, padx=10, pady=10)

        # 변환 버튼
        self.convert_button = ttk.Button(root, text="Convert", command=self.convert_prompt)
        self.convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # 변환 함수
    def convert_prompt(self):
        input_prompt = self.input_text.get("1.0", tk.END).strip()
        if input_prompt:
            conversion_type = self.conversion_type.get()
            if conversion_type == "N2C":
                output_prompt = convert_novelai_to_comfyui(input_prompt)
            else:
                output_prompt = convert_comfyui_to_novelai(input_prompt)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, output_prompt)
        else:
            messagebox.showwarning("Input Error", "Please enter a prompt.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeightConverterApp(root)
    root.mainloop()
