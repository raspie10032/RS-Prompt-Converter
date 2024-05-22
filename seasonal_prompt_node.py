import random

# Define the seasonal fashion, backgrounds, weather, time of day, and additional poses and directions
seasonal_fashion = {
    "spring": {
        "top": ["light jacket", "floral blouse", "cardigan", "pastel blouse", "lightweight sweater", "spring scarf"],
        "bottom": ["denim skirt", "ankle boots", "flats", "capris", "culottes", "tulle skirt"],
        "one_piece": ["floral dress", "pastel jumpsuit", "sundress"],
        "accessory": ["light scarf", "sunglasses", "bracelet", "anklet"],
        "hat": ["sunhat", "beret", "wide-brim hat"]
    },
    "summer": {
        "top": ["tank top", "t-shirt", "cropped top", "halter top", "bikini top"],
        "bottom": ["shorts", "swim trunks", "mini skirt", "board shorts", "linen pants", "sarong"],
        "one_piece": ["sundress", "romper", "swimsuit"],
        "accessory": ["sunglasses", "beach bag", "shell necklace", "bracelets"],
        "hat": ["sunhat", "visor", "baseball cap"]
    },
    "autumn": {
        "top": ["sweater", "cardigan", "flannel shirt", "knitted top", "blazer"],
        "bottom": ["jeans", "ankle boots", "corduroy pants", "tweed skirt", "leggings", "culottes"],
        "one_piece": ["sweater dress", "plaid dress", "long sleeve dress"],
        "accessory": ["scarf", "beanie", "fingerless gloves", "necklace"],
        "hat": ["beret", "felt hat", "knit cap"]
    },
    "winter": {
        "top": ["wool sweater", "thermal top", "turtleneck", "fleece jacket", "puffer coat"],
        "bottom": ["thermal leggings", "snow pants", "wool skirt", "corduroy pants", "jeans", "lined trousers"],
        "one_piece": ["puffer coat dress", "knit dress", "wool dress"],
        "accessory": ["gloves", "scarf", "earmuffs", "wool socks"],
        "hat": ["beanie", "fur hat", "knit cap"]
    }
}

seasonal_backgrounds = {
    "spring": ["flower meadow", "forest path", "spring blossom garden", "rice terraces", "tulip fields", "vineyard", "flower garden", "blossoming orchard", "park with cherry blossoms"],
    "summer": ["sunset beach", "tropical rainforest", "lakeside", "coastal cliffs", "coral reef", "rocky shore", "desert dunes", "countryside field", "mountain lake"],
    "autumn": ["autumn forest", "prairie", "vineyard", "savannah", "mountain range", "canyon", "pumpkin patch", "harvest field", "cabin in the woods"],
    "winter": ["snowy landscape", "glacier", "mountain range", "canyon", "lakeside", "forest path", "frozen lake", "ice cave", "snowy village"]
}

seasonal_weather = {
    "spring": ["sunny", "partly cloudy", "light rain", "misty", "drizzling"],
    "summer": ["sunny", "partly cloudy", "clear night", "humid", "dry"],
    "autumn": ["overcast", "partly cloudy", "windy", "rainy", "foggy"],
    "winter": ["snowy", "snow flurries", "blizzard", "frosty", "clear night"]
}

seasonal_times = {
    "spring": ["morning", "late morning", "afternoon", "golden hour"],
    "summer": ["morning", "noon", "afternoon", "evening"],
    "autumn": ["morning", "afternoon", "late afternoon", "dusk"],
    "winter": ["morning", "afternoon", "evening", "night"]
}

general_composition = [
    "rule of thirds", "leading lines", "symmetry", "asymmetry", "framing", "depth of field", "negative space", "centered composition", 
    "diagonal lines", "foreground interest", "background interest", "high angle", "low angle", "wide angle", "close-up", 
    "over-the-shoulder shot", "silhouette", "reflections", "motion blur", "bokeh", "tilted frame", "panoramic view", "birds-eye view", 
    "worms-eye view", "extreme close-up", "long shot", "medium shot", "full shot", "medium close-up", "two-shot", "point of view shot", 
    "cut-in", "cutaway", "insert shot", "aerial shot", "establishing shot", "macro shot", "split screen"
]

gaze_direction = [
    "looking at the camera", "looking away", "looking to the left", "looking to the right", "looking up", "looking down", "looking over the shoulder", 
    "looking into the distance", "looking at an object", "looking at another person", "looking at the ground", "looking at the sky", "looking back", 
    "looking forward", "side glance", "upward gaze", "downward gaze", "sideways glance", "staring straight ahead", "averting eyes", 
    "focused gaze", "distracted gaze", "curious gaze", "thoughtful gaze", "intense gaze", "soft gaze", "playful gaze", "confident gaze", 
    "shy gaze", "surprised gaze"
]

