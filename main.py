from typing import TypedDict
from langgraph.graph import END, StateGraph

# Lets make our state

class State(TypedDict):
    number : int

#now lets make nodes

# NODE: 1 (double)
def double(state:State) -> dict:
    boardNum = state["number"]
    newNumber = boardNum * 2 
    print(f"In Double: {newNumber}")

    return {"number" : newNumber}

# NODE: 2 (finish)

def finish(state: State) -> dict:
    boardNum = state["number"]
    print("In Finish")
    print(boardNum)

    return {"number" : boardNum}


# LETS MAKE A HELPER FUNCTION 

def decision(state : State) -> str:
    if(state["number"] < 100):
        return "double"
    else:
        return "finish"


# NOW LETS ADD THESE TO GRAPH

# lets initialize our graph

builder = StateGraph(State)

# lets add nodes (name and function_name)

builder.add_node("double",double)

builder.add_node("finish",finish)


# ENTRY POINT (from which point to start the program)
# HERE WE START FROM DOUBLE NODE:
# here we add just the name of entry node -> with just name

builder.set_entry_point("double")

#Now add conditional edge -> here is num < 100 then call double , if >=100 call finish

# Here we first add name of "start node" then add the "func_name" of decision maker , then in a dict write for what value of decision maker which
# node will be called. 

builder.add_conditional_edges("double", decision, {"double" : "double", "finish":"finish"})

# add a simple edge saying when you reach finish END it

builder.add_edge("finish",END)

# graph banalo

graph = builder.compile()


# NOW TO RUN

if __name__ == "__main__":
    result = graph.invoke({"number" : 2})
