#Read one line containing several scores separated by spaces.
#  Write grade(score): 90 and above is A, 80 to 89 B,
#  70 to 79 C, 60 to 69 D, below 60 F. 
# A token is valid only if it is a whole number 
# from 0 to 100; anything else (for example -5, abc,
#  4.5, 101) is printed as <token>: invalid and is 
# excluded from the average. Print <score>: <grade>
#  for valid scores, then Average of valid
#  scores: <value> with one decimal, or No valid scores when there are none.



def grade(score):
    if score >= 90:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"
    
        
scores = input().split()
# print(scores)
valid_scores = []
for token in scores:
    if token.isdigit() and 0<= int(token) <= 100:
        num = int(token)
        print(f"{num}: {grade(num)}")
        valid_scores.append(num)
    else:
        print(f"{token}: invalid")
if valid_scores:
    avg = sum(valid_scores) / len(valid_scores)
    print(f"Average of valid scores: {avg:.1f}")
else:
    print("No valid scores")
