class State:
    def __init__(self,missionaries_left,cannibals_left,boat_left,missionaries_right,cannibals_right):
        self.missionaries_left=missionaries_left
        self.cannibals_left=cannibals_left
        self.boat_left=boat_left
        self.missionaries_right=missionaries_right
        self.cannibals_right=cannibals_right
    
    def is_valid(self):
        if(
            0<=self.missionaries_left<=3 and
            0<=self.cannibals_left<=3 and
            0<=self.missionaries_right<=3 and
            0<=self.cannibals_right<=3 ):
            if(
                self.missionaries_left >= self.cannibals_left or
                self.missionaries_left == 0  and
                self.missionaries_right >= self.cannibals_right or
                self.missionaries_right == 0):
                return True
            return False
    
    def is_goal(self):
        return self.missionaries_left == 0 and self.cannibals_left == 0
    
    def __eq__(self,other):
        return(
            self.missionaries_left==other.missionaries_left,
            self.cannibals_left==other.cannibals_left,
            self.boat_left==other.boat_left,
            self.missionaries_right==other.missionaries_right,
            self.cannibals_right==other.cannibals_right,
            )
    
    def __hash__(self):
        return hash((
            self.missionaries_left,
        self.cannibals_left,
        self.boat_left,
        self.missionaries_right,
        self.cannibals_right,
        ))

def generate_next_states(current_state):
    next_states=[]
    moves=[(1,0),(2,0),(0,1),(0,2),(1,1)]
    for m,c in moves:
        if current_state.boat_left:
            new_state=State(
                current_state.missionaries_left -m,
                current_state.cannibals_left -c,
                1-current_state.boat_left,
                current_state.missionaries_right +m,
                current_state.cannibals_right +c
            )
        else:
             new_state=State(
                current_state.missionaries_left +m,
                current_state.cannibals_left +c,
                1-current_state.boat_left,
                current_state.missionaries_right -m,
                current_state.cannibals_right -c
            )
        if new_state.is_valid():
            next_states.append(new_state)
    return next_states

def gbfs_search(current_state,path,visited):
    if current_state.is_goal():
        return path
    visited.add(current_state)
    next_states=generate_next_states(current_state)
    for next_state in next_states:
        if next_state not in visited:
            result=gbfs_search(next_state, path + [next_state],visited)
            if result:
                return result
    return None    
    
def print_state_description(state):
    left_shore = f"{state.missionaries_left} Missionaries and {state.cannibals_left} Cannibals on left shore"
    right_shore = f"{state.missionaries_right} Missionaries and {state.cannibals_right} Cannibals on right shore"
    print(f"{left_shore},{right_shore}\n")

if __name__ == "__main__":
    start_state=State(3,3,1,0,0)
    visited= set()
    solution_path=gbfs_search(start_state,[start_state],visited)
    if solution_path:
        print("Solution: \n")
        for i,state in enumerate(solution_path):
            print(f"Step {i + 1}:")
            print_state_description(state)