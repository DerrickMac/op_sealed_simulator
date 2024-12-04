from random import randint

# number of cards pulled after opening 6 booster packs
max_cards = 72 
deck = {}
res = []
card_pool = {
  1: 'uncommon',
  2: 'rare',
  3: 'common',
  4: 'super rare',
  5: 'rare',
  6: 'common',
  7: 'common',
  8: 'uncommon',
  9: 'super rare',
  10: 'common',
  11: 'uncommon',
  12: 'common',
  13: 'rare',
  14: 'uncommon',
  15: 'rare',
  16: 'common',
  17: 'uncommon',
  18: 'uncommon',
  19: 'common',
  20: 'rare',
  21: 'common',
  22: 'uncommon',
  23: 'super rare',
  24: 'common',
  25: 'uncommon',
  26: 'rare',
  27: 'uncommon',
  28: 'common',
  29: 'common',
  30: 'uncommon',
  31: 'rare',
  32: 'uncommon',
  33: 'common',
  34: 'rare',
  35: 'uncommon',
  36: 'common',
  37: 'super rare',
  38: 'common',
  39: 'rare',
  40: 'uncommon',
  41: 'common',
  42: 'uncommon',
  43: 'uncommon',
  44: 'uncommon',
  45: 'uncommon',
  46: 'super rare',
  47: 'common',
  48: 'super rare',
  49: 'common',
  50: 'rare',
  51: 'rare',
  52: 'common',
  53: 'uncommon',
  54: 'common',
  55: 'common',
  56: 'rare',
  57: 'rare',
  58: 'common',
  59: 'uncommon',
  60: 'common',
  61: 'uncommon',
  62: 'uncommon',
  63: 'common',
  64: 'uncommon',
  65: 'super rare',
  66: 'uncommon',
  67: 'common',
  68: 'uncommon',
  69: 'rare',
  70: 'uncommon',
  71: 'common',
  72: 'super rare',
  73: 'common',
  74: 'common',
  75: 'uncommon',
  76: 'rare',
  77: 'uncommon',
  78: 'rare',
  79: 'common',
  80: 'common',
  81: 'uncommon',
  82: 'common',
  83: 'rare',
  84: 'uncommon',
  85: 'common',
  86: 'rare',
  87: 'common',
  88: 'uncommon',
  89: 'uncommon',
  90: 'rare',
  91: 'common',
  92: 'common',
  93: 'super rare',
  94: 'common',
  95: 'rare',
  96: 'rare',
  97: 'common',
  98: 'uncommon',
  99: 'common',
  100: 'uncommon',
  101: 'rare',
  102: 'rare',
  103: 'super rare',
  104: 'rare',
  105: 'common',
  106: 'common',
  107: 'rare',
  108: 'uncommon',
  109: 'uncommon',
  110: 'common',
  111: 'common',
  112: 'common',
  113: 'common',
  114: 'common',
  115: 'uncommon',
  116: 'common',
  117: 'rare',
  118: 'secret rare',
  119: 'secret rare'
}

rarity_odds = {
    "secret rare": 2,    # 2% chance
    "super rare": 3,     # 3% chance
    "rare": 10,          # 10% chance
    "uncommon": 50       # 50% chance
}


total_cards = 0
pool_length = len(card_pool)
while total_cards < max_cards:
    card_draw = randint(1, pool_length)
    card_rarity = card_pool[card_draw]
    additional_roll = randint(1, 100)
    match card_rarity:
        case "uncommon":
            if additional_roll > rarity_odds["uncommon"]:
                continue
        case "rare":
            if additional_roll > rarity_odds["rare"]:
                continue
        case "super rare":
            if additional_roll > rarity_odds["super rare"]:
                continue
        case "secret rare":
            if additional_roll > rarity_odds["secret rare"]:
                continue
    formatted_number = f"OP09-{card_draw:03}"
    
    deck[formatted_number] = deck.get(formatted_number, 0) + 1
    total_cards += 1

for key in deck:
    formatted_string = f"{deck[key]}x{key}"
    res.append(formatted_string)

sorted_res = sorted(res)
for card in sorted_res:
    print(card)