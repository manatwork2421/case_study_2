def convert_to_grade(score):
    if score < 0 or score > 100: 
        raise ValueError('Score must be between 0 and 100') 
    if score >= 80: 
        return 'A' 
    elif score >= 60: 
        return 'B' 
    elif score >= 40: 
        return 'C' 
    else: 
        return 'F' 
 
