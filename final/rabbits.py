import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """
        rabbitGrowth is called once at the beginning of each time step.
        
        It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.
        
        The global variable CURRENTRABBITPOP is modified by this procedure.
        
        For each rabbit, based on the probabilities in the problem set write-up,
        a new rabbit may be born.
        Nothing is returned.
        """
    global CURRENTRABBITPOP, MAXRABBITPOP, CURRENTFOXPOP
    for _ in range(CURRENTRABBITPOP):
        new_rabbit_prob = 1.0 - (CURRENTRABBITPOP/float(MAXRABBITPOP))
        if new_rabbit_prob > random.random():
            if CURRENTRABBITPOP < MAXRABBITPOP:
                CURRENTRABBITPOP += 1
    if CURRENTRABBITPOP > MAXRABBITPOP:
        CURRENTRABBITPOP = MAXRABBITPOP


def foxGrowth():
    """
        foxGrowth is called once at the end of each time step.
        
        It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.
        
        Each fox, based on the probabilities in the problem statement, may eat
        one rabbit (but only if there are more than 10 rabbits).
        
        If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.
        
        If it does not eat a rabbit, then with a 1/10 prob it dies.
        
        Nothing is returned.
        """
    global CURRENTRABBITPOP, CURRENTFOXPOP, MAXRABBITPOP
    for _ in range(CURRENTFOXPOP):
        eat_prob = CURRENTRABBITPOP/float(MAXRABBITPOP)
        if eat_prob > random.random():
            if CURRENTRABBITPOP > 10:
                CURRENTRABBITPOP -= 1
            if 1/3.0 > random.random():
                CURRENTFOXPOP += 1
        else:
            if 0.1 > random.random():
                CURRENTFOXPOP -= 1
    if CURRENTRABBITPOP < 10:
        CURRENTRABBITPOP = 10

def runSimulation(numSteps):
    """
        Runs the simulation for `numSteps` time steps.
        
        Returns a tuple of two lists: (rabbit_populations, fox_populations)
        where rabbit_populations is a record of the rabbit population at the
        END of each time step, and fox_populations is a record of the fox population
        at the END of each time step.
        
        Both lists should be `numSteps` items long.
        """
    global CURRENTRABBITPOP, CURRENTFOXPOP, MAXRABBITPOP
    rabbit_pops = [0]*numSteps
    fox_pops = [0]*numSteps
    
    for i in range(numSteps):
        rabbitGrowth()
        rabbit_pops[i] = CURRENTRABBITPOP
        foxGrowth()
        fox_pops[i] = CURRENTFOXPOP
    return (rabbit_pops, fox_pops)


r_pop, f_pop = runSimulation(200)


pylab.plot(range(200), r_pop)
pylab.plot(range(200), f_pop)
pylab.title('Forrest animals')
pylab.legend( ("Rabbits", "Foxes") )
pylab.xlabel('Time')
pylab.ylabel('Population')
#show()


pylab.coeff = pylab.polyfit(range(len(r_pop)), r_pop, 2)
pylab.plot(pylab.polyval(pylab.coeff, range(len(r_pop))))

pylab.coeff = pylab.polyfit(range(len(f_pop)), f_pop, 2)
pylab.plot(pylab.polyval(pylab.coeff, range(len(f_pop))))

pylab.show()
