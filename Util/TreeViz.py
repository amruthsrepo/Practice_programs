class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)
    
def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1
    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y-20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x-dx, y-60, dx/2)
            jumpto(x, y-20)
            draw(node.right, x+dx, y-60, dx/2)
    import turtle
    t = turtle.Turtle()
    t.speed(0); turtle.delay(0)
    h = height(root)
    jumpto(0, 30*h)
    draw(root, 0, 30*h, 40*h)
    t.hideturtle()
    turtle.mainloop()
    
if __name__ == '__main__':
    # drawtree(deserialize('[72,71,71,70,72,70,null,null,null,71,null,null,null,null,72]'))
    drawtree(deserialize('[73,74,72,73,73,71,73,72,72,74,72,null,72,74,72,73,71,71,71,73,null,71,73,73,73,75,75,71,73,74,74,70,70,70,72,70,72,74,74,72,72,72,null,72,null,null,null,null,null,74,76,70,72,null,72,75,75,null,null,null,71,null,null,71,71,71,73,71,null,71,71,null,75,null,null,71,73,71,73,null,73,null,null,null,75,null,77,null,71,null,null,null,73,74,null,74,null,72,null,72,70,72,null,null,null,72,74,70,null,72,null,null,72,null,null,72,null,74,74,70,null,null,null,74,null,74,null,76,null,null,null,72,74,75,75,73,73,71,73,73,null,69,null,71,73,71,71,73,null,null,null,null,null,73,71,71,73,null,null,73,73,69,69,75,73,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,72,null,72,null,null,70,70,null,null,74,70,72,70,null,null,null,72,null,70,70,null,null,72,74,null,null,null,null,68,70,null,70,null,null,null,74,null,null,null,null,null,null,null,null,null,null,null,null,71,null,null,null,73,73,null,null,null,71,73,null,75,75,67,null,null,71,71,null,null,null,null,72,null,72,null,null,null,null,74,null,null,null,76,74,null,null,null,72,null,null,null,null,null,null,null,null,77,77,null,75,null,null,76,76,null,null,null,null,75,77,null,null,null,74]'))