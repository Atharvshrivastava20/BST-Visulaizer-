import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

class BSTVisualizer:
    def __init__(self, bst):
        self.bst = bst
        self.graph = nx.DiGraph()

    def add_edges(self, node, pos, x=0, y=0, layer=1):
        if node is not None:
            self.graph.add_node(node.val, pos=(x, y))
            if node.left:
                self.graph.add_edge(node.val, node.left.val)
                l = x - 1 / layer
                self.add_edges(node.left, pos, x=l, y=y-1, layer=layer+1)
            if node.right:
                self.graph.add_edge(node.val, node.right.val)
                r = x + 1 / layer
                self.add_edges(node.right, pos, x=r, y=y-1, layer=layer+1)

    def visualize(self):
        pos = {}
        self.add_edges(self.bst.root, pos)
        pos = nx.get_node_attributes(self.graph, 'pos')
        nx.draw(self.graph, pos, with_labels=True, arrows=False)
        plt.show()

def main():
    bst = BST()
    visualizer = BSTVisualizer(bst)
    commands = ['insert', 'visualize', 'exit']
    completer = WordCompleter(commands, ignore_case=True)

    while True:
        user_input = prompt('Enter command: ', completer=completer)
        if user_input.lower() == 'exit':
            break
        elif user_input.lower().startswith('insert'):
            try:
                _, value = user_input.split()
                value = int(value)
                bst.insert(value)
                print(f'Inserted {value} into the BST.')
            except ValueError:
                print('Invalid input. Use "insert <value>".')
        elif user_input.lower() == 'visualize':
            visualizer.visualize()
        else:
            print('Unknown command. Available commands: insert, visualize, exit.')

if __name__ == "__main__":
    main()