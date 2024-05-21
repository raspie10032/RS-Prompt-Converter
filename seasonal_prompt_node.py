# This code was created using only ChatGPT.
# 이 코드는 ChatGPT만을 사용하여 만들었습니다.

import random

# 계절별 의상, 배경, 날씨, 시간 정의
seasonal_fashion = {
    "spring": [
        "light jacket", "floral dress", "cardigan", "pastel blouse", "denim skirt", 
        "lightweight sweater", "spring scarf", "ankle boots", "flats", "raincoat", 
        "trench coat", "chinos", "beret", "skater dress"
    ],
    "summer": [
        "sundress", "shorts", "tank top", "swimsuit", "sandals", "flip-flops", 
        "t-shirt", "sunhat", "bikini", "romper", "maxi dress", "linen pants", 
        "crop top", "sunglasses"
    ],
    "autumn": [
        "sweater", "jeans", "leather jacket", "ankle boots", "scarf", "beanie", 
        "cardigan", "flannel shirt", "combat boots", "wool coat", "turtleneck", 
        "poncho", "corduroy pants", "parka"
    ],
    "winter": [
        "coat", "thermal leggings", "wool sweater", "snow boots", "beanie", 
        "gloves", "scarf", "parka", "puffer jacket", "fleece jacket", "down vest", 
        "wool hat", "mittens", "thermal shirt"
    ]
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
        fashion = get_random_element(seasonal_fashion[season])
        background = get_random_element(seasonal_backgrounds[season])
        weather = get_random_element(seasonal_weather[season])
        time = get_random_element(seasonal_times[season])
        composition = get_random_element(general_composition)
        gaze = get_random_element(gaze_direction)
        pose = get_random_element(poses)
        prompt = f"{season}, {fashion}, {background}, {weather}, {time}, {composition}, {gaze}, {pose}"
        return (prompt,)

# 커스텀 노드 등록
NODE_CLASS_MAPPINGS = {
    "SeasonalFashionPromptNode": SeasonalFashionPromptNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SeasonalFashionPromptNode": "계절별 패션 프롬프트 생성기"
}
