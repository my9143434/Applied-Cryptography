def modular_inverse(e, phi_n):
    temp_remainder = 0
    test_d = 0
    while temp_remainder != 1:
        test_d += 1
        print(test_d)
        temp_remainder = (e * test_d) % phi_n

    return test_d


d = modular_inverse(17, 60)
print(d)
