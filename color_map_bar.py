import matplotlib.pyplot as plt
import numpy as np

# mAP scores for each class
classes = [
    'Blackbean', 'Flax', 'Canola', 'Kochia', 'Sugar beet', 'Soybean', 
    'Waterhemp', 'Ragweed', 'Redroot Pigweed', 'Lentil', 'Corn', 
    'Field Pea', 'Horseweed'
]

map_scores = [
    0.19007451629171496, 0.15182203900103247, 0.45902095239573476, 
    0.25710098079500787, 0.11563703920497721, 0.22971205338773876, 
    0.10694688258492979, 0.11689146306952052, 0.1502065421705096, 
    0.1793827801395323, 0.21822243856530696, 0.18454112627814437, 
    0.11439324380182794
]

# Sorting classes alphabetically and adjusting mAP scores to match
sorted_classes = sorted(classes)
sorted_map_scores = [map_scores[classes.index(c)] for c in sorted_classes]

# Generate rainbow colors and reverse the order
colors = plt.cm.rainbow(np.linspace(0, 1, len(sorted_classes)))[::-1]

# 1. Vertical Bar Plot for mAP Scores by Class (with reversed rainbow order)
plt.figure(figsize=(12, 6))
plt.bar(sorted_classes, sorted_map_scores, color=colors)
plt.xlabel('Classes')
plt.ylabel('mAP Score')
plt.title('mAP Scores by Class (Generation 0) - Reversed Rainbow Colors')
plt.xticks(rotation=45, ha='right')
plt.ylim(0, 0.5)
plt.tight_layout()
plt.show()
