import random

class Particle:
    def __init__(self, initial_position, initial_velocity, tsplib_problem):
        self.position = initial_position
        self.velocity = initial_velocity 

        self.tsplib_problem = tsplib_problem 
        self.personal_best_position = initial_position 
        self.personal_best_distance = self.current_total_distance(initial_position)


    def current_total_distance(self, position):
        total_distance = 0
        for i in range(len(position) - 1):
            total_distance += self.tsplib_problem.get_weight(position[i], position[i+1])
        
        return total_distance


    @staticmethod
    def get_swap_sequence(curr, target):
        curr = curr[:]
        swaps = []
        for i in range(len(curr)):
            if curr[i] != target[i]:
                j = curr.index(target[i])
                curr[i], curr[j] = curr[j], curr[i]
                swaps.append((i, j))
        return swaps

    def sample_social_cognitive(self, swaps, coefficient):
        num_swaps = max(1, int(len(swaps) * coefficient * random.random())) if swaps else 0
        sampled_swaps = swaps[:num_swaps]
        return sampled_swaps

    def sample_inertial(self, swaps, inertia_weight):
        num_swaps = max(1, int(len(swaps) * inertia_weight)) if swaps else 0
        sampled_swaps = swaps[:num_swaps]
        return sampled_swaps

    
    def update_velocity(self, global_best_position, inertia_weight, cognitive_coefficient, social_coefficient, velocity_cap=10):
        gswaps = self.get_swap_sequence(self.position, global_best_position)
        pswaps = self.get_swap_sequence(self.position, self.personal_best_position)

        sampled_gswaps = self.sample_social_cognitive(gswaps, social_coefficient)
        sampled_pswaps = self.sample_social_cognitive(pswaps, cognitive_coefficient)
        inertia_swaps = self.sample_inertial(self.velocity, inertia_weight)

        new_velocity = inertia_swaps + sampled_gswaps + sampled_pswaps
        random.shuffle(new_velocity)
        self.velocity = new_velocity[:velocity_cap]

    def update_position(self):
        for swap in self.velocity:
            i, j = swap
            self.position[i], self.position[j] = self.position[j], self.position[i]

        current_distance = self.current_total_distance(self.position)
        if current_distance < self.personal_best_distance:
            self.personal_best_position = self.position[:]
            self.personal_best_distance = current_distance
