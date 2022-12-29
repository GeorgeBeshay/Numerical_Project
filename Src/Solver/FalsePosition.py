import math

def roundsig(x, digits=6):
    if x == 0 or not math.isfinite(x):
        return x
    digits -= math.ceil(math.log10(abs(x)))
    return round(x, digits)


def false_position(function, x_lower, x_upper, tolerance, maxit = 50, sigdig = 10):
    fx_lower = roundsig(eval(function, {"x": x_lower}), sigdig)
    fx_upper = roundsig(eval(function, {"x": x_upper}), sigdig)
    steps = f'\nf(x) = {function}\nInitial boundaries: Xl = {x_lower}, Xu = {x_upper}, f(Xl) = {fx_lower}, f(Xu) = {fx_upper}.\n'

    if (fx_lower*fx_upper > 0):
        steps += f'Error! f(Xl) and f(Xu) have the same sign which means the interval has no root.'
        return steps

    steps += f'For every iteration: f(Xl)*f(Xu)<0, Xr(new) = Xu - f(Xu)*(Xu-Xl)/(f(Xu)-f(Xl)), tol = Xr(new) - Xr(old).\n'

    xr = 0
    fxr = 0
    i = 0
    while(i<maxit):
        steps += f'\n================================ Iteration {i+1} ================================\n'
        xr = roundsig(x_upper - fx_upper*(x_upper-x_lower)/(fx_upper-fx_lower), sigdig)
        fxr = roundsig(eval(function, {"x" : xr}), sigdig)
        steps += f'Xl = {x_lower}\nXu = {x_upper}\nf(Xl) = {fx_lower}\nf(Xu) = {fx_upper}\n'
        steps += f'Xr = {x_upper} - ({fx_upper})*({x_upper}-({x_lower}))/({fx_upper}-({fx_lower})) = {xr}\nf(Xr) = {fxr}\n'
        
        if i>0:
            err = roundsig(abs(xr-xr_old), sigdig)
            steps += f'The absolute approximate error is {err}'
            if err < tolerance:
                steps += f' < {tolerance}, so we stop iterating. \n\n\n The estimated root Xr = {xr}, and f(Xr) = {fxr} .'
                return steps
            steps += f'\n'
        xr_old = xr

        if fxr == 0:
            steps += f'\n\n\n An exact zero at X = {xr} is found.'
            return steps
        elif fxr*fx_lower < 0:
            x_upper = xr
            fx_upper = fxr
            steps += f'Since f(Xr)*f(Xl)<0, Xr will be the new Xu = {x_upper}.\n'
        else:
            x_lower = xr
            fx_lower = fxr
            steps += f'Since f(Xr)*f(Xu)<0, Xr will be the new Xl = {x_lower}.\n'

        i += 1 

    steps += f'\n\n\nMaximum iterations were reached and no root was found to the desired tolerance.\n'
    steps += f'Calculations lead to approximation Xr = {xr}, f(Xr) = {fxr} .'
    return steps

print(false_position(function = "x**3-x-1", x_lower=1, x_upper=2, tolerance=0.0001, sigdig=5))