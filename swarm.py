import random
from particle import Particle  

class Swarm:
    def __init__(self, tsplib_problem, swarm_size, problem_size):
        self.swarm_size = swarm_size
        self.problem_size = problem_size
        self.tsplib_problem = tsplib_problem 
        self.particles = []
        self.global_best_position = None 
        self.global_best_distance = float('inf')
        self.epochs = 0


    def initialize_particles(self):
        for _ in range(self.swarm_size):
            nodes = list(self.tsplib_problem.get_nodes())
            position = random.sample(nodes, len(nodes))
            velocity = self.random_velocity()
            particle = Particle(position, velocity, self.tsplib_problem)
            self.particles.append(particle)
            if particle.personal_best_distance < self.global_best_distance:
                self.global_best_position = particle.personal_best_position[:]
                self.global_best_distance = particle.personal_best_distance


    def random_velocity(self, velocity_length=5):
        swaps = []
        for _ in range(velocity_length):
            i, j = random.sample(range(self.problem_size), 2)
            swaps.append((i, j))

        return swaps 


    def simulate(self, max_epochs=100, inertia_weight=0.5, cognitive_coefficient=1.5, social_coefficient=1.5):
        self.initialize_particles()
        while self.epochs < max_epochs:
            for particle in self.particles:
                particle.update_velocity(self.global_best_position, inertia_weight, cognitive_coefficient, social_coefficient)
                particle.update_position()

                if particle.personal_best_distance < self.global_best_distance:
                    self.global_best_position = particle.personal_best_position[:]
                    self.global_best_distance = particle.personal_best_distance

            self.epochs += 1


    def get_best_solution(self):
        return self.global_best_position, self.global_best_distance