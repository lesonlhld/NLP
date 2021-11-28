def variable_decorator(func):
    def wrapper(variable_name = 'x'):
        if variable_name not in wrapper.variable_count:
            wrapper.variable_count[variable_name] = 1
        else:
            wrapper.variable_count[variable_name] += 1
        return func(variable_name) + str(wrapper.variable_count[variable_name])
    wrapper.variable_count = {}
    return wrapper

@variable_decorator
def create_variable(variable_name):
  return variable_name