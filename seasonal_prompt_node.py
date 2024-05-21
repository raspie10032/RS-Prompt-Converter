# This code was created using only ChatGPT.
# 이 코드는 ChatGPT만을 사용하여 만들었습니다.

import random

# 계절별 의상, 배경, 날씨, 시간 정의
seasonal_fashion = {
    "spring": {
        "top": ["light jacket", "cardigan", "pastel blouse", "lightweight sweater", "raincoat", "trench coat"],
        "bottom": ["denim skirt", "chinos", "capri pants", "culottes", "midi skirt"],
        "one_piece": ["floral dress", "skater dress", "wrap dress", "maxi dress", "shirt dress", "tea dress", "pinafore dress", "pleated dress", "tunic dress"],
        "accessory": ["spring scarf", "belt", "bracelet", "necklace", "watch", "ring", "sunglasses", "hairband", "earrings", "handbag"],
        "hat": ["beret", "bucket hat", "wide-brim hat", "cloche hat", "sun hat"]
    },
    "summer": {
        "top": ["tank top", "t-shirt", "crop top"],
        "bottom": ["shorts", "linen pants", "denim shorts", "biker shorts", "mini skirt"],
        "one_piece": ["sundress", "swimsuit", "bikini", "romper", "maxi dress", "slip dress", "halter dress", "off-the-shoulder dress", "tube dress"],
        "accessory": ["sunglasses", "bracelet", "necklace", "watch", "ring", "anklet", "hair clip", "beach bag", "shell necklace", "toe ring"],
        "hat": ["sunhat", "visor", "bucket hat", "wide-brim hat", "straw hat", "baseball cap", "boater hat"]
    },
    "autumn": {
        "top": ["sweater", "leather jacket", "cardigan", "flannel shirt", "wool coat", "turtleneck", "poncho"],
        "bottom": ["jeans", "corduroy pants", "plaid skirt", "leggings", "wide-leg pants"],
        "one_piece": ["sweater dress", "knit dress", "tunic dress", "jumper dress", "wrap dress", "midi dress", "maxi dress", "shirt dress", "pinafore dress"],
        "accessory": ["scarf", "belt", "bracelet", "necklace", "watch", "ring", "gloves", "shawl", "earrings", "handbag"],
        "hat": ["beanie", "beret", "fedora", "newsboy cap", "cloche hat", "bucket hat", "trilby", "flat cap"]
    },
    "winter": {
        "top": ["coat", "wool sweater", "parka", "puffer jacket", "fleece jacket", "down vest", "thermal shirt"],
        "bottom": ["thermal leggings", "fleece pants", "wool pants", "corduroy pants", "jeans"],
        "one_piece": ["sweater dress", "knit dress", "tunic dress", "jumper dress", "wrap dress", "midi dress", "maxi dress", "shirt dress", "pinafore dress"],
        "accessory": ["gloves", "scarf", "belt", "bracelet", "necklace", "watch", "ring", "earmuffs", "hand warmers", "shawl"],
        "hat": ["beanie", "wool hat", "mittens", "trapper hat", "knit hat", "pom-pom hat"]
    }
}

seasonal_backgrounds = {
    "spring": ["flower meadow", "forest path", "spring blossom garden", "rice terraces", "tulip fields", "vineyard"],
    "summer": ["sunset beach", "tropical rainforest", "lakeside", "coastal cliffs", "coral reef", "rocky shore"],
    "autumn": ["autumn forest", "prairie", "vineyard", "savannah", "mountain range", "canyon"],
    "winter": ["snowy landscape", "glacier", "mountain range", "canyon", "lakeside", "forest path"]
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

general_composition = ["rule of thirds", "leading lines", "symmetry", "asymmetry", "framing", "depth of field", "negative space", "centered composition", "diagonal lines", "foreground interest", "background interest", "high angle", "low angle", "wide angle", "close-up", "over-the-shoulder shot", "silhouette", "reflections", "motion blur", "bokeh", "tilted frame", "panoramic view", "birds-eye view", "worms-eye view", "extreme close-up", "long shot", "medium shot", "full shot", "medium close-up", "two-shot", "point of view shot", "cut-in", "cutaway", "insert shot", "aerial shot", "establishing shot", "macro shot", "split screen"]
gaze_direction = ["looking at the camera", "looking away", "looking to the left", "looking to the right", "looking up", "looking down", "looking over the shoulder", "looking into the distance", "looking at an object", "looking at another person", "looking at the ground", "looking at the sky", "looking back", "looking forward", "side glance", "upward gaze", "downward gaze", "sideways glance", "staring straight ahead", "averting eyes", "focused gaze", "distracted gaze", "curious gaze", "thoughtful gaze", "intense gaze", "soft gaze", "playful gaze", "confident gaze", "shy gaze", "surprised gaze"]
poses = ["hands on hips", "crossed arms", "one hand in pocket", "both hands in pockets", "arms raised", "hand on chin", "looking over shoulder", "sitting cross-legged", "leaning against a wall", "walking", "jumping", "kneeling", "squatting", "lying down", "hand on head", "arms outstretched", "holding an object", "pointing", "hand on hip", "one leg up", "both hands on face", "spinning", "dancing", "bending forward", "stretching", "leaning back", "holding a prop", "looking up", "looking down", "crouching", "balancing on one leg", "twirling hair", "covering face with hands", "resting chin on hands", "hugging self", "leaning on one leg", "playing with hair", "holding a bag", "holding a hat", "thumbs up", "peace sign", "waving", "hand on heart", "clapping"]

# 리스트에서 무작위 요소를 선택하는 함수
def get_random_element(lst):
    return random.choice(lst)

class SeasonalFashionPromptNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "season": (["spring", "summer", "autumn", "winter"],),
                "seed": ("INT", {"default": 123456789012}),  # 기본 12자리 시드 값
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_prompt"

    def generate_prompt(self, season, seed):
        random.seed(seed)  # 각 시드 값에 대해 다른 결과를 보장하기 위해 무작위 시드 설정
        fashion_category = seasonal_fashion[season]
        if random.choice([True, False]):  # 상의와 하의를 한 세트로 선택
            top = get_random_element(fashion_category["top"])
            bottom = get_random_element(fashion_category["bottom"]) if fashion_category["bottom"] else ""
            one_piece = ""
        else:  # 원피스를 선택
            top = ""
            bottom = ""
            one_piece = get_random_element(fashion_category["one_piece"]) if fashion_category["one_piece"] else ""

        accessory = get_random_element(fashion_category["accessory"]) if fashion_category["accessory"] else ""
        hat = get_random_element(fashion_category["hat"]) if fashion_category["hat"] else ""

        fashion = ", ".join(filter(None, [top, bottom, one_piece, accessory, hat]))

        background = get_random_element(seasonal_backgrounds[season])
        weather = get_random_element(seasonal_weather[season])
        time = get_random_element(seasonal_times[season])
        composition = get_random_element(general_composition)
        gaze = get_random_element(gaze_direction)
        pose = get_random_element(poses)

        # 추가적인 상황 반영
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
        prompt = f"{season}, {fashion}, {background}, {weather}, {time}, {composition}, {gaze}, {pose}, {additional_situation}"
        return (prompt,)

# 커스텀 노드 등록
NODE_CLASS_MAPPINGS = {
    "SeasonalFashionPromptNode": SeasonalFashionPromptNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SeasonalFashionPromptNode": "Seasonal Fashion Prompt Generator"
}
