import state 

class Vertex(object):
    def __init__(self,  index, row, col, value, reward):
        self.index = int(index)
        self.value = value
        self.row = int(row)
        self.col = int(col)
        self.reward = reward
        self.steps = 0

class Grid(object):

    def __init__(self):
        self.vertex_list = []
        self.possible_entries = []

    def generate_from_file(self, file):
        with open(file) as f:
            result = []
            for line in f:
                if(('*' in line) or ('$' in line) or ('.' in line) or ('#' in line)):
                    result.append(list(line.replace(" ", "").rstrip()))
                else:
                    result.append(list(line.split(" ")))
            
            self.rows = int(result[0][0])
            self.cols = int(result[0][1])
            self.steps = int(result[0][2])
            self.vertex_count = 0
            row_count = 0
            for line in result[1:]:
                col_count = 0
                for character in line:
                    reward = self.getReward(character)

                    vertex = Vertex(self.vertex_count, row_count, col_count, character, reward)

                    if(character == '$'):
                        self.goal = vertex

                    self.vertex_list.append(vertex)

                    if(vertex.value not in ['*', '$']):  
                        self.possible_entries.append(vertex)

                    self.vertex_count += 1
                    col_count += 1
                    
                row_count += 1

    def vertices(self): 
        for vertex in self.vertex_list:
            print("Key: {}".format(vertex.index), "Row: {}".format(vertex.row), 
                    "Value: {}".format(vertex.value))
    
    def getReward(self, character):
        if(character == '.'):
            return -1
        elif(character == '#'):
            return 1
        elif(character == '$'):
            return 10
        else:
            return -10
        




def printStates(stateDic, rewardMap, steps):
    for(x in rows of rewardMap):
        for(y in cols of rewardMap):
            for(s in range(0, steps)):
                if((x,y,s) in stateDic.keys())
                    printState(stateDic[(x,y,s)])

                else
                    print((x, y, s), 'LEFT', 1)

def printState(state):
    maxValue = max(state.qvalues, key=state.qvalues.get())

    print((state.posX, state.posY, state.steps), maxValue, maxValue)

if __name__ == "__main__":
    printState(State(1, 1, 2, 3))