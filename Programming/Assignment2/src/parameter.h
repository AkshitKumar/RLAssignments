#ifndef __PARAMETER_H_
#define __PARAMETER_H_

// Types - young, breedable, old
#define NUM_COW_TYPES 3
#define MAX_OFFSPRINGS 2
#define NUM_COWS 12
#define MAX_STATE_NUMBER 455

#define CONVERGENCE_EPS 1e-9
#define GAMMA 0.9
// Total possible states : 454 + 1

#define TEST_INPUT_1 768
#define TEST_INPUT_2 214
#define TEST_INPUT_3 1548

#include "header.h"

extern map<int, int> compress_naming;
extern map<int, int> rev_naming;
extern ll factorial[NUM_COWS+1];

extern double expected_payoff[NUM_COW_TYPES];
extern double expected_utility[NUM_COW_TYPES];

extern double transition_probability[NUM_COW_TYPES][NUM_COW_TYPES];

extern double offspring_probability[NUM_COW_TYPES][MAX_OFFSPRINGS+1];

extern double evolve_prob[MAX_STATE_NUMBER][MAX_STATE_NUMBER];
extern double reproduction_prob[MAX_STATE_NUMBER][MAX_STATE_NUMBER];
extern double afterstate_to_state[MAX_STATE_NUMBER][MAX_STATE_NUMBER];

#endif //__PARAMETER_H_

