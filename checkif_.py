from text_normalizer.normalizer import TextNormalizer


txt_normalizer = TextNormalizer()
input_text = "T̵̰̋͊ȩ̷͍̌̈ṣ̶̨̰̂͐͗t̴͓̱̗͌͋ ̵̗̲̌͝c̴̻̭̃a̶͕͕̓s̵̨͛̑e̶͔̲̽́ "

normalized_text = txt_normalizer.normalize(input_text)
print(normalized_text)