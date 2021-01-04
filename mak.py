import pickle

a = open('collision_points.dat', 'rb')

print(pickle.load(a))
coll_loc = [(193, 1, 530, 10), (720, 2, 10, 10), (734, 20, 10, 10), (762, 47, 10, 10), (789, 75, 10, 10), (816, 98, 10, 10),
			(834, 119, 10, 10), (856, 142, 10, 10), (876, 161, 10, 10), (895, 181, 10, 10), (920, 203, 10, 10), (947, 229, 10, 10),
			(959, 249, 10, 130), (959, 369, 230, 10), (1189, 339, 10, 10), (1220, 200, 10, 130), (1220, 200, 130, 10),
			(1358, 217, 10, 10), (1376, 236, 10, 10), (1404, 260, 10, 10), (1427, 287, 10, 10), (1450, 309, 10, 10), (1472, 329, 10, 10), (1494, 354, 10, 10), (1516, 376, 10, 10),
			(1432, 435, 100, 10), (1401, 509, 10, 240), (1403, 741, 200, 10), (1603, 741, 10, 120), (1603, 861, 240, 10),
			(1833, 740, 10, 130), (1833, 740, 200, 10), (2011, 828, 10, 10), (2049, 789, 10, 10), (2056, 848, 30, 10), (2077, 850, 10, 200), (2029, 935, 50, 10), (2029, 950, 40, 10),
			(2003, 1044, 80, 10), (2003, 1044, 10, 100), (1841, 1142, 150, 10), (1837, 1028, 10, 130), (1606, 1027, 230, 10),
			(1606, 1027, 10, 150), (1407, 1170, 200, 10), (1407, 1170, 10, 220), (1408, 1382, 130, 10), (1521, 1383, 10, 100),
			(1413, 1469, 120, 10), (1413, 1469, 10, 80), (1438, 1549, 10, 80), (1408, 1689, 10, 80),
			(1341, 1827, 10, 10), (1363, 1804, 10, 10), (1384, 1782, 10, 10), (1148, 1817, 200, 10),
			(1145, 1728, 130, 10), (1145, 1728, 10, 80), (1251, 1709, 10, 10), (1221, 1685, 10, 10), (1041, 1658, 170, 10), (1041, 1658, 10, 70),
			(1091, 1720, 10, 180), (1047, 1893, 40, 10), (1047, 1893, 10, 100), (714, 2000, 340, 10), (712, 1893, 10, 100),
			(672,1893, 40, 10), (665, 1743, 10, 150), (665, 1743, 240, 10), (903, 1657, 10, 80), (626, 1658, 280, 10),
			(626, 1658, 10, 400), (290, 2044, 350, 10), (960, 536, 280, 10), (1265, 550, 10, 200), (1000, 744, 260, 10),
			(1014, 803, 20, 10), (957, 833, 10, 30), (924, 886, 10, 80), (924, 964, 280, 10), (1195, 916, 10, 50),
			(1195, 916, 280, 10), (1466, 917, 10, 100), (1263, 1017, 200, 10), (1263, 1017, 10, 470,), (626, 1494, 600, 10),
			(626, 1268, 10, 230), (555, 1265, 80, 10), (553, 1226, 160, 10), (704, 1225, 10, 200),
			(707, 1433, 350, 10), (1094, 1402, 10, 10), (1132, 1059, 10, 350), (1063, 1056, 50, 10),
			(811, 1108, 250, 10), (717, 1059, 80, 10), (554, 1093, 150, 10), (553, 942, 10, 150),
			(827, 1250, 190, 80), (554, 942, 200, 10), (780, 906, 10, 10), (818, 867, 10, 10), (849, 835, 10, 10), (889, 799, 10, 10), (921, 762, 10, 10),
			(962, 537, 10, 200), (1300, 380, 50, 50), (605, 216, 150, 100), (188, 222, 150, 100), (398, 444, 150, 100), (184, 656, 150, 100), (605, 656, 150, 100),
			(109, 1848, 10, 10), (113, 1870, 10, 10), (126, 1888, 10, 10), (135, 1901, 10, 10), (153, 1917, 10, 10), (168, 1929, 10, 10), (183, 1948, 10, 10), (202, 1966, 10, 10), (219, 1983, 10, 10), (236, 2002, 10, 10), (254, 2019, 10, 10), (271, 2036, 10, 10),
			(-541, 1845, 600, 10), (-543, 1612, 10, 240), (-695, 1615, 160, 10), (-695, 1615, 10, 150),
			(-983, 1750, 300, 10), (-1094, 1671, 10, 10), (-1078, 1685, 10, 10), (-1065, 1695, 10, 10), (-1049, 1709, 10, 10), (-1036, 1719, 10, 10), (-1023, 1728, 10, 10), (-1012, 1739, 10, 10), (-1001, 1747, 10, 10),
			(-1096, 1308, 10, 380), (-1096, 1598, 320, 10), (-784, 1457, 10, 150), (-1096, 1457, 320, 10),
			(-1096, 1308, 150, 10), (-943, 1079, 10, 230), (-803, 1079, 10, 230), (-802, 1308, 100, 10),
			(-698, 1309, 10, 150), (-699, 1447, 280, 10), (-404, 1446, 10, 240), (-406, 1679, 90, 10), (-322, 1151, 10, 540),
			(-322, 1163, 440, 10), (111, 1164, 10, 100), (101, 1275, 10, 10), (81, 1295, 10, 10), (60, 1314, 10, 10), (39, 1334, 10, 10), (24, 1352, 10, 10),
			(9, 1369, 10, 170), (-4, 1546, 10, 10), (-21, 1562, 10, 10), (-36, 1576, 10, 10), (-53, 1594, 10, 10), (-66, 1606, 10, 10), (-73, 1615, 10, 10),
			(-190, 1618, 100, 10), (-190, 1618, 10, 70), (-191, 1679, 300, 10), (112, 1455, 10, 200),
			(317, 1270, 100, 10), (303, 1270, 10, 30), (285, 1314, 10, 10), (262, 1330, 10, 10), (230, 1355, 10, 10), (211, 1368, 10, 10), (191, 1391, 10, 10), (167, 1403, 10, 10), (152, 1422, 10, 10), (131, 1435, 10, 10), (115, 1441, 10, 10),
			(270, 1514, 238, 238), (201, 1590, 50, 60), (417, 944, 10, 330), (233, 942, 190, 10), (18, 737, 10, 10), (37, 754, 10, 10), (53, 774, 10, 10), (74, 791, 10, 10), (91, 809, 10, 10), (109, 829, 10, 10), (124, 848, 10, 10), (150, 871, 10, 10), (174, 895, 10, 10), (194, 915, 10, 10), (213, 932, 10, 10),
			(19, 536, 10, 200), (-156, 535, 180, 10), (-156, 535, 10, 75), (-156, 610, 130, 10), (-38, 607, 10, 200),
			(-35, 823, 10, 10), (-19, 845, 10, 10), (-5, 855, 10, 10), (8, 869, 10, 10), (-10, 888, 10, 10), (3, 908, 10, 10), (17, 922, 10, 10), (31, 937, 10, 10), (54, 927, 10, 10), (63, 925, 10, 10), (77, 934, 10, 10), (89, 946, 10, 10), (99, 956, 10, 10), (107, 963, 10, 10),
			(-129, 697, 100, 20), (-386, 697, 100, 20), (-387, 808, 100, 20), (-132, 811, 100, 20), (109, 966, 10, 100),
			(-321, 1070, 440, 10), (-398, 994, 10, 10), (-384, 1007, 10, 10), (-374, 1022, 10, 10), (-361, 1038, 10, 10), (-350, 1052, 10, 10), (-338, 1066, 10, 10),
			(-397, 604, 10, 380), (-397, 604, 100, 10), (-294, 535, 10, 80), (-695, 535, 410, 10), (-695, 535, 10, 180), (-804, 701, 120, 10), (-804, 701, 10, 216),
			(-806, 908, 130, 10), (-674, 815, 10, 100), (-665, 804, 10, 10), (-652, 791, 10, 10), (-640, 780, 10, 10), (-627, 767, 10, 10), (-617, 759, 100, 10),
			(-486, 762, 10, 10), (-483, 772, 10, 10), (-471, 786, 10, 10), (-461, 802, 10, 10), (-445, 817, 10, 10), (-441, 830, 10, 350), (-530, 971, 100, 100),
			(-676, 1183, 240, 10), (-677, 1080, 10, 100), (-804, 1078, 130, 10), (-944, 698, 10, 220), (-1095, 698, 160, 10),
			(-1095, 577, 316, 10), (-1095, 577, 10, 120), (-789, 408, 10, 170), (-1089, 408, 300, 10), (-1049, 306, 10, 100),
			(-1037, 294, 10, 10), (-1019, 281, 10, 10), (-1005, 272, 10, 10), (-985, 258, 300, 10), (-698, 257, 10, 100),
			(-695, 364, 720, 10), (20, 172, 10, 200), (31, 159, 10, 10), (52, 140, 10, 10), (62, 127, 10, 10), (75, 116, 10, 10), (89, 100, 10, 10), (104, 82, 10, 10), (124, 65, 10, 10), (142, 45, 10, 10), (160, 29, 10, 10), (176, 16, 10, 10),
			(-311, 1377, 210, 20), (-595, 800, 60, 20), (-1096, 1602, 100, 60), (-1094, 581, 100, 40), (-1057, 906, 10, 10), (-1032, 909, 10, 10), (-1007, 908, 10, 10), (-981, 908, 10, 10), (-949, 908, 10, 10),
			(-1330, 626, 10, 10), (-1285, 626, 10, 10), (-1240, 626, 10, 10), (-1210, 626, 10, 10), (-1210, 650, 10, 10), (-1210, 680, 10, 10), (-1210, 710, 10, 10), (-1210, 740, 10, 10), (-1210, 764, 10, 10), (-1175, 764, 10, 10), (-1140, 764, 10, 10), (-1115, 764, 10, 10), (-1090, 764, 10, 10), (-1060, 764, 10, 10), (-1060, 776, 10, 10), (-1060, 797, 10, 10), (-1060, 818, 10, 10), (-1060, 818, 10, 10), (-1060, 853, 10, 10), (-1057, 878, 10, 10),
			(-1340, 648, 10, 10), (-1349, 663, 10, 10), (-1355, 687, 10, 10), (-1372, 703, 10, 10), (-1381, 721, 10, 10), (-1400, 735, 10, 10), (-1417, 765, 10, 10), (-1425, 789, 10, 10), (-1426, 825, 10, 10),
			(-1425, 857, 10, 10), (-1419, 881, 10, 10), (-1385, 885, 10, 10), (-1362, 885, 10, 10), (-1339, 888, 10, 10), (-1339, 920, 10, 10), (-1341, 952, 10, 10), (-1329, 970, 10, 10), (-1326, 992, 10, 10), (-1328, 1016, 10, 10), (-1310, 1026, 10, 10), (-1288, 1038, 10, 10), (-1297, 1059, 10, 10), (-1323, 1060, 10, 10), (-1343, 1063, 10, 10),
			(-1346, 1072, 10, 10), (-1345, 1103, 10, 10), (-1364, 1078, 10, 10), (-1388, 1085, 10, 10), (-1416, 1085, 10, 10), (-1421, 1128, 10, 10), (-1423, 1156, 10, 10), (-1423, 1183, 10, 10), (-1422, 1217, 10, 10), (-1422, 1250, 10, 10), (-1423, 1283, 10, 10),
			(-1411, 1309, 10, 10), (-1383, 1329, 10, 10), (-1362, 1343, 10, 10), (-1338, 1358, 10, 10), (-1314, 1375, 10, 10), (-1287, 1375, 10, 10), (-1245, 1375, 10, 10), (-1217, 1377, 10, 10), (-1204, 1347, 10, 10), (-1205, 1315, 10, 10), (-1205, 1279, 10, 10), (-1205, 1242, 10, 10), (-1205, 1216, 10, 10), (-1171, 1216, 10, 10),
			(-1141, 1215, 10, 10), (-1104, 1213, 10, 10), (-1071, 1216, 10, 10), (-1058, 1191, 10, 10), (-1059, 1160, 10, 10), (-1058, 1132, 10, 10), (-1058, 1108, 10, 10), (-1059, 1094, 10, 10), (-1038, 1093, 10, 10), (-1035, 1078, 10, 10), (-1012, 1078, 10, 10), (-989, 1077, 10, 10), (-962, 1077, 10, 10), (-942, 1076, 10, 10),
			]
a.close()