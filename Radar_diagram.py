# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:07:01 2024

@author: 10364

"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False

stats = [
    {"Ag 1": 382, "Ag 2": 369, "Farmer1": 415, "Farmer2": 401, "GPT-4": 387},
    {"Ag 1": 337, "Ag 2": 321, "Farmer1": 381, "Farmer2": 370, "GPT-4": 402},
    {"Ag 1": 221, "Ag 2": 208, "Farmer1": 267, "Farmer2": 237, "GPT-4": 275},

]

data_length = len(stats[0])

angles = np.linspace(0, 2 * np.pi, data_length, endpoint=False)
labels = [key for key in stats[0].keys()]
score = [[v for v in stat.values()] for stat in stats]

score_a = np.concatenate((score[0], [score[0][0]]))
score_b = np.concatenate((score[1], [score[1][0]]))
score_c = np.concatenate((score[2], [score[2][0]]))

angles = np.concatenate((angles, [angles[0]]))
labels = np.concatenate((labels, [labels[0]]))

fig = plt.figure(figsize=(4.5, 4.5), dpi = 900)

ax = plt.subplot(111, polar=True)

ax.plot(angles, score_a, color='m')
ax.plot(angles, score_b, color='g')
ax.plot(angles, score_c, color='r')


ax.set_thetagrids( angles * 180 / np.pi, labels, fontsize = "10.5")

ax.set_theta_zero_location('N')  # E W S N SW SE NW NE

ax.set_rlim(0, 500)

ax.set_rlabel_position(270)
#ax.set_title("Comparative performances of three models")
plt.legend(["ChatAgronomist", "ChatGPT-3.5", "LLaMA-7B"], bbox_to_anchor = (1.35, 1), loc = 0, borderaxespad = 0.1, fontsize = "10")

ax.set_rlim(150, 450)

plt.show()
