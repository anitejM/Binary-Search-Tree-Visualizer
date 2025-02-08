import tkinter as tk

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BSTVisualizer:
    def __init__(self, root):
        self.root = root
        self.window = tk.Tk()
        self.window.title("BST Visualizer")
        self.canvas = tk.Canvas(self.window, width=800, height=600, bg='white')
        self.canvas.pack()
        self.node_radius = 20
        self.x_spacing = 50
        self.y_spacing = 50
        
        self.entry = tk.Entry(self.window)
        self.entry.pack()
        self.insert_button = tk.Button(self.window, text="Insert", command=self.insert_value)
        self.insert_button.pack()

    def insert_value(self):
        value = self.entry.get()
        if value.isdigit():
            self.insert(int(value))
            self.entry.delete(0, tk.END)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
        self.draw_tree()

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def draw_tree(self):
        self.canvas.delete("all")
        self._draw_node(self.root, 400, 50, 200)

    def _draw_node(self, node, x, y, x_offset):
        if node is not None:
            self.canvas.create_oval(x - self.node_radius, y - self.node_radius,
                                    x + self.node_radius, y + self.node_radius, fill='lightblue')
            self.canvas.create_text(x, y, text=str(node.value), font=('Arial', 12))
            
            if node.left:
                self.canvas.create_line(x, y, x - x_offset, y + self.y_spacing)
                self._draw_node(node.left, x - x_offset, y + self.y_spacing, x_offset // 2)
            if node.right:
                self.canvas.create_line(x, y, x + x_offset, y + self.y_spacing)
                self._draw_node(node.right, x + x_offset, y + self.y_spacing, x_offset // 2)

    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
    tree = BSTVisualizer(None)
    tree.start()