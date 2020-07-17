
from requestAQI import data

# def color_coding(value):
     
#     if 0 <= value <= 50:
#             data.set_background(0x66bb6a)  # good
#     if 51 <= value <= 100:
#             data.set_background(0xffeb3b)  # moderate
#     if 101 <= value <= 150:
#             data.set_background(0xf39c12)  # sensitive
#     if 151 <= value <= 200:
#             data.set_background(0xff5722)  # unhealthy
#     if 201 <= value <= 300: 
#             data.set_background(0x8e24aa)  # very unhealthy
#     if 301 <= value <= 500:
#             data.set_background(0xb71c1c) # hazardous

# likeability_scores = np.array(data)
 
# data_normalizer = mp.colors.Normalize()
# color_map = mp.colors.LinearSegmentedColormap(
#     "my_map",
#     {
#         "red": [(0, 1.0, 1.0),
#                 (1.0, .5, .5)],
#         "green": [(0, 0.5, 0.5),
#                   (1.0, 0, 0)],
#         "blue": [(0, 0.50, 0.5),
#                  (1.0, 0, 0)]
#     }
# )