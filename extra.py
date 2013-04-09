        def delete(self, data):
              """
              Delete node containing data

              @param data node's content to delete
              """
              # get node containing data
              node, parent = self.lookup(data)
              if node is not None:
                  children_count = node.children_count()
              if children_count == 0:
                  # if node has no children, just remove it
                  if parent.left is node:
                      parent.left = None
                  else:
                      parent.right = None
                  del node
              elif children_count == 1:
                  # if node has 1 child
                  # replace node by its child
                  if node.left:
                          n = node.left
                  else:
                          n = node.right
                  if parent:
                      if parent.left is node:
                              parent.left = n
                      else:
                              parent.right = n
                  del node
              else:
                  # if node has 2 children
                  # find its successor
                  parent = node
                  successor = node.right
                  while successor.left:
                      parent = successor
                      successor = successor.left
                  # replace node data by its successor data
                  node.data = successor.data
                  # fix successor's parent's child
                  if parent.left == successor:
                      parent.left = successor.right
                  else:
                      parent.right = successor.right
