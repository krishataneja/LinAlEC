
def belongs_to_span(vec_set, target_vec):
    for i in range(len(vec_set)):
        scalar = target_vec[0] / vec_set[i][0] if vec_set[i][0] != 0 else 0
        if all(scalar * vec_set[i][j] == target_vec[j] for j in range(len(target_vec))):
            return True
    return False


def find_representation(vec_set, target_vec):
    coefficients = []
    for i in range(len(vec_set)):
        multiplier = target_vec[0] / vec_set[i][0] if vec_set[i][0] != 0 else 0
        if all(multiplier * vec_set[i][j] == target_vec[j] for j in range(len(target_vec))):
            coefficients.append(multiplier)
    return coefficients if coefficients else None

def compare_spans(set1, set2):
    for vec in set1:
        if not belongs_to_span(set2, vec):
            return False
    for vec in set2:
        if not belongs_to_span(set1, vec):
            return False
    return True


def coordinates_in_basis(basis, target_vec):
    coords = []
    for base_vec in basis:
        scale = sum(base_vec[i] * target_vec[i] for i in range(len(target_vec))) / sum(base_vec[j] ** 2 for j in range(len(base_vec)))
        coords.append(scale)
    return coords

def basis_transformation_matrix(basis1, basis2):
    matrix = []
    for vec in basis2:
        row = coordinates_in_basis(basis1, vec)
        matrix.append(row)
    return matrix


def switch_basis(vec, basis1, basis2):
    transform = basis_transformation_matrix(basis1, basis2)
    result = []
    for i in range(len(transform[0])):
        value = sum(transform[j][i] * vec[j] for j in range(len(vec)))
        result.append(value)
    return result


S = [[1, 0], [0, 1]]
v = [2, 3]
print("In Span:", belongs_to_span(S, v))
print("Representation:", find_representation(S, v))

S1 = [[1, 0], [0, 1]]
S2 = [[2, 0], [0, 2]]
print("Same Span:", compare_spans(S1, S2))

B = [[1, 0], [0, 1]]
print("Coordinates:", coordinates_in_basis(B, v))

B1 = [[1, 0], [0, 1]]
B2 = [[2, 0], [0, 2]]
print("COB Matrix:", basis_transformation_matrix(B1, B2))

print("New Basis:", switch_basis(v, B1, B2))
