score=0
def add_points(points=10):
    global score
    score+=points
    print(f"Score after adding points: {score}")
def reset_score():
    global score
    print(f"Score after reset: {score}")
    
