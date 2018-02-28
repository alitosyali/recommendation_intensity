def recommendation_intensity(R, L):

	'''
	R: the list of top-k returned objects of a ranking approach
	L: the list of ground truth

	Wang, S., Xie, S., Zhang, X., Li, Z., Yu, P. S., & Shu, X. (2014, April). 
	Future influence ranking of scientific literature. In Proceedings of the 
	2014 SIAM International Conference on Data Mining (pp. 749-757). Society 
	for Industrial and Applied Mathematics.
	'''


	k = len(R)

	intensity = 0
	for i in range(k):
		if R[i] in L:
			o_r = L.index(R[i])
			intensity += 1 + (k-(o_r+1))/k

	return intensity

# example
L = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"]
R = ["A2", "A11", "A6", "A13", "A5", "A15", "A4", "A18", "A10", "A9"]

print(recommendation_intensity(R, L))