import numpy as np


class HistogramFilter(object):
    """
    Class HistogramFilter implements the Bayes Filter on a discretized grid space.
    """
    def transition_mat(self, M, N, action):

        T = np.identity(M*N) * 0.1
        action = (-action[1], action[0])
       
        if action == (10,):             #right
            for i in range(M*N):
                next_state = i+1
                if i % N == N-1:
                    T[i, i] = 1
                else:
                    T[i, next_state] = 0.9

        if action == (0,-1):            #left
            for i in range(M*N):
                next_state = i-1
                if i % N == 0:
                    T[i,i] = 1 
                else: 
                    T[i, next_state] = 0.9
                
        if action == (1,0):            #down
            for i in range(M*N):
                next_state = i
                if N+next_state < M*N:
                    T[i, N+next_state] += 0.9
            for i in range(M*N-M,M*N):
                for j in range(M*N-N,M*N):
                    if i==j:
                        T[i,j] = 1
        
        if action == (-1,0):             #up
            for i in range(M*N):
                next_state = i+1
                if N+next_state <= M*N:
                    T[N+next_state-1,i] += 0.9
            for i in range(N):
                for j in range(N):
                    if i==j:
                        T[i,j] = 1

        return T

    def histogram_filter(self, cmap, belief, action, observation):
        '''
        Takes in a prior belief distribution, a colormap, action, and observation, and returns the posterior
        belief distribution according to the Bayes Filter.
        :param cmap: The binary NxM colormap known to the robot.
        :param belief: An NxM numpy ndarray representing the prior belief.
        :param action: The action as a numpy ndarray. [(1, 0), (-1, 0), (0, 1), (0, -1)]
        :param observation: The observation from the color sensor. [0 or 1].
        :return: The posterior distribution.
        '''
        
        M = cmap.shape[0]
        N = cmap.shape[1]

        T = self.transition_mat(M, N, action)
        print(cmap)
        M_xy = np.zeros((M*N, 2))
        for i in range(M*N):
            for j in range(2):
                if cmap.flatten()[i] == j:
                    M_xy[i,j] = 0.9
                    M_xy[i,1-j] = 0.1

        alpha_in = belief.flatten()

        alpha_kT = np.multiply(M_xy[:,observation], np.dot(alpha_in.T, T))
       
        posterior = alpha_kT.T / np.sum(alpha_kT.T)
        posterior = posterior.reshape(M, N)

        return posterior

        
                    


        

       
