# LangGraph Conditional Workflow

A beginner-friendly implementation of a conditional workflow using **LangGraph and Python**.

This project demonstrates how LangGraph organizes program execution using three core building blocks: **State, Nodes, and Edges**.

The workflow takes an initial number, repeatedly doubles it, and stops when the number reaches or exceeds 100.

## 🚀 Project Overview

The goal is to understand how LangGraph works internally without using an LLM.

For this implementation:

- Start with an initial number.
- Double the number.
- Check whether the number is less than 100.
- If YES, execute the `double` node again.
- If NO, execute the `finish` node and terminate the workflow.

### Workflow Example

```text
START
  |
  v
DOUBLE NODE
  |
  v
Is number < 100?
  |
  |---- YES ----> DOUBLE NODE (Repeat)
  |
  |---- NO -----> FINISH NODE
                      |
                      v
                     END
```

## 🧠 Core LangGraph Concepts

This project demonstrates three fundamental concepts:

### 1. State

State represents the shared data available throughout the workflow.

We use Python's `TypedDict` to define the structure of our state.

```python
from typing import TypedDict

class State(TypedDict):
    number: int
```

Here, `number` stores the current integer value.

### 2. Nodes

Nodes are Python functions that perform individual tasks and can update the workflow state.

**Double Node**

Doubles the current number and returns the updated state.

```python
def double(state: State) -> dict:
    boardNum = state["number"]
    newNumber = boardNum * 2

    print(f"In Double: {newNumber}")

    return {"number": newNumber}
```

**Finish Node**

Prints the final number and returns the state.

```python
def finish(state: State) -> dict:
    boardNum = state["number"]

    print("In Finish")
    print(boardNum)

    return {"number": boardNum}
```

### 3. Edges

Edges define how execution moves between nodes.

**Conditional Routing**

The decision function determines which node executes next.

```python
def decision(state: State) -> str:
    if state["number"] < 100:
        return "double"
    else:
        return "finish"
```

We connect the nodes using `add_conditional_edges()`:

```python
builder.add_conditional_edges(
    "double",
    decision,
    {
        "double": "double",
        "finish": "finish"
    }
)
```

This creates a loop when the number is less than 100 and routes execution to the finish node otherwise.

## ⚙️ Technologies Used

- Python
- LangGraph
- TypedDict
- Conditional Routing
- Graph-based Workflow Execution

## 📂 Project Structure

```text
langgraph-conditional-workflow/
│
├── main.py
├── requirements.txt
└── README.md
```

## 🛠️ Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/langgraph-conditional-workflow.git
```

**2. Navigate to the project directory**

```bash
cd langgraph-conditional-workflow
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

Activate it:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Run the project**

```bash
python main.py
```

## 📊 Expected Output

With an initial value of `5`:

```text
In Double: 10
In Double: 20
In Double: 40
In Double: 80
In Double: 160
In Finish
160
```

The workflow terminates when the number reaches 100 or more.

## 🔑 Important LangGraph Methods Learned

| Method | Purpose |
|---|---|
| `StateGraph()` | Initializes the workflow graph |
| `add_node()` | Registers a Python function as a node |
| `set_entry_point()` | Defines the starting node |
| `add_conditional_edges()` | Implements conditional routing |
| `add_edge()` | Creates a direct connection |
| `compile()` | Compiles the graph |
| `invoke()` | Executes the workflow |

## 💡 Key Takeaway

LangGraph is not limited to LLM-based applications.

It can also organize ordinary Python logic into structured workflows using shared state, nodes, and edges.

This implementation helped me understand the fundamentals of graph-based execution, conditional routing, and looping workflows before moving towards more advanced AI agent applications.

---

**Learning in Public | AI Engineering Journey**

If you find this project useful, feel free to ⭐ the repository!