poses = [
    "hands on hips", "crossed arms", "one hand in pocket", "both hands in pockets", "arms raised", "hand on chin", "looking over shoulder", 
    "sitting cross-legged", "leaning against a wall", "walking", "jumping", "kneeling", "squatting", "lying down", "hand on head", 
    "arms outstretched", "holding an object", "pointing", "hand on hip", "one leg up", "both hands on face", "spinning", "dancing", 
    "bending forward", "stretching", "leaning back", "holding a prop", "looking up", "looking down", "crouching", "balancing on one leg", 
    "twirling hair", "covering face with hands", "resting chin on hands", "hugging self", "leaning on one leg", "playing with hair", "holding a bag", 
    "holding a hat", "thumbs up", "peace sign", "waving", "hand on heart", "clapping",
    # 추가된 포즈
    "running", "jumping in mid-air", "twirling", "kicking", "reaching out", "leaping", "spinning", "dancing with wide movements", 
    "skipping", "lunging", "side step", "looking back while walking", "leaning forward as if in motion", "sitting sideways", 
    "crouching with one knee up"
]

# 새로운 리스트: 몸의 방향
body_directions = [
    "facing forward", "facing left", "facing right", "facing back", "slightly turned left", "slightly turned right", 
    "turned to the left", "turned to the right", "back to camera", "side profile left", "side profile right"
]

# Function to get random element from a list
def get_random_element(lst):
    return random.choice(lst)

class SeasonalFashionPromptNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "season": (["spring", "summer", "autumn", "winter"],),
                "seed": ("INT", {"default": 123456789012}),  # Default 12-digit seed
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_prompt"

    def generate_prompt(self, season, seed):
        random.seed(seed)  # Set the random seed to ensure different results for each seed
        fashion_category = seasonal_fashion[season]
        top = get_random_element(fashion_category["top"])
        bottom = get_random_element(fashion_category["bottom"])
        one_piece = get_random_element(fashion_category["one_piece"])
        accessory = get_random_element(fashion_category["accessory"]) if fashion_category["accessory"] else ""
        hat = get_random_element(fashion_category["hat"]) if fashion_category["hat"] else ""

        # Choose between top/bottom or one-piece outfit
        if random.choice([True, False]):
            fashion = ", ".join(filter(None, [top, bottom, accessory, hat]))
        else:
            fashion = ", ".join(filter(None, [one_piece, accessory, hat]))

        background = get_random_element(seasonal_backgrounds[season])
        weather = get_random_element(seasonal_weather[season])
        time = get_random_element(seasonal_times[season])
        composition = get_random_element(general_composition)
        gaze = get_random_element(gaze_direction)
        pose = get_random_element(poses)
        body_direction = get_random_element(body_directions)

        additional_situations = {
            "wet clothes": ["water", "light rain", "misty", "drizzling", "rainy"],
            "sweating": ["sunny", "humid"],
            "shivering": ["snowy", "snow flurries", "blizzard", "frosty"],
            "sunburn": ["beach", "tropical"],
            "dim lighting": ["evening", "night", "dusk"],
            "blowing hair": ["windy"],
            "surrounded by trees": ["forest"],
            "high altitude": ["mountain", "cliff"],
            "vast landscape": ["prairie", "savannah"],
            "rocky terrain": ["canyon"],
            "icy conditions": ["glacier"],
            "low visibility": ["foggy", "misty"],
            "rows of grapevines": ["vineyard"],
            "morning dew": ["morning", "late morning"],
            "blooming flowers": ["flower"],
            "stepped fields": ["rice terraces"],
            "colorful flowers": ["tulip fields"],
            "dry air": ["dry"],
            "calm water": ["lakeside"],
            "dramatic cliffs": ["coastal cliffs"],
            "rocky coast": ["rocky shore"],
            "warm light": ["sunset", "golden hour"],
            "dense foliage": ["tropical rainforest"],
            "cloudy sky": ["overcast"],
            "falling leaves": ["autumn forest"],
            "dry grassland": ["savannah"],
            "setting sun": ["sunset beach"],
            "heavy snow": ["blizzard"]
        }

        selected_situations = [situation for situation, conditions in additional_situations.items() 
                               if any(condition in background or condition in weather or condition in time for condition in conditions)]

        additional_situation = ", ".join(selected_situations)
        prompt = f"{season}, {fashion}, {background}, {weather}, {time}, {composition}, {gaze}, {pose}, {body_direction}, {additional_situation}"
        return (prompt,)

# 커스텀 노드 등록
NODE_CLASS_MAPPINGS = {
    "SeasonalFashionPromptNode": SeasonalFashionPromptNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SeasonalFashionPromptNode": "Seasonal Fashion Prompt Generator"
}
