class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs


    def __call__(self, x):
        return sum(c * (x ** i) for i, c in enumerate(self.coeffs))


    def __add__(self, other):
        max_len = max(len(self.coeffs), len(other.coeffs))
        new_coeffs = [0] * max_len
        for i in range(max_len):
            c1 = self.coeffs[i] if i < len(self.coeffs) else 0
            c2 = other.coeffs[i] if i < len(other.coeffs) else 0
            new_coeffs[i] = c1 + c2
        return Polynomial(new_coeffs)


    def __eq__(self, other):
        return self.coeffs == other.coeffs


    def __repr__(self):
        terms = []
        for i, c in enumerate(self.coeffs):
            if c:
                if i == 0:
                    terms.append(str(c))
                elif i == 1:
                    terms.append(f"{c}x")
                else:
                    terms.append(f"{c}x^{i}")
        return "Polynomial(" + " + ".join(reversed(terms)) + ")"
