import matplotlib.pyplot as plt

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

# Fitness scores for the first generation
generation = [0]
best_fitness = [0.19030400443738288]
mean_fitness = [0.17685672789710716]

# 1. Bar Plot for mAP Scores by Class
plt.figure(figsize=(12, 6))
plt.barh(classes, map_scores, color='teal')
plt.xlabel('mAP Score')
plt.title('mAP Scores by Class (Generation 0)')
plt.xlim(0, 0.5)
plt.tight_layout()
plt.show()

# 2. Line Plot for Best and Mean Fitness Scores
plt.figure(figsize=(12, 6))
plt.plot(generation, best_fitness, label='Best Fitness', marker='o', color='green')
plt.plot(generation, mean_fitness, label='Mean Fitness', marker='o', color='orange')
plt.xlabel('Generation')
plt.ylabel('Fitness Score')
plt.title('Best and Mean Fitness Scores (Generation 0)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
