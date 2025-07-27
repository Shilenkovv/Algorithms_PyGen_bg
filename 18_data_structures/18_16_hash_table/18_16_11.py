def is_isomorphic(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    mapping_s1_to_s2 = {}
    mapping_s2_to_s1 = {}

    for c1, c2 in zip(s1, s2):
        # Проверяем, что символ c1 однозначно отображается в c2
        if c1 in mapping_s1_to_s2:
            if mapping_s1_to_s2[c1] != c2:
                return False
        else:
            mapping_s1_to_s2[c1] = c2

        # Проверяем обратное отображение: для изоморфизма оно должно быть взаимным и уникальным
        if c2 in mapping_s2_to_s1:
            if mapping_s2_to_s1[c2] != c1:
                return False
        else:
            mapping_s2_to_s1[c2] = c1

    return True
