import re
from typing import Any, Dict, Tuple

# Weight conversion constants
NOVEL_AI_BRACKET = 0.95
NOVEL_AI_BRACE = 1.05

# Function to convert Novel AI to ComfyUI
def convert_novelai_to_comfyui(prompt: str) -> str:
    try:
        # Function to find brackets and braces and calculate the weight
        def replace_weights(match):
            text = match.group(1)
            weight = 1.0

            # Apply weights
            for char in match.group(0):
                if char == '[':
                    weight *= NOVEL_AI_BRACKET
                elif char == '{':
                    weight *= NOVEL_AI_BRACE

            # Round to one decimal place
            weight = round(weight, 1)
            return f'({text}:{weight:.1f})'

        # Find patterns with brackets and braces and convert weights
        prompt = re.sub(r'[\[\{]+([^\]\}]+)[\]\}]+', replace_weights, prompt)
        return prompt
    except Exception as e:
        raise RuntimeError(f"An error occurred during conversion to ComfyUI: {str(e)}")

# Function to convert ComfyUI to Novel AI
def convert_comfyui_to_novelai(prompt: str) -> str:
    try:
        # Convert "artist:" to "artist_"
        prompt = prompt.replace("artist:", "artist_")

        # Function to convert the weight of general text
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

        # Find patterns with text and weight and convert
        pattern = re.compile(r'\(([^:]+):([\d.]+)\)')
        prompt = pattern.sub(replace_match, prompt)

        # Handle consecutive commas
        prompt = re.sub(r',\s*,', ', ', prompt)

        # Remove incomplete parentheses
        prompt = re.sub(r'(?<!\()\(|\)(?!\))', '', prompt)

        # Remove backslashes
        prompt = prompt.replace('\\', '')

        # Convert "artist_" back to "artist:"
        prompt = prompt.replace("artist_", "artist:")

        # Convert "artist:aa_bb" to "artist:aa_(bb)"
        def artist_format(match):
            artist_name, artist_alias = match.groups()
            return f'artist:{artist_name}_({artist_alias})'

        prompt = re.sub(r'artist:([a-zA-Z0-9]+)_([a-zA-Z0-9]+)', artist_format, prompt)

        return prompt
    except Exception as e:
        raise RuntimeError(f"An error occurred during conversion to Novel AI: {str(e)}")

# Define the custom node class for ComfyUI
class PromptConverterNode:
    @staticmethod
    def INPUT_TYPES() -> Dict[str, Any]:
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True}),
                "conversion_type": ("BOOLEAN", {"default": False, "display_name": "Conversion Type (C2N=True, N2C=False)"})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Converted Prompt",)
    FUNCTION = "convert_prompt"
    CATEGORY = "Custom"
    DESCRIPTION = (
        "Converts prompts between Novel AI and ComfyUI formats.\n\n"
        "Conversion Type:\n"
        "True: ComfyUI Prompt to NAI Prompt\n"
        "False: NAI Prompt to ComfyUI Prompt"
    )

    @staticmethod
    def convert_prompt(prompt: str, conversion_type: bool) -> Tuple[str]:
        if conversion_type:
            return (convert_comfyui_to_novelai(prompt),)
        else:
            return (convert_novelai_to_comfyui(prompt),)

# Register the custom node with ComfyUI
NODE_CLASS_MAPPINGS = {
    "PromptConverterNode": PromptConverterNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptConverterNode": "Prompt Converter"
}
