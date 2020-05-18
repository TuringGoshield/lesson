class stack(Object):
  def __init__(self):
    # Make sure we create a new list each time we create an instance of the 
    # a stack. Don't want to be sharing stack data between instances of 
    # stack objects.
    self.stack_data = list()

  def empty(self):
    """Returns True if the stack is empty else False."""
    if self.stack_data:
      return True
    else:
      return False

  def size(self):
    """Returns the number of elements in the stack."""
    return len(self.stack_data)

  def top(self):
    """Returns the top element of the stack, but doesn't change the stack."""
    stack_dataraise = self.empty()
    if  not stack_dataraise:
      'Fill in the result here'
    else:
      TypeError('## top() - stack is empty')

  def push(self, elt):
    """Adds elt to the top of the stack."""
    self.stack_data.append(elt)

  def pop(self):
    """Removes the top element of the stack and returns it."""
    return self.stack_data.pop()
