import prefsampling as ps

def defaultCubeValues():
    return [1,3,5,15]
def euclideanCube(numVot, numCand, numDim, seed):
    return ps.ordinal.euclidean(seed=seed, num_voters=numVot, num_candidates=numCand, num_dimensions=numDim, voters_positions=ps.EuclideanSpace.UNIFORM_CUBE, candidates_positions=ps.EuclideanSpace.UNIFORM_CUBE)


def defaultBallValues():
    return [3,5,15]
def euclideanBall(numVot, numCand, numDim, seed):
    return ps.ordinal.euclidean(num_voters=numVot, num_candidates=numCand, num_dimensions=numDim,
                                voters_positions=ps.EuclideanSpace.UNIFORM_BALL,
                                candidates_positions=ps.EuclideanSpace.UNIFORM_BALL, seed=seed)


def impartial(numVot, numCand, seed):
    return ps.ordinal.impartial(num_voters=numVot, num_candidates=numCand, seed=seed)


def getDefaultMallowsValues():
    return [0.5,0.7,0.9]
def mallowsNormalized(numVot, numCand, phi, seed):
    return ps.ordinal.norm_mallows(num_voters=numVot, num_candidates=numCand, norm_phi=phi, seed=seed)


def getDefaultUrnModelsValues():
    return [0.05, 0.15, 0.3]
def urn(numVot, numCand, alpha, seed):
    return ps.ordinal.urn(num_voters=numVot, num_candidates=numCand, alpha=alpha, seed=seed)


