import re
from typing import Any, Dict, Tuple, Match

# Constants
NOVEL_AI_BRACKET = 0.95
NOVEL_AI_BRACE = 1.05
ARTIST_PREFIX = "artist:"
ARTIST_TEMP = "artist_"

# Compile frequently used regex patterns
WEIGHT_PATTERN = re.compile(r'\(([^:]+):([\d.]+)\)')
ARTIST_PATTERN = re.compile(rf'{ARTIST_PREFIX}([a-zA-Z0-9]+)_([a-zA-Z0-9]+)')
BRACKET_BRACE_PATTERN = re.compile(r'[\[\{]+([^\]\}]+)[\]\}]+')

def convert_novelai_to_comfyui(prompt: str) -> str:
    """
    Convert Novel AI prompt format to ComfyUI format.
    
    Args:
        prompt (str): The input prompt in Novel AI format.
    
    Returns:
        str: The converted prompt in ComfyUI format.
    
    Raises:
        ValueError: If an error occurs during conversion.
    """
    try:
        def replace_weights(match: Match[str]) -> str:
            """Calculate and replace weights for matched brackets and braces."""
            text = match.group(1)
            weight = 1.0
            for char in match.group(0):
                if char == '[':
                    weight *= NOVEL_AI_BRACKET
                elif char == '{':
                    weight *= NOVEL_AI_BRACE
            return f'({text}:{weight:.1f})'

        prompt = BRACKET_BRACE_PATTERN.sub(replace_weights, prompt)
        return prompt
    except Exception as e:
        raise ValueError(f"An error occurred during conversion to ComfyUI: {str(e)}")

def convert_comfyui_to_novelai(prompt: str) -> str:
    """
    Convert ComfyUI prompt format to Novel AI format.
    
    Args:
        prompt (str): The input prompt in ComfyUI format.
    
    Returns:
        str: The converted prompt in Novel AI format.
    
    Raises:
        ValueError: If an error occurs during conversion.
    """
    try:
        prompt = prompt.replace(ARTIST_PREFIX, ARTIST_TEMP)

        def replace_match(match: Match[str]) -> str:
            """Convert the weight of general text to Novel AI format."""
            text, weight_str = match.groups()
            weight = float(weight_str)
            if weight == 1.0:
                return text
            elif weight < 1.0:
                brackets = int(round((1 - weight) / (1 - NOVEL_AI_BRACKET)))
                return '[' * brackets + text + ']' * brackets
            else:
                braces = int(round((weight - 1) / (NOVEL_AI_BRACE - 1)))
                return '{' * braces + text + '}' * braces

        # Handle nested weights
        while re.search(WEIGHT_PATTERN, prompt):
            prompt = WEIGHT_PATTERN.sub(replace_match, prompt)

        prompt = re.sub(r',\s*,', ', ', prompt)
        prompt = re.sub(r'(?<!\()\(|\)(?!\))', '', prompt)
        prompt = prompt.replace('\\', '')
        prompt = prompt.replace(ARTIST_TEMP, ARTIST_PREFIX)

        def artist_format(match: Match[str]) -> str:
            """Format artist name and alias."""
            artist_name, artist_alias = match.groups()
            return f'{ARTIST_PREFIX}{artist_name}_({artist_alias})'

        prompt = ARTIST_PATTERN.sub(artist_format, prompt)

        return prompt
    except Exception as e:
        raise ValueError(f"An error occurred during conversion to Novel AI: {str(e)}")

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
        """
        Convert the input prompt based on the specified conversion type.
        
        Args:
            prompt (str): The input prompt to convert.
            conversion_type (bool): True for ComfyUI to NAI, False for NAI to ComfyUI.
        
        Returns:
            Tuple[str]: A tuple containing the converted prompt.
        """
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