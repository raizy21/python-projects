print('grade calculator app')
scores = []

while True:
    score = input("enter a score (or 'done' to finish): ")
    
    if score.lower() == 'done':
        print("goodbye!")
        break
   
    scores.append(float(score))
    average_score = sum(scores) / len(scores)
    print(f"current average score: {average_score:.1f}")
    if average_score >= 90:
        print("grade: A")
    elif average_score >= 80:
        print("grade: B")
    elif average_score >= 70:
        print("grade: C")
    elif average_score >= 60:
        print("grade: D")
    else:
        print("grade: F")