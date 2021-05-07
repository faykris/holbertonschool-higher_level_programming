#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    m_key = ""
    m_val = 0
    best_key = {}
    for key, value in a_dictionary.items():
        if value > m_val:
            m_key = key
            m_val = value
    best_key[m_key] = m_val
    return m_key
