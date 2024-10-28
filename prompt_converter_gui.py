"""
Original source code credit:
The prompt_to_stack function is based on the code from:
https://github.com/bedovyy/ComfyUI_NAIDGenerator/blob/master/utils.py#L146
Author: bedovyy
Modified for Novel AI to ComfyUI conversion purposes.
"""

import tkinter as tk
from tkinter import ttk
import re
from n2c_converter import novel_to_comfy
from c2n_converter import comfy_to_novel

class PromptConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Novel AI ↔ ComfyUI Converter")
        
        # 전체 프레임
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 버튼 프레임
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky=tk.W)
        
        # 변환 버튼들
        ttk.Button(btn_frame, text="Novel → Comfy", command=self.novel_to_comfy).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Comfy → Novel", command=self.comfy_to_novel).grid(row=0, column=1, padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear_input).grid(row=0, column=2, padx=5)
        
        # 입력 텍스트 영역
        input_frame = ttk.LabelFrame(main_frame, text="Input", padding="5")
        input_frame.grid(row=1, column=0, padx=(0, 5), sticky=(tk.W, tk.E, tk.N, tk.S))
        self.input_text = tk.Text(input_frame, width=40, height=15, wrap=tk.WORD)
        self.input_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 입력 텍스트 스크롤바
        input_scroll = ttk.Scrollbar(input_frame, orient=tk.VERTICAL, command=self.input_text.yview)
        input_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.input_text['yscrollcommand'] = input_scroll.set
        
        # 결과 텍스트 영역
        result_frame = ttk.LabelFrame(main_frame, text="Result", padding="5")
        result_frame.grid(row=1, column=1, padx=(5, 0), sticky=(tk.W, tk.E, tk.N, tk.S))
        self.result_text = tk.Text(result_frame, width=40, height=15, wrap=tk.WORD, state='disabled')
        self.result_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 결과 텍스트 스크롤바
        result_scroll = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, command=self.result_text.yview)
        result_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.result_text['yscrollcommand'] = result_scroll.set
        
        # 복사 버튼
        ttk.Button(main_frame, text="Copy Result", command=self.copy_result).grid(row=2, column=0, columnspan=2, pady=(10, 0))
        
        # 그리드 설정
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        input_frame.columnconfigure(0, weight=1)
        input_frame.rowconfigure(0, weight=1)
        result_frame.columnconfigure(0, weight=1)
        result_frame.rowconfigure(0, weight=1)

    def set_result_text(self, text):
        self.result_text.configure(state='normal')
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(1.0, text)
        self.result_text.configure(state='disabled')

    def novel_to_comfy(self):
        input_text = self.input_text.get(1.0, tk.END).strip()
        if input_text:
            result = novel_to_comfy(input_text)
            self.set_result_text(result)

    def comfy_to_novel(self):
        input_text = self.input_text.get(1.0, tk.END).strip()
        if input_text:
            result = comfy_to_novel(input_text)
            self.set_result_text(result)

    def clear_input(self):
        self.input_text.delete(1.0, tk.END)
        self.set_result_text("")

    def copy_result(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.result_text.get(1.0, tk.END).strip())
        self.root.update()

def main():
    root = tk.Tk()
    app = PromptConverterGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()