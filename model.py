import lesson.stack

class model (Object):
  """First value returned by every operation on the model is True or False
  To indicate if the operation was successful.  Additional values may also 
  be returned.

    new_number(num)
        Push a new number onto the values stack.
    
    new_op(op)
        Given an operator do what ever the operator indicates to the top 
        elements of the stack. The operator may use zero or more elements 
        of the stack.
  """

  def __init__(self):
    self.stack = stack()

    self.operators = dict()
    self.operators['ADD'] = lambda stack: stack.push(stack.pop() + stack.pop())
    self.operators['SUB'] = lambda stack: stack.push(- stack.pop() + stack.pop())
    self.operators['MUL'] = lambda stack: stack.push(stack.pop() * stack.pop())
    self.operators['DOT'] = self._dot_product
  
  def new_number(self, num):
    self.stack.push(num)
    return True

  def new_op(self, op):
    """Op is a string indicating what to do next."""
    fun = self.operators[op]
    fun(self.stack)
    return True, self.stack.top()

  def _dot_product(self):
    stack = self.stack
    dimension = stack.pop()
    total = 0
    for i in range(dimension):
      total = total + stack.pop() * stack.pop()

    stack.push(sum)