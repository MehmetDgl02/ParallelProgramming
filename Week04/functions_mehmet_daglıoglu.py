custom_power = lambda x=0,/,e=1: x*e;

def custom_equation(x=0,y=0,/,a=1,b=1,*,c=1):
    '''
    This function computes the resul of the equation 
    
    
    :param arg1: Positional Only integer base for the first term
    :param arg2: Positional Only integer base for the second term
    :param arg3: Positional/ Keyword integer exponent for the first term
    :param arg4: Positional / Keyword integer exponent for the first term
    :param arg5: Keyword Only integer divisor
    :return: The result as a float

    '''
    return (x**a+y**b)/c 

def fn_w_counter():
    if not hasattr(fn_w_counter, "total_calls"):
        fn_w_counter.total_calls = 0
        fn_w_counter.callers = {}
    
   
    fn_w_counter.total_calls += 1

    
    caller_name = __name__
    
   
    if caller_name in fn_w_counter.callers:
        fn_w_counter.callers[caller_name] += 1
    else:
        fn_w_counter.callers[caller_name] = 1

    
    return fn_w_counter.total_calls, fn_w_counter.callers
