
# Please write proper comments with explanation
def check_pass(input_pass):
    valid_pass = []
    current_pass = ""
    for character in input_pass:
        if character != ',':
            current_pass += character
        else:
            if 6 <= len(current_pass) <= 12:
                matched_with_lower = matched_with_upper = matched_with_digit = matched_with_special = False
                for char in current_pass:
                    if 'a' <= char <= 'z':
                        matched_with_lower = True
                    elif 'A' <= char <= 'Z':
                        matched_with_upper = True
                    elif '0' <= char <= '9':
                        matched_with_digit = True
                    elif char in '$#@':
                        matched_with_special = True
                if matched_with_lower and matched_with_upper and matched_with_digit and matched_with_special:
                    valid_pass.append(current_pass)
            current_pass = ""   
    if current_pass:
        if 6 <= len(current_pass) <= 12:
            matched_with_lower = matched_with_upper = matched_with_digit = matched_with_special = False
            for char in current_pass:
                if 'a' <= char <= 'z':
                    matched_with_lower = True
                elif 'A' <= char <= 'Z':
                    matched_with_upper = True
                elif '0' <= char <= '9':
                    matched_with_digit = True
                elif char in '$#@':
                    matched_with_special = True
            if matched_with_lower and matched_with_upper and matched_with_digit and matched_with_special:
                valid_pass.append(current_pass)   
    return ",".join(valid_pass)
input_pass = "ABd1234@1,a F1#,2w3E*,2We3345"
valid = check_pass(input_pass)
print(valid)
