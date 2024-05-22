import random

# Define the seasonal fashion, backgrounds, weather, time of day, and additional poses and directions
seasonal_fashion = {
    "spring": {
        "top": ["light jacket", "cardigan", "pastel blouse", "lightweight sweater", "raincoat", "trench coat", "striped tee", "blouse", "windbreaker", "denim jacket", "sweatshirt", "v-neck sweater", "kimono cardigan", "lace top", "peplum top", "bomber jacket"],
        "bottom": ["denim skirt", "chinos", "capri pants", "culottes", "midi skirt", "tapered pants", "floral skirt", "pleated trousers", "straight-leg jeans", "khaki pants", "paperbag shorts", "cargo pants", "jogger pants", "pencil skirt"],
        "one_piece": ["floral dress", "skater dress", "wrap dress", "maxi dress", "shirt dress", "tea dress", "pinafore dress", "pleated dress", "tunic dress", "ruffle dress", "sheath dress", "peasant dress", "chiffon dress", "button-front dress", "smock dress", "a-line dress", "patchwork dress", "midi wrap dress", "embroidered dress"],
        "accessory": ["spring scarf", "belt", "bracelet", "necklace", "watch", "ring", "sunglasses", "hairband", "earrings", "handbag", "tote bag", "anklet", "hair clip", "brooch", "pendant necklace", "bangle", "waist belt", "headband", "stud earrings", "crossbody bag"],
        "hat": ["beret", "bucket hat", "wide-brim hat", "cloche hat", "sun hat", "trucker hat", "visor cap", "newsboy cap", "boater hat", "panama hat", "fedora", "gambler hat", "pork pie hat", "bowler hat", "cloche hat"]
    },
    "summer": {
        "top": ["tank top", "t-shirt", "crop top", "tube top", "camisole", "sports bra", "sleeveless shirt", "off-shoulder top", "tankini top", "polo shirt", "cropped hoodie", "lace bralette", "mesh top"],
        "bottom": ["shorts", "linen pants", "denim shorts", "biker shorts", "mini skirt", "capri pants", "bermuda shorts", "athletic shorts", "wrap skirt", "high-waisted shorts", "skort", "palazzo pants", "denim capris", "ripped jeans"],
        "one_piece": ["sundress", "swimsuit", "bikini", "romper", "maxi dress", "slip dress", "halter dress", "off-the-shoulder dress", "tube dress", "backless dress", "wrap dress", "cutout dress", "beach dress", "polo dress", "kaftan", "flounce dress", "shirtdress"],
        "accessory": ["sunglasses", "bracelet", "necklace", "watch", "ring", "anklet", "hair clip", "beach bag", "shell necklace", "toe ring", "beach bag", "shell anklet", "sunblock", "beach towel", "water bottle", "visor", "beaded bracelet", "statement necklace", "tassel earrings", "wristband"],
        "hat": ["sunhat", "visor", "bucket hat", "wide-brim hat", "straw hat", "baseball cap", "boater hat", "trilby", "floppy hat", "cowboy hat", "snapback", "pith helmet", "fisherman hat"]
    },
    "autumn": {
        "top": ["sweater", "leather jacket", "cardigan", "flannel shirt", "wool coat", "turtleneck", "poncho", "plaid shirt", "henley", "quilted vest", "corduroy shirt", "fleece pullover", "wool blazer", "oversized cardigan", "knit hoodie"],
        "bottom": ["jeans", "corduroy pants", "plaid skirt", "leggings", "wide-leg pants", "corduroy pants", "leather pants", "wool skirt", "flannel-lined jeans", "cargo skirt", "denim overalls", "sweatpants", "velvet pants", "harem pants"],
        "one_piece": ["sweater dress", "knit dress", "tunic dress", "jumper dress", "wrap dress", "midi dress", "maxi dress", "shirt dress", "pinafore dress", "tweed dress", "long-sleeve dress", "suede dress", "layered dress", "knitted dress", "high-neck dress", "bohemian dress", "shift dress"],
        "accessory": ["scarf", "belt", "bracelet", "necklace", "watch", "ring", "gloves", "shawl", "earrings", "handbag", "knit scarf", "leather gloves", "satchel", "bucket bag", "wrap bracelet", "charm bracelet", "ear cuffs", "wrist watch", "shawl"],
        "hat": ["beanie", "beret", "fedora", "newsboy cap", "cloche hat", "bucket hat", "trilby", "flat cap", "newsboy cap", "felt hat", "flat cap", "wool fedora", "trapper hat", "knit cap", "pom-pom hat"]
    },
    "winter": {
        "top": ["coat", "wool sweater", "parka", "puffer jacket", "fleece jacket", "down vest", "thermal shirt", "parka", "down jacket", "turtleneck", "knit sweater", "flannel shirt", "fleece hoodie", "quilted jacket", "thermal vest", "cable-knit sweater"],
        "bottom": ["thermal leggings", "fleece pants", "wool pants", "corduroy pants", "jeans", "thermal pants", "ski pants", "snow pants", "knit pants", "sherpa-lined pants", "velvet leggings", "quilted pants"],
        "one_piece": ["sweater dress", "knit dress", "tunic dress", "jumper dress", "wrap dress", "midi dress", "maxi dress", "shirt dress", "pinafore dress", "long-sleeve knit dress", "velvet dress", "thermal dress", "cable-knit dress", "quilted dress", "long-sleeve midi dress", "plush dress"],
        "accessory": ["gloves", "scarf", "belt", "bracelet", "necklace", "watch", "ring", "earmuffs", "hand warmers", "shawl", "wool scarf", "knit gloves", "thermal socks", "leg warmers", "knit beanie", "insulated gloves", "knit headband"],
        "hat": ["beanie", "wool hat", "mittens", "trapper hat", "knit cap", "pom-pom hat", "thermal beanie", "earflap hat", "cossack hat", "winter beret"]
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
